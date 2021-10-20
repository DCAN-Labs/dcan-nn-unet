from os.path import join
from collections import OrderedDict

from batchgenerators.utilities.file_and_folder_operations import *

from dcan.dataset_conversion.utils import generate_dataset_json
from dcan.paths import nnUNet_raw_data


def get_id_to_region_mapping(mapping_file_name, separator=None):
    file = open(mapping_file_name, 'r')
    lines = file.readlines()

    id_to_region = {}
    for line in lines:
        line = line.strip()
        if line.startswith('#') or line == '':
            continue
        if separator:
            parts = line.split(separator)
        else:
            parts = line.split()
        region_id = int(parts[0])
        region = parts[1]
        id_to_region[region_id] = region
    return id_to_region


def fill_in_labels(free_surfer_label_to_region):
    n = max(free_surfer_label_to_region.keys())
    for i in range(1, n):
        if i not in free_surfer_label_to_region.keys():
            free_surfer_label_to_region[i] = 'unknown-' + str(i)
    dict1 = OrderedDict(sorted(free_surfer_label_to_region.items()))

    return dict1


def main():
    task_name = 'Task001_BrainABCD'
    target_base = join(nnUNet_raw_data, task_name)
    target_images_tr = join(target_base, "imagesTr")
    target_images_ts = join(target_base, "imagesTs")
    free_surfer_color_lut = '/home/miran045/reine097/projects/BrainSegNet3D/notebooks/FreeSurferColorLUT.txt'
    free_surfer_label_to_region = get_id_to_region_mapping(free_surfer_color_lut)
    consecutive_labels_to_regions = fill_in_labels(free_surfer_label_to_region)

    generate_dataset_json(join(target_base, 'dataset.json'), target_images_tr, target_images_ts, ('T1',),
                          labels=dict(consecutive_labels_to_regions), dataset_name=task_name, lcns='hands off!')


if __name__ == '__main__':
    main()