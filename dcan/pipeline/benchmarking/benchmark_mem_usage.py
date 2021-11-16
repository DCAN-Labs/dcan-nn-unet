from os import listdir
from os.path import isfile, join
import random
import os
from shutil import copyfile


bcp_folder = '/home/feczk001/shared/projects/nnunet_predict/BCP/input/cropped_resized/'
output_folder = '/home/feczk001/shared/projects/nnunet_predict/BCP/benchmark/'
only_files = [f for f in listdir(bcp_folder) if isfile(join(bcp_folder, f))]
only_files.sort()
for i in range(20):
    rand_index = random.randrange(len(only_files) // 2)
    f1 = only_files[2 * rand_index]
    f2 = only_files[2 * rand_index + 1]
    rand_file1 = join(bcp_folder, f1)
    rand_file2 = join(bcp_folder, f2)
    new_output_folder = join(output_folder, f'{i:02d}')
    os.mkdir(new_output_folder)
    new_output_in_folder = join(new_output_folder, 'in')
    os.mkdir(new_output_in_folder)
    copyfile(rand_file1, join(new_output_in_folder, f1))
    copyfile(rand_file2, join(new_output_in_folder, f2))
    new_output_out_folder = join(new_output_folder, 'out')
    os.mkdir(new_output_out_folder)
    only_files.remove(f1)
    only_files.remove(f2)
