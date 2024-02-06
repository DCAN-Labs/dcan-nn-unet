from os import listdir
from os.path import isfile, join

my_path = '/home/feczk001/shared/projects/nnunet_predict/nnunet_echo_input/'
only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
only_files.sort()
for i in range(len(only_files) // 2):
    file_1 = only_files[2 * i]
    assert file_1.endswith('T1w_0000.nii.gz')
    base_1 = file_1[:-15]
    file_2 = only_files[2 * i + 1]
    assert file_2.endswith('T2w_0001.nii.gz')
    base_2 = file_2[:-15]
    assert base_1 == base_2
