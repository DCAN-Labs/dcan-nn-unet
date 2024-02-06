from os import listdir
from os.path import isfile, join
import subprocess
import numpy as np
import matplotlib.pyplot as plt


logs_dir = '/home/feczk001/shared/projects/nnunet_predict/BCP/benchmark/slurm_scripts/logs/'
job_numbers = set()
only_files = [f for f in listdir(logs_dir) if isfile(join(logs_dir, f))]
for f in only_files:
    job_id = f[-11:-4]
    job_numbers.add(job_id)

gb_memory_utilized = []
for job_number in job_numbers:
    result = subprocess.run(['seff', job_number], stdout=subprocess.PIPE)
    lines = str(result.stdout).split('\\n')
    cpu_utilized_str = lines[6]
    memory_utilized_str = lines[9]
    gb = float(memory_utilized_str[17:22])
    gb_memory_utilized.append(gb)

n, bins, patches = plt.hist(gb_memory_utilized, 10, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Memory Utilized in GB')
plt.ylabel('Probability')
plt.title('Histogram of Memory Usage')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlim(16, 28)
plt.ylim(0, 2)
plt.grid(True)
plt.show()
