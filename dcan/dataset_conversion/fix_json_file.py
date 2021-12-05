# Author: Paul Reiners

import argparse
from collections import OrderedDict


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
    free_surfer_label_to_region[0] = "Background"
    n = max(free_surfer_label_to_region.keys())
    for i in range(1, n):
        if i not in free_surfer_label_to_region.keys():
            free_surfer_label_to_region[i] = 'unknown-' + str(i)
    dict1 = OrderedDict(sorted(free_surfer_label_to_region.items()))

    return dict1


def main(input_f):
    with open(input_f, 'r') as reader:
        # Note: readlines doesn't trim the line endings
        lines = reader.readlines()

    new_lines = []

    in_regions = False
    for line in lines:
        if '"labels": {' in line:
            in_regions = True
            new_lines.append(line)
            free_surfer_color_lut = '../../look_up_tables/Freesurfer_LUT_DCAN.md'
            free_surfer_label_to_region = get_id_to_region_mapping(free_surfer_color_lut)
            consecutive_labels_to_regions = fill_in_labels(free_surfer_label_to_region)
            for label in consecutive_labels_to_regions:
                region = consecutive_labels_to_regions[label]
                line = '        "{}": "{}"'.format(label, region)
                # TODO Hack below.  Come up with something better.
                if label != 172:
                    line += ","
                new_lines.append(line)
                new_lines.append("\n")
        elif in_regions and '},' in line:
            new_lines.append(line)
            in_regions = False
        elif not in_regions:
            new_lines.append(line)
    with open(input_f, 'w') as writer:
        writer.writelines(new_lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix nnU-Net JSON file.')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    main(args.input_file)
