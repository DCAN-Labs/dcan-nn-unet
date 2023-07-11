How-To
======

* Once a nnU-Net/BIBSNet model has been trained and selected to be placed into the BIBSNet container a few potential steps remain
* For starters, launch an interactive session on mesabi/mangi/agate. Something like this should work:
* 
      srun -N 1 --ntasks-per-node=10  --mem-per-cpu=4gb -t 5:00:00 -p interactive --pty bash

* Next, the requisite environment variables and environment must be defined. Copy and paste the following commands into your MSI terminal:

      export nnUNet_raw_data_base="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/"
      export nnUNet_preprocessed="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_preprocessed"
      export RESULTS_FOLDER="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models"
      source /panfs/roc/msisoft/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
      module load gcc cuda/11.2
      source /panfs/roc/msisoft/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
      conda activate /home/support/public/torch_cudnn8.2
All trained models on MSI for are here: 

  * */home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models/nnUNet/3d_fullres*

  1. The first step is to try whether the command nnUNet_export_model_to_zip just works on your model

   1.1. For example: `nnUNet_export_model_to_zip -t <Task ID> -m 3d_fullres -o <Task ID>.zip`
   
   1.2. If this generates a zip file for you, skip to step 4

   1.3. It is very likely that you will get the following error message. If so move onto step 2:


    Traceback (most recent call last):
      File "/home/support/public/torch_cudnn8.2/bin/nnUNet_export_model_to_zip", line 8, in <module>
        sys.exit(export_entry_point())
      File "/home/support/public/torch_cudnn8.2/lib/python3.9/site-packages/nnunet/inference/pretrained_models/collect_pretrained_models.py", line 253, in export_entry_point
        export_pretrained_model(taskname, args.o, args.m, args.tr, args.trc, args.pl, strict=not args.disable_strict,
      File "/home/support/public/torch_cudnn8.2/lib/python3.9/site-packages/nnunet/inference/pretrained_models/collect_pretrained_models.py", line 191, in export_pretrained_model
        raise RuntimeError('postprocessing.json missing. Run nnUNet_determine_postprocessing or disable strict')
    RuntimeError: postprocessing.json missing. Run nnUNet_determine_postprocessing or disable strict
  
2. To produce the required postprocessing.json file two different nnU-Net commands are needed, *nnUNet_determine_postprocessing* and *nnUNet_find_best_configuration*.
    
2.1. First *nnUNet_determine_postprocessing*: 
    
    nnUNet_determine_postprocessing -t <Task ID> -m 3d_fullres

2.2. Second *nnUNet_find_best_configuration*: 

    nnUNet_find_best_configuration -t <Task ID> -m 3d_fullres

This will take some time, be patient
When it finishes the text 'done' will be sent to standard output (or the terminal)
Once step 2 finishes, try repeating step 1

4. If a ZIP file has been created with the model, it can now be placed into the MSI S3 bucket that houses all BIBSNet models
To place ZIP file into bucket type: 

        s3cmd put </path/to/zip/file> s3://CABINET_data 
    
Next, ensure that the ZIP file just placed in the bucket is available publicly by typing:
     
    s3cmd --acl-public setacl s3://CABINET_data/<ZIP filename>
    
A test to ensure this worked is to see whether the file can be downloaded from the web
Open a web browser and type input the following URL:

    https://s3.msi.umn.edu/CABINET_data/<ZIP filename>

If the file begins downloading, you are done!
