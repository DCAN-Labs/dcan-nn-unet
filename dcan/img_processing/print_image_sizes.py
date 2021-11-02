from os import listdir
from os.path import isfile, join
import nibabel as nib

path = '/home/feczk001/shared/projects/nnunet_predict/nnunet_echo_input/to_run/'
only_files = [f for f in listdir(path) if isfile(join(path, f))]

for f in only_files:
    img = nib.load(join(path, f))
    print(f, img.shape)
