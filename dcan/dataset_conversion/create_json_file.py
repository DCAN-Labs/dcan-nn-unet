"""
Create JSON file.

Usage:
  create_json_file <task_name> [<look_up_table_path>]
  create_json_file -h | --help

Options:
  -h --help     Show this screen.
"""

from collections import OrderedDict
from os.path import join

from docopt import docopt

from dcan.dataset_conversion.utils import generate_dataset_json
from dcan.paths import nnUNet_raw_data
from dcan.util.look_up_tables import get_id_to_region_mapping


def fill_in_labels(free_surfer_label_to_region):
    n = max(free_surfer_label_to_region.keys())
    for i in range(1, n):
        if i not in free_surfer_label_to_region.keys():
            free_surfer_label_to_region[i] = 'unknown-' + str(i)
    dict1 = OrderedDict(sorted(free_surfer_label_to_region.items()))

    return dict1


def main(task, free_surfer_color_lut='/home/miran045/reine097/projects/abcd-nn-unet/look_up_tables/Freesurfer_LUT_DCAN.md'):
    target_base = join(nnUNet_raw_data, task)
    target_images_tr = join(target_base, "imagesTr")
    target_images_ts = join(target_base, "imagesTs")
    free_surfer_label_to_region = get_id_to_region_mapping(free_surfer_color_lut)
    consecutive_labels_to_regions = fill_in_labels(free_surfer_label_to_region)

    generate_dataset_json(join(target_base, 'dataset.json'), target_images_tr, target_images_ts, ('T1', 'T2'),
                          labels=dict(consecutive_labels_to_regions), dataset_name=task, lcns='hands off!')


if __name__ == '__main__':
    args = docopt(__doc__)
    task_name = args['<task_name>']
    if not args['<look_up_table_path>']:
        main(task_name)
    else:
        main(task_name, args['<look_up_table_path>'])
