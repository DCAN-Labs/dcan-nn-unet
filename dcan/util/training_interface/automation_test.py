import argparse
import os
import shutil
import sys
import subprocess
import time

from os.path import isfile, join

processes = []

def get_job_id_by_name(job_name, fold):
    # Get the job ID with a specified job name
    result = subprocess.run(['squeue', '--name', job_name, '--format', '%.18i %.9P %.50j %.8u %.2t %.10M %.6D %R'], capture_output=True, text=True)
    
    # Extract the job ID from the output
    output = result.stdout.splitlines()
    if len(output) > 1:
        # Assuming the first line is the header, get the first job ID from the second line
        job_id = output[1].split()[0]
        # Wait for necessary files to be made
        break_count = 0
        # Only do this for train step, other steps will have fold number -1
        # Waits for the necessary files to be made
        if fold >= 0:
            while (not os.path.isfile(os.path.join(slurm_scripts_path, f"Train_{fold}_{args.task_number}_nnUNet-{job_id}.out"))) or (not os.path.isfile(os.path.join(slurm_scripts_path, f"Train_{fold}_{args.task_number}_nnUNet-{job_id}.out"))):
                time.sleep(5)        
                break_count += 1
                if break_count >= 4000:
                    print("Job couldn't start, you may try reruning the program from the training step")
                    subprocess.run(["scancel", job_id])
                    exit()
        return job_id
    else:
        return None

def check_complete(job_id, fold):
    # Checks if a job finished due to time limit or completion by reading the .err file
    f = open(os.path.join(slurm_scripts_path, f"Train_{fold}_{args.task_number}_nnUNet-{job_id}.err"))
    lines = f.readlines()
    f.close()
    for line in lines:
        # If anywhere in the code, it says DUE TO TIME LIMIT, the training has not finished
        if "DUE TO TIME LIMIT" in line:
            print(f"Fold {fold} training stopped due to time limit. Resuming now...")
            return False
    print(f"Fold {fold} Training Complete.")
    return True
    
def is_job_running(job_id):
    # Checks if a certain job is still running
    result = subprocess.run(['squeue', '--job', str(job_id)], capture_output=True, text=True)
    return str(job_id) in result.stdout

def wait_for_job_to_finish(job_id, fold, check_interval=60):
    # Waits untill job is done running
    printCondition = 0
    while is_job_running(job_id):
        # Check if the job has finished every 60 seconds but update the user in the terminal once an day if it is still running
        if printCondition % 1140 == 0 and fold >= 0:
            print(f"Waiting for fold {fold} to complete training...")
        if printCondition % 60 == 0 and fold == -1:
            print(f"Waiting for inference to complete...")
        printCondition += 1
        time.sleep(check_interval)
        
def is_training_ready(job_id):
    # Checks if initial fold has run up to the epochs step by reading the .out file
    f = open(os.path.join(slurm_scripts_path, f"Train_0_{args.task_number}_nnUNet-{job_id}.out"))
    lines = f.readlines()
    f.close()
    for line in lines:
        # If epoch 0 has started, the next folds are ready to be run
        if "epoch:  0" in line or "epoch: 0" in line:
            print(f"Preperation complete. Ready to continue training on the rest of the folds.")
            return True
    return False
        
def wait_fold_0_setup(job_id, check_interval=60):
    # Waits for initial setup process to finish (until epochs)
    printCondition = 0
    while not is_training_ready(job_id):
        # Check if the preperation steps have finished every 60 seconds but update the user in the terminal every 30 minutes
        if printCondition % 30 == 0:
            print(f"Setup in progress...")
        printCondition += 1
        time.sleep(check_interval)
        
def set_up_slurm_scripts_folder(script_path, task_number):
    scripts = ["SynthSeg_image_generation.sh", "NnUnet_plan_and_preprocess_agate.sh", "NnUnetTrain_agate.sh", "infer_agate.sh", "create_min_maxes.sh"]
    # Set up the slurm scripts
    if not os.path.isdir(slurm_scripts_path):
        os.mkdir(slurm_scripts_path)
    for s in scripts:
        if not os.path.isfile(os.path.join(slurm_scripts_path, s)):
            shutil.copyfile(os.path.join(all_slurm_path, s), os.path.join(slurm_scripts_path, s))
            
def move_files(src_dir, dst_dir, pattern):
    for filename in os.listdir(src_dir):
        if pattern in filename:
            src_file = os.path.join(src_dir, filename)
            dst_file = os.path.join(dst_dir, filename)
            shutil.move(src_file, dst_file)            

 ### RESIZING IMAGES ###
def resize_images():
        print("--- Now Resizing Images ---")
        p = subprocess.run(["python", os.path.join(args.dcan_path, "dcan", "img_processing", "resize_images_test.py"), args.task_path])
        print("--- Images Resized ---")
    
### SETTING UP MINS/MAXES ###
def min_max():
    print("--- Now Creating Min Maxes ---")
    os.chdir(slurm_scripts_path)
    subprocess.run(["sbatch", "-W", os.path.join(slurm_scripts_path, "create_min_maxes.sh"), args.synth_path, args.task_path, os.path.join(script_dir, "min_maxes", f"mins_maxes_task_{args.task_number}.npy")])
    print("--- Min Maxes Created ---")

### CREATING SYNTHETICS ###
def SynthSeg_img():
    print("--- Now Creating Synthetic Images ---")
    os.chdir(slurm_scripts_path)
    subprocess.run(["sbatch", "-W", os.path.join(slurm_scripts_path, "SynthSeg_image_generation.sh"), args.synth_path, args.task_path, os.path.join(script_dir, "min_maxes", f"mins_maxes_task_{args.task_number}.npy"), args.synth_img_amt, f'--modalities={args.modality}', f'--distribution={args.distribution}'])
    print("--- SynthSeg Images Generated ---")

### COPYING OVER SYNTHSEG GENERATED IMAGE FILES ###
def copy_SynthSeg():
    print("--- Now Moving Over SynthSeg Generated Images ---")
    os.chdir(os.path.join(args.dcan_path, "dcan", "util"))
    subprocess.run(["python", f'copy_over_augmented_image_files.py', os.path.join(args.task_path, "SynthSeg_generated", "images"), os.path.join(args.task_path, "imagesTr"), os.path.join(args.task_path, "labelsTr")])
    subprocess.run(["python", f'copy_over_augmented_image_files.py', os.path.join(args.task_path, "SynthSeg_generated", "labels"), os.path.join(args.task_path, "imagesTr"), os.path.join(args.task_path, "labelsTr")])
    os.chdir(f'{args.task_path}')
    #subprocess.run(f'mv ./imagesTr/*_SynthSeg_generated_0000.nii.gz ./labelsTr/', shell=True)
    #subprocess.run(f'mv ./imagesTr/*_SynthSeg_generated_0001.nii.gz ./labelsTr/', shell=True)
    move_files("imagesTr", "labelsTr", "_SynthSeg_generated_0000.nii.gz")
    move_files("imagesTr", "labelsTr", "_SynthSeg_generated_0001.nii.gz")
    #subprocess.run(['ls', f'./imagesTr/', '|', 'wc', '-l'])
    #subprocess.run(['ls', f'./labelsTr/', '|', 'wc', '-l'])
    #subprocess.run(['rm', f'SynthSeg_generated/', '-r'])
    if os.path.exists("SynthSeg_generated"):
        shutil.rmtree("SynthSeg_generated")
    print("--- Images Moved ---")


### CREATING JSON ###
def create_json():
    print("--- Now Creating Dataset json ---")
    os.chdir(args.task_path)
    subprocess.run(["python", os.path.join(args.dcan_path, "dcan", "dataset_conversion", "create_json_file.py"), f'Task{args.task_number}', os.path.join(args.dcan_path, "look_up_tables", "Freesurfer_LUT_DCAN.txt"), f'--modalities={args.modality}'])
    subprocess.run(["python", os.path.join(args.dcan_path, "dcan", "dataset_conversion", "fix_json_file.py"), 'dataset.json', 'dataset2.json', os.path.join(args.dcan_path, "look_up_tables", "Freesurfer_LUT_DCAN.txt")])
    os.remove('dataset.json')
    os.rename('dataset2.json', 'dataset.json')
    print("--- Dataset json Created ---")

### RUNNING PLAN AND PREPROCESS ###
def p_and_p():

    print("--- Now Running Plan and Preprocess ---")
    os.chdir(slurm_scripts_path)
    subprocess.run(["sbatch", "-W", "NnUnet_plan_and_preprocess_agate.sh", args.raw_data_base_path, args.task_number])
    print("--- Finished Plan and Preprocessing ---")

### TRAINING MODEL ###
def model_training():
    print("--- Now Running Nnunet Training ---")
    
    job_ids = [0, 0, 0, 0, 0]
    complete = [False, False, False, False, False]
    
    # Start first fold and wait for initial steps
    os.chdir(slurm_scripts_path)
    
    subprocess.run(["sbatch", "-W", f"NnUnetTrain_agate.sh", "0", "faird", args.task_number, args.raw_data_base_path])
    job_ids[0] = get_job_id_by_name(f"{args.task_number}_0_Train_nnUNet", 0)
    wait_fold_0_setup(job_ids[0], 60)
    print("Begin training Fold 0.")
    
    # Start next folds
    for i in range(1, 5):
        print(f"Begin training Fold {i}")
        subprocess.run(["sbatch", "-W", f"NnUnetTrain_agate.sh", f"{i}", "faird", args.task_number, args.raw_data_base_path])
        job_ids[i] = get_job_id_by_name(f"{args.task_number}_{i}_Train_nnUNet", i)
        
    # Keep running folds untill all of them are done
    while not all(complete[i] == True for i in range(5)):
        for i in range(5):
            # Wait for first fold to finish and check the error file. If it terminated due to time limit, run it again with the -c argument
            wait_for_job_to_finish(job_ids[i], i, 60) 
            if check_complete(job_ids[i], i):
                complete[i] = True
            else:
                subprocess.run(["sbatch", "-W", f"NnUnetTrain_agate.sh", f"{i}", "faird", args.task_number, args.raw_data_base_path, "-c"])
                job_ids[i] = get_job_id_by_name(f"{args.task_number}_{i}_Train_nnUNet", i)
    print("--- Training Complete ---")

### INFERENCE ###
def inference():
    print("--- Starting Inference ---")
    if not os.path.isdir(os.path.join("home", "faird", "shared", "data", "nnUNet_lundq163", f"{args.task_number}_infer")):
        os.mkdir(os.path.join("home", "faird", "shared", "data", "nnUNet_lundq163", f"{args.task_number}_infer"))
    os.chdir(slurm_scripts_path)
    subprocess.run(["sbatch", "-W", f"infer_agate.sh", "faird", args.task_number, args.raw_data_base_path])
    id = get_job_id_by_name(f"{args.task_number}_infer", -1)
    wait_for_job_to_finish(id, -1, 60) 
    print("--- Inference Complete ---")
    #'''
    ### CREATE PLOTS
    print("--- Creating Plots ---")
    if not os.path.isdir(os.path.join("home", "faird", "shared", "data", "nnUNet_lundq163", f"{args.task_number}_results")):
        os.mkdir(os.path.join("home", "faird", "shared", "data", "nnUNet_lundq163", f"{args.task_number}_results"))
    os.chdir(os.path.join(args.synth_path, "SynthSeg", "dcan", "paper"))
    subprocess.run(["python", "evaluate_results.py", os.path.join(args.task_path, "labelsTs"), os.path.join("home", "faird", "shared", "data", "nnUNet_lundq163", f"{args.task_number}_infer"), os.path.join("home", "faird", "shared", "data", "nnUNet_lundq163", f"{args.task_number}_results")])
    print("--- Plots Creted ---")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dcan_path')
    parser.add_argument('task_path')
    parser.add_argument('synth_path')
    parser.add_argument('raw_data_base_path')
    parser.add_argument('modality')
    parser.add_argument('task_number')
    parser.add_argument('distribution')
    parser.add_argument('synth_img_amt')
    
 
    parser.add_argument('list')
    

    args = parser.parse_args()

    ### SETTING UP PATHS ###
    os.environ["PYTHONPATH"] = f"{args.synth_path}:{os.path.join(args.synth_path, 'SynthSeg')}:{args.dcan_path}:{os.path.join(args.dcan_path, 'dcan')}"
    os.environ["nnUNet_raw_data_base"] = args.raw_data_base_path
    os.environ["nnUNet_preprocessed"] = os.path.join(args.raw_data_base_path, "nnUNet_preprocessed")
    os.environ["RESULTS_FOLDER"] = os.path.join("home", "faird", "shared", "data", "nnUNet_lundq163", "nnUNet_raw_data_base", "nnUNet_trained_models")
    
    script_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(script_dir) 
    
    slurm_scripts_path = os.path.join(script_dir, "scripts", "slurm_scripts", args.task_number)
    all_slurm_path = os.path.join(script_dir, "scripts", "slurm_scripts")
    
    set_up_slurm_scripts_folder(script_dir, args.task_number)

    run_list = ['resize_images', 'min_max', 'SynthSeg_img', 'copy_SynthSeg', 'create_json','p_and_p','model_training', 'inference']
    
    if args.list[1]=='1':
        resize_images()
    if args.list[4]=='1':    
        min_max()
    if args.list[7]=='1': 
        SynthSeg_img()
    if args.list[10]=='1': 
        copy_SynthSeg()
    if args.list[13]=='1': 
        create_json()
    if args.list[16]=='1': 
        p_and_p()
    if args.list[19]=='1': 
        model_training()
    if args.list[22]=='1': 
        inference()
    print("PROGRAM COMPLETE!")