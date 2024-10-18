import argparse
from collections import OrderedDict

from dcan.dataset_conversion.create_json_file import get_label_dict


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
    dict1 = get_label_dict(free_surfer_label_to_region)

    return dict1


def main(input_f, output_f):
    with open(input_f, 'r') as reader:
        # Note: readlines doesn't trim the line endings
        lines = reader.readlines()

    with open(output_f, 'w') as writer:
        in_regions = False
        for line in lines:
            if '"labels": {' in line:
                in_regions = True
                writer.write(line)
                # TODO: generalize hard coded path
                free_surfer_color_lut = args.lookup_table_path
                free_surfer_label_to_region = get_id_to_region_mapping(free_surfer_color_lut)
                consecutive_labels_to_regions = fill_in_labels(free_surfer_label_to_region)
                for label in consecutive_labels_to_regions:
                    region = consecutive_labels_to_regions[label]
                    line = '        "{}": "{}"'.format(label, region)
                    if not (label == 14175 and "FreesurferColorLUT.txt" in free_surfer_color_lut) and not (label == 172 and "Freesurfer_LUT_DCAN.txt" in free_surfer_color_lut):
                        line += ","
                    line += "\n"
                    writer.write(line)
            elif in_regions and '},' in line:
                writer.write(line)
                in_regions = False
            elif not in_regions:
                writer.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix nnU-Net JSON file.')
    parser.add_argument('input_file', help='input file')
    parser.add_argument('output_file', help='output file')
    parser.add_argument('lookup_table_path', help='lookup table path')
    args = parser.parse_args()

    main(args.input_file, args.output_file)
