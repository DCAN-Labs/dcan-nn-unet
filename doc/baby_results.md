nnU-Net Segmentation of Baby MRI Images
========================================

The goal of the project is to segment MRI scans (both T1-weighted 
and T2-weighted) of babies both accurately and reasonably quickly.

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

My second choice was [MIC-DKFZ / nnU-Net](https://github.com/MIC-DKFZ/nnUNet).
I also ran into many difficult problems in running nn-UNet
but these were due to MSI software and configuration problems and not due to the
nnU-Net code itself.  However, these were all resolved within a
week (or three) by working with MSI.  Some time was also spent
in finding the best SLURM parameters to optimize the running time
for training.

Run-time
--------

Inference time for one set of T1/T2 images takes about 2 minutes.

I spent a lot of time on optimizing the MSI
parameters to match the 
[benchmark run-times](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/expected_epoch_times.md#pytorch-171-compiled-with-cudnn-81077).
I was able to get within a factor of two of 
the benchmark.  So it might be possible to halve
our current run-time.  My experiments with
optimizing parameters are documented 
[here](./params-vs-epoch-time.csv).  The best
set of parameters I could find for MSI are
in [this SLURM script](../slurm/train/RunNnUnetTrain_102_0.sh).

Results
-------

* [0-2 months](./00-02mos_Template05.md)
* [8 months](./8mo_Template09.md)
* [All months (with age encoding)](./Task501_Babies_AllMonths.md)

### Dice coefficients

| Group      | Training/cross-validation set size | Dice coefficient | avg_epoch_time |
| ----------- | ----------- |-------------------|----------------|
| 00-02mos      | 4       | 0.03424693173990132 | 294.7903675987501 s |
| 500_Babies8Mo   | 8        | 0.9206427375735695 | 280.5509568585713 |
| 501_Babies_AllMonths   | 34        | 0.90412274421532315 | 314.8189190775993 |
| 502_Babies_AllMonthsAgeNotEncoded   | 34        | 0.903551078311636 | 286.16027479799993 |

Future directions
-----------------

1. Increase the training set size.  We currently
have about 20 subjects total.  I would recommend first trying a training set of size 10.  If nnU-Net scales linearly, this will take about 6 days to run.  Keep doubling the training set size until we're using all the data.  Establish the relationship between training set size and the resulting run-time and Dice coefficient.
2. If we don't get good results with a sufficiently large training set, go back and try SynthSeg or perhaps a third application.

Conclusions
-----------

I'm confident that
nnU-Net will do well with a sufficiently large
training set of baby T1 and T2 images that are
well-labelled.  To get a Dice coefficient of at least 0.9, a training/cross-validation set 
of at least size 8 seems to be necessary.  There are two practical
considerations for finishing this project:
manually creating the segmented data, and
the run-time for training on this data.  As I mentioned
earlier, it might be possible to halve the 
training run-time.  I can continue experimenting with the 
MSI parameters, or we could consult with MSI (the latter might be quicker).
Also, once we seem to have reached a plateau
with Dice coefficients, there are methods
for 
[extending and changing nnU-Net](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/extending_nnunet.md#extendingchanging-nnu-net) that could
better our results.
