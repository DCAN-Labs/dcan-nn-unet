import argparse
import os
import shutil
import sys
import subprocess

from os.path import isfile, join

processess = []







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

    args = parser.parse_args()


    os.environ["PYTHONPATH"] = f"{args.synth_path}:{args.synth_path}SynthSeg/:{args.dcan_path}:{args.dcan_path}dcan/"
    os.environ["nnUNet_raw_data_base"] = f"{args.raw_data_base_path}"
    os.environ["nnUNet_preprocessed"] = f"{args.raw_data_base_path}nnUNet_preprocessed/"
    os.environ["RESULTS_FOLDER"] = f"{args.raw_data_base_path}nnUNet_trained_models/"
    
    # test_run: bash /home/faird/efair/projects/dcan-nn-unet/dcan/util/export_automation_test.sh /home/faird/efair/projects/dcan-nn-unet/ /scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/nnUNet_raw_data/Task545/ /home/faird/efair/projects/SynthSeg/ /scratch.global/lundq163/nnUNet_HBCD_noFlip_noMirr/nnUNet_raw_data_base/ t2 545 uniform 50
    

    
    #subprocess.run(f"bash /home/faird/efair/projects/dcan-nn-unet/dcan/util/export_automation_test.sh {args.dcan_path} {args.task_path} {args.synth_path} {args.raw_data_base_path} {args.modality} {args.task_number} {args.distribution} {args.synth_img_amt}", shell=True)
    
    # RESIZING IMAGES
    print("Now Resizing Images")
    p = subprocess.run(["python", f'{args.dcan_path}dcan/img_processing/resize_images_test.py', args.task_path])
    processess.append(p)
    print("Images Resized")
    
    # MINS/MAXES
    print("Now Creating Min Maxes")
    os.chdir(f'{args.synth_path}')
    subprocess.run(["python", f'{args.synth_path}SynthSeg/dcan/ten_fold_uniformity_estimation_one_task.py', args.task_path, f'./data/labels_classes_priors/dcan/uniform/mins_maxes_task_{args.task_number}.npy'])
    print("Min Maxes Created")
    
    #SYNTHSEG
    print("Now Creating Synthetic Images")
    os.chdir(f'{args.synth_path}')
    subprocess.run(["python", f'./SynthSeg/dcan/image_generation_for_all_ages.py', args.task_path, f'{args.task_path}SynthSeg_generated/', f'{args.synth_path}data/labels_classes_priors/dcan/uniform/mins_maxes_task_{args.task_number}.npy', args.synth_img_amt, f'--modalities={args.modality}', f'--distribution={args.distribution}'])
    print("SynthSeg Images Generated")
    
    # COPYING OVER IMAGE FILES
    print("Now Moving Over SynthSeg Generated Images")
    os.chdir(f'{args.dcan_path}dcan/util/')
    subprocess.run(["python", f'copy_over_augmented_image_files.py', f'{args.task_path}SynthSeg_generated/images/', f'{args.task_path}imagesTr/', f'{args.task_path}labelsTr/'])
    subprocess.run(["python", f'copy_over_augmented_image_files.py', f'{args.task_path}SynthSeg_generated/labels/', f'{args.task_path}imagesTr/', f'{args.task_path}labelsTr/'])
    os.chdir(f'{args.task_path}')
   
    subprocess.run(f'mv ./imagesTr/*_SynthSeg_generated_0000.nii.gz ./labelsTr/ -v', shell=True)
    subprocess.run(f'mv ./imagesTr/*_SynthSeg_generated_0001.nii.gz ./labelsTr/ -v', shell=True)
    #subprocess.run(['ls', f'./imagesTr/', '|', 'wc', '-l'])
    #subprocess.run(['ls', f'./labelsTr/', '|', 'wc', '-l'])
    subprocess.run(['rm', f'SynthSeg_generated/', '-r'])
    
    print("Images Moved")
    
    # CREATING JSON
    print("Now Creating Dataset json")
    os.chdir(f'{args.task_path}')
    subprocess.run(["python", f'{args.dcan_path}dcan/dataset_conversion/create_json_file.py', f'Task{args.task_number}', f'{args.dcan_path}look_up_tables/Freesurfer_LUT_DCAN.txt', f'--modalities={args.modality}'])
    subprocess.run(["python", f'{args.dcan_path}dcan/dataset_conversion/fix_json_file.py', './dataset.json', './dataset2.json', f'{args.dcan_path}look_up_tables/Freesurfer_LUT_DCAN.txt'])
    os.remove(f'{args.task_path}dataset.json')
    os.rename(f'{args.task_path}dataset2.json', f'{args.task_path}dataset.json')
    print("Dataset json Created")
