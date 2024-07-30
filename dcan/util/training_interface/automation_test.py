import argparse
import os
import shutil
import sys
import subprocess
import time

from os.path import isfile, join

processess = []

def get_job_id_by_name(job_name):
    # Run the squeue command and capture the output
    result = subprocess.run(['squeue', '--name', job_name, '--format', '%.18i %.9P %.50j %.8u %.2t %.10M %.6D %R'], capture_output=True, text=True)
    
    # Extract the job ID from the output
    output = result.stdout.splitlines()
    if len(output) > 1:
        # Assuming the first line is the header, get the first job ID from the second line
        job_id = output[1].split()[0]
        return job_id
    else:
        return None

def check_complete(job_id):
    f = open(f"{args.slurm_scripts_path}545_{i}_Train_nnUNet-{job_id}.err")
    lines = f.readlines()
    
    for line in lines:
        if "DUE TO TIME LIMIT" in line:
            print(f"JOB {job_id} STOPPED DUE TO TIME LIMIT")
            return False
    
    return True
    
def is_job_running(job_id):
    """Check if the job with the given job_id is still running."""
    result = subprocess.run(['squeue', '--job', str(job_id)], capture_output=True, text=True)
    return str(job_id) in result.stdout

def wait_for_job_to_finish(job_id, check_interval=60):
    """Wait until the job with the given job_id is no longer running."""
    while is_job_running(job_id):
        print(f"Job {job_id} is still running. Waiting...")
        time.sleep(check_interval)
    print(f"Job {job_id} has finished.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dcan_path')
    parser.add_argument('task_path')
    parser.add_argument('synth_path')
    parser.add_argument('raw_data_base_path')
    parser.add_argument('slurm_scripts_path')

    parser.add_argument('modality')
    parser.add_argument('task_number')
    parser.add_argument('distribution')
    parser.add_argument('synth_img_amt')

    args = parser.parse_args()

    # SETTING PATHS
    os.environ["PYTHONPATH"] = f"{args.synth_path}:{args.synth_path}SynthSeg/:{args.dcan_path}:{args.dcan_path}dcan/"
    os.environ["nnUNet_raw_data_base"] = f"{args.raw_data_base_path}"
    os.environ["nnUNet_preprocessed"] = f"{args.raw_data_base_path}nnUNet_preprocessed/"
    os.environ["RESULTS_FOLDER"] = f"{args.raw_data_base_path}nnUNet_trained_models/"
    
    # test_run: bash /home/faird/efair/projects/dcan-nn-unet/dcan/util/export_automation_test.sh /home/faird/efair/projects/dcan-nn-unet/ /scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/nnUNet_raw_data/Task545/ /home/faird/efair/projects/SynthSeg/ /scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/ t2 545 uniform 50
    '''
    # RESIZING IMAGES
    print("--- Now Resizing Images ---")
    p = subprocess.run(["python", f'{args.dcan_path}dcan/img_processing/resize_images_test.py', args.task_path])
    processess.append(p)
    print("--- Images Resized ---")
    
    # MINS/MAXES
    print("--- Now Creating Min Maxes ---")
    os.chdir(f'{args.synth_path}')
    subprocess.run(["python", f'{args.synth_path}SynthSeg/dcan/ten_fold_uniformity_estimation_one_task.py', args.task_path, f'./data/labels_classes_priors/dcan/uniform/mins_maxes_task_{args.task_number}.npy'])
    print("--- Min Maxes Created ---")
    
    #SYNTHSEG
    print("--- Now Creating Synthetic Images ---")
    os.chdir(f'{args.synth_path}')
    subprocess.run(["python", f'./SynthSeg/dcan/image_generation_for_all_ages.py', args.task_path, f'{args.task_path}SynthSeg_generated/', f'{args.synth_path}data/labels_classes_priors/dcan/uniform/mins_maxes_task_{args.task_number}.npy', args.synth_img_amt, f'--modalities={args.modality}', f'--distribution={args.distribution}'])
    print("--- SynthSeg Images Generated ---")
    
    # COPYING OVER IMAGE FILES
    print("--- Now Moving Over SynthSeg Generated Images ---")
    os.chdir(f'{args.dcan_path}dcan/util/')
    subprocess.run(["python", f'copy_over_augmented_image_files.py', f'{args.task_path}SynthSeg_generated/images/', f'{args.task_path}imagesTr/', f'{args.task_path}labelsTr/'])
    subprocess.run(["python", f'copy_over_augmented_image_files.py', f'{args.task_path}SynthSeg_generated/labels/', f'{args.task_path}imagesTr/', f'{args.task_path}labelsTr/'])
    os.chdir(f'{args.task_path}')
   
    subprocess.run(f'mv ./imagesTr/*_SynthSeg_generated_0000.nii.gz ./labelsTr/ -v', shell=True)
    subprocess.run(f'mv ./imagesTr/*_SynthSeg_generated_0001.nii.gz ./labelsTr/ -v', shell=True)
    #subprocess.run(['ls', f'./imagesTr/', '|', 'wc', '-l'])
    #subprocess.run(['ls', f'./labelsTr/', '|', 'wc', '-l'])
    subprocess.run(['rm', f'SynthSeg_generated/', '-r'])
    
    print("--- Images Moved ---")
    
    # CREATING JSON
    print("--- Now Creating Dataset json ---")
    os.chdir(f'{args.task_path}')
    subprocess.run(["python", f'{args.dcan_path}dcan/dataset_conversion/create_json_file.py', f'Task{args.task_number}', f'{args.dcan_path}look_up_tables/Freesurfer_LUT_DCAN.txt', f'--modalities={args.modality}'])
    subprocess.run(["python", f'{args.dcan_path}dcan/dataset_conversion/fix_json_file.py', './dataset.json', './dataset2.json', f'{args.dcan_path}look_up_tables/Freesurfer_LUT_DCAN.txt'])
    os.remove(f'{args.task_path}dataset.json')
    os.rename(f'{args.task_path}dataset2.json', f'{args.task_path}dataset.json')
    print("--- Dataset json Created ---")
    
    # Running Plan and Preprocess
    print("--- Now Running Plan and Preprocess ---")
    
    os.chdir(f"{args.slurm_scripts_path}")
    subprocess.run(["sbatch", "-W", "NnUnet_plan_and_preprocess_agate.sh"])
    print("--- Finished Plan and Preprocessing ---")
    '''
    
    # Training Model
    print("--- Now Running Nnunet Training ---")
    job_ids = [0, 0, 0, 0, 0]
    complete = [False, False, False, False, False]
    
    os.chdir(f"{args.slurm_scripts_path}")
    subprocess.run(["sbatch", "-W", "NnUnetTrain_agate.sh", "0", "faird"])
    
    # Start first fold and wait for initial steps
    job_ids[0] = get_job_id_by_name(f"545_0_Train_nnUNet")
    
    # Start next folds
    for i in range(1, 3):
        subprocess.run(["sbatch", "-W", "NnUnetTrain_agate.sh", f"{i}", "faird"])
        job_ids[i] = get_job_id_by_name(f"545_{i}_Train_nnUNet")
    
    # Keep running folds untill all of them are done
    while not all(complete[i] == True for i in range(3)):
        for i in range(3):
            # Wait for first fold to finish and check the error file. If it terminated due to time limit, run it again with the -c argument
            wait_for_job_to_finish(job_ids[i])
            check_complete(job_ids[i])
            if complete[i] == False:
                subprocess.run(["sbatch", "-W", "NnUnetTrain_agate.sh", f"{i}", "faird", "-c"])
                job_ids[i] = get_job_id_by_name(f"545_{i}_Train_nnUNet")
    
    print("--- Finished Training ---")