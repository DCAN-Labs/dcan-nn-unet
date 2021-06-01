nnU-Net Segmentation of Baby MRI Images
========================================

The goal of the project is to segment MRI scans (both T1-weighted 
and T2-weighted) both accurately and reasonably quickly.

Software considerations
-----------------------

If at all possible, I wanted to use a well-established code base,
rather than write something from scratch.  I consulted the
[Papers with Code](https://paperswithcode.com/task/brain-segmentation) 
site for candidate software.  My first choice was 
[BBillot / SynthSeg](https://github.com/BBillot/SynthSeg).
Unfortunately, I ran into a [problem](https://github.com/BBillot/SynthSeg/issues/11) in using it.
I found out today that this problem was fixed an hour ago.  I
hope to go back to SynthSeg and try it again.

My second choice was [nnU-Net](https://github.com/MIC-DKFZ/nnUNet).
I also ran into many difficult problems in running nn-UNet
but these were due to MSI software and configuration problems and not due to the
nnU-Net code itself.  However, these were all resolved within a
week (or three) by working with MSI.  Some time was also spent
in finding the best SLURM parameters to optimize the running time
for training.

Initial data set
----------------

Because of all the unknowns and lack of knowledge of run-time
for training, I wanted to start with small training/validation/test
sets.  I wasn't expecting great results with this small training
set, but I did want to make sure that I could get nn-UNet to run
efficiently on MSI.  That was accomplished.  Because of [nn-UNet's
good results on other medical image segmentation problems](https://arxiv.org/pdf/1809.10486v1.pdf)
I am confident we will get good results with a sufficiently
large training set.

I used the following images given to me by Luci Moore:
* Training set
    * 00-02mos_Template01
    * 00-02mos_Template04
    * 00-02mos_Template07
    * 00-02mos_Template08
* Cross-validation set
    * 00-02mos_Template03
* Test set
    * 00-02mos_Template05

Run-time
--------

Training consists of five folds each of 1000 epochs.  Once
the first fold has done some preliminary set-up, the folds can be
run in parallel.  From examination of log files,
we get the following statistics:

    min_epoch_time: 240.548288
    max_epoch_time: 389.860017
    avg_epoch_time: 294.7903675987501
