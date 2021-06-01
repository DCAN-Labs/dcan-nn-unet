from nnunet.dataset_conversion.Task001_BrainABCD import get_id_to_region_mapping, fill_in_labels
import sys


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
                free_surfer_color_lut = '/home/miran045/reine097/projects/abcd-nn-unet/nnunet/dataset_conversion' \
                                        '/Freesurfer_LUT_DCAN.md'
                free_surfer_label_to_region = get_id_to_region_mapping(free_surfer_color_lut)
                consecutive_labels_to_regions = fill_in_labels(free_surfer_label_to_region)
                for label in consecutive_labels_to_regions:
                    region = consecutive_labels_to_regions[label]
                    line = '        "{}": "{}"'.format(label, region)
                    if label != 14175:
                        line += ","
                    line += "\n"
                    writer.write(line)
            elif in_regions and '},' in line:
                writer.write(line)
                in_regions = False
            elif not in_regions:
                writer.write(line)


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
