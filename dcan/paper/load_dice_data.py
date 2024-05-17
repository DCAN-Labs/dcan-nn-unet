import pickle
import sys
import csv

from util.look_up_tables import get_id_to_region_mapping


def load_data(data_location, csv_location):
    dbfile = open(data_location, 'rb')
    free_surfer_color_lut = '/home/miran045/reine097/projects/abcd-nn-unet/look_up_tables' \
                            '/Freesurfer_LUT_DCAN.txt'
    db = pickle.load(dbfile)
    free_surfer_label_to_region = get_id_to_region_mapping(free_surfer_color_lut)
    with open(csv_location, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['reference', 'segment_name', 'Dice'])
        for keys in db:
            for dice_score in db[keys]:
                writer.writerow([keys, free_surfer_label_to_region[keys], dice_score])
    dbfile.close()


if __name__ == "__main__":
    load_data(sys.argv[1], sys.argv[2])
