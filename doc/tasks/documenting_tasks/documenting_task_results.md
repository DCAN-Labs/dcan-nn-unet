Documenting the results of a Task
=================================

Getting top-level results
-------------------------

```
Script path: /home/miran045/reine097/projects/abcd-nn-unet/dcan/evaluation/iou_dice_score.py
Sample args: /scratch.global/lundq163/nnUNet_HBCD/nnUNet_raw_data_base/nnUNet_raw_data/Task528/labelsTs/ /home/feczk001/shared/data/nnUNet/528_infer/
```

For creating images:

```
Script path: /home/miran045/reine097/projects/SynthSeg/SynthSeg/dcan/paper/evaluate_results.py
Sample args: /scratch.global/lundq163/nnUNet_HBCD/nnUNet_raw_data_base/nnUNet_raw_data/Task527/labelsTs/
/home/feczk001/shared/data/nnUNet/527_infer/
/home/feczk001/shared/data/nnUNet/527_results/
```

Creating markdown and plots of model applied to test set
--------------------------------------------------------

We will look at 538 as an example.  The steps below need to be applied sequentially.
The idea is to eventually stitch these all together in a single Python script.

### Organize ground truth files and inferred files.

The ground truth and inferred segmentations should be in 
[this sort of folder structure](./sample-dir-tree.txt).  Note the partitioning
by age group in months.  This will probably need to be made more flexible in the future.

There is a utility program for creating this kind of tree structure here:

    /home/miran045/reine097/projects/abcd-nn-unet/dcan/dataset_conversion/create_stats_markdown_and_plots/partition_by_age.py

### Create plots and supporting stats files.

Run

    SynthSeg/dcan/paper/create_stats_markdown_and_plots/create_all_cat_plots.py

Note that `src_dir` is hard-coded in this script.  Do not simply edit the path.  Generalize this by extracting it to a command-line argument.  <b>The same goes
for any other hard-coded structures you find.</b>

After this is done, you should find a folder of `catplot`s for each age group in the 
`results_folder` you specified.  Copy these over to the correct folders in doc/tasks.
This copying step should
be automated.

### Create markdown docs for each age group.

These are generated from a Jinja template.  Run this program:

    SynthSeg/dcan/paper/task/write_month_markdown.py

Run it from the SynthSeg root project folder so it can find the paths.

### Create top-level task markdown docs.

These include, e.g., 528.md and 528-all-measures.md.  I've been copying and pasting from old
versions.  This should probably be formalized with Jinja templates, though.


