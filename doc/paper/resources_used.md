# Computational resources used

In the table below, training resources are computed for training with 74 subjects.  The Job Wall-clock time is about 1 day as that is the maximum time allowed on the system we use.  In reality, training takes 3--5 days with five parallel folds running.

The inference task resources are for a single subject.

In both cases, a GPU is used.  The entries were computed using `seff`.  The entries are typical, not an average.

| | Nodes      | Cores per node | CPU Utilized | CPU Efficiency                         | Job Wall-clock time | Memory Utilized | Memory Efficiency  |
| ---- | ---------- | -------------- | ------------ | -------------------------------------- | ------------------- | --------------- | ------------------ |
| training | 1          | 24             | 00:00:00     | 0.00% of 24-00:06:00 core-walltime     |          1-00:00:15 |        39.42 GB | 61.60% of 64.00 GB |
| inference | 1          | 3              | 00:00:08     | 7.41% of 00:01:48 core-walltime        |            00:00:36 |         1.46 MB | 0.00% of 60.00 GB  |

