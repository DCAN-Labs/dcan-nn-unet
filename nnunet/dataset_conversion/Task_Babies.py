from os.path import join
from collections import OrderedDict
import sys

from batchgenerators.utilities.file_and_folder_operations import *

from nnunet.dataset_conversion.utils import generate_dataset_json
from nnunet.paths import nnUNet_raw_data
from nnunet.util.look_up_tables import get_id_to_region_mapping


def fill_in_labels(free_surfer_label_to_region):
    n = max(free_surfer_label_to_region.keys())
    for i in range(1, n):
        if i not in free_surfer_label_to_region.keys():
            free_surfer_label_to_region[i] = 'unknown-' + str(i)
    dict1 = OrderedDict(sorted(free_surfer_label_to_region.items()))

    return dict1


def main(task):
    target_base = join(nnUNet_raw_data, task)
    target_images_tr = join(target_base, "imagesTr")
    target_images_ts = join(target_base, "imagesTs")
    free_surfer_color_lut = \
        '/home/miran045/reine097/projects/abcd-nn-unet/nnunet/dataset_conversion/Freesurfer_LUT_DCAN.md'
    free_surfer_label_to_region = get_id_to_region_mapping(free_surfer_color_lut)
    consecutive_labels_to_regions = fill_in_labels(free_surfer_label_to_region)

    generate_dataset_json(join(target_base, 'dataset.json'), target_images_tr, target_images_ts, ('T1', 'T2'),
                          labels=dict(consecutive_labels_to_regions), dataset_name=task, lcns='hands off!')


if __name__ == '__main__':
    task_name = sys.argv[1]
    main(task_name)
