Running one training fold of nnU-Net
====================================

Before reading this document, the user should be familiar with nnU-Net
[model training](https://github.com/MIC-DKFZ/nnUNet#model-training), in general.

When training, five folds must be run.  After the first fold has done some initialization
work, the five folds can be run concurrently.  You can tell if the first fold has done
its initialization work by looking at its log file and seeing whether there is at least
one line like this:

    epoch:  n

where *n* is some integer.

Each set of data is given a task number.  Before you can do anything,
you have to add some lines to either your *.bashrc* or *.bash_profile* file:

    export nnUNet_raw_data_base="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/"
    export nnUNet_preprocessed="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_preprocessed"
    export RESULTS_FOLDER="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models"
    . /panfs/roc/msisoft/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh
    conda activate

Each of the five folds runs for 1000 epochs.  It takes about 3 days to run 1000 epochs.
You need to run nnU-Net on the *v100* partition.  However, the longest SLURM job
allowed on MSI v100 partitions is only 24 hours.  So you will need to restart the training job at least
a couple of times before all 1000 epochs have finished.  Epochs are numbered 0&ndash;4.
You can list the jobs running like this:

    -bash-4.2$ squeue -u reine097
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               4455653      v100 501_2_Tr reine097 PD       0:00      1 (Priority)
               4455667      v100 501_3_Tr reine097 PD       0:00      1 (Priority)
               4453638      v100 501_4_Tr reine097  R    2:33:01      1 cn2112
               4453620      v100 501_0_Tr reine097  R    3:07:39      1 cn2114

You will probably want to substitute your own user name.

From the naming convention of our jobs, we can see that fold 1 of task 500 isn't running.
Here is the call to run training on fold 1 of task 501 for the first time.  Do not run this yet,
though.

    nnUNet_train 3d_fullres nnUNetTrainerV2 501 1

If you are restarting the fold training because a previous fold 1 SLURM job timed out, this is the
invocation:

    nnUNet_train 3d_fullres nnUNetTrainerV2 501 1 -c

Note the *-c* an the end.  This stands for *continue*.

Now we show how to run a training fold on MSI.  As an example, we will run fold 1 of task 501.
Do the following.

1. Start up [NICE](https://www.msi.umn.edu/support/faq/how-do-i-obtain-graphical-connection-using-nice-system).
2. Log on to mesabi:
    
        ssh -Y mesabi
   
3. Change to the following directory:


        cd /home/faird/shared/code/internal/nnUNet/training/501/
   
4. Open the file *NnUnetTrain_501_1.sh*.  Note how the task number and fold number are coded
up in the file name.  Change the email addresses if necessary.  Also add the *-c* argument to the last line, if necessary.  Save and close the file.
   
5. Schedule the SLURM job like this:


        -bash-4.2$ sbatch NnUnetTrain_501_1.sh
        sbatch: Setting account: miran045
        Submitted batch job 4464201

6. Now we can see that fold 1 is scheduled to run:

        -bash-4.2$ squeue -u reine097
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           4455653      v100 501_2_Tr reine097 PD       0:00      1 (Priority)
           4455667      v100 501_3_Tr reine097 PD       0:00      1 (Priority)
           4464201      v100 501_1_Tr reine097 PD       0:00      1 (None)
           4453638      v100 501_4_Tr reine097  R    2:54:16      1 cn2112
           4453620      v100 501_0_Tr reine097  R    3:28:54      1 cn2114

7. You can monitor the progress of jobs with *squeue*.  You will also get emails when jobs start, stop, fail, and so on.

8. Another way to monitor a particular job is to check the end of its log file like this (we get the name of the log file from its task number, fold number, and process ID):

        -bash-4.2$ tail Train_501_0_nnUNet-4453620.out
        2021-06-21 08:13:03.053071: lr: 0.007941
        2021-06-21 08:13:03.054774: This epoch took 288.041806 s
        
        2021-06-21 08:13:03.056420: 
        epoch:  226
        2021-06-21 08:17:05.605214: train loss : -0.7531
        2021-06-21 08:17:47.605599: validation loss: -0.5259
        2021-06-21 08:17:47.610551: Average global foreground Dice: [0.9093312319493183, 0.7775973440464092, 0.7883118618657827, 0.0, 0.7126153014567062, 0.7973344590588927, 0.8420865344015805, 0.7777127228359223, 0.7488627842185367, 0.6716956145265625, 0.8649476300372803, 0.8467684857515366, 0.934550692204221, 0.7114458243135467, 0.7004558102755004, 0.790277366273902, 0.5591292460859921, 0.7497159825877642, 0.0, 0.5474940426603638, 0.9131458043005022, 0.7655945284606557, 0.7826127244463829, 0.0, 0.6828777534137347, 0.7603114516078773, 0.8524014006106162, 0.7901438637807238, 0.7500531958049559, 0.6916238951117923, 0.6961286767401325, 0.6749165965987686, 0.5679711863662318, 0.7697087281420936, 0.0, 0.5379228438037513, 0.0, 0.0, 0.729026368377782, 0.707422462567093, 0.6848011695845101, 0.6818664571834657, 0.7402420587522865]
        2021-06-21 08:17:47.611751: (interpret this as an estimate for the Dice of the different classes. This is not exact.)
        2021-06-21 08:17:48.132057: lr: 0.007932

The most important information here is the epoch number.  We can see that we're on epoch 226 of 1000.  "Average global foreground Dice" can also give you an idea how well the algorithm is performing at this point.

9. If the SLURM job times out before all 1000 epochs are finished, go back to step 5 and repeat, making sure the *-c* flag is set.

10. When all 1000 epochs are finished, you should get an email saying that the task finished with an exit code of 0.
