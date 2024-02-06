import subprocess
from os import listdir
from os.path import isfile, join

import matplotlib.pyplot as plt

logs_dir = '/home/feczk001/shared/projects/nnunet_predict/BCP/benchmark/slurm_scripts/logs/'
job_numbers = set()
only_files = [f for f in listdir(logs_dir) if isfile(join(logs_dir, f))]
for f in only_files:
    job_id = f[-11:-4]
    job_numbers.add(job_id)

cpu_utilized = []
for job_number in job_numbers:
    result = subprocess.run(['seff', job_number], stdout=subprocess.PIPE)
    lines = str(result.stdout).split('\\n')
    cpu_utilized_str = lines[6]
    minutes_and_seconds_str = cpu_utilized_str[-8:]
    hours, minutes, seconds = minutes_and_seconds_str.split(':')
    cpu_utilized.append(float(minutes) + float(seconds) / 60.0)

n, bins, patches = plt.hist(cpu_utilized, 10, density=True, facecolor='g', alpha=0.75)

plt.xlabel('CPU Utilized in Minutes')
plt.ylabel('Probability')
plt.title('Histogram of CPU Usage')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlim(5, 9)
plt.ylim(0, 2)
plt.grid(True)
plt.show()
