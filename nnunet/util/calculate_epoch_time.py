import os
import sys


def main(folder):
    min_epoch_time = float("inf")
    max_epoch_time = 0
    total_epoch_time = 0.0
    epoch_count = 0
    for filename in os.listdir(folder):
        if filename.endswith(".out"):
            file_path = os.path.join(folder, filename)
            print(file_path)
            out_file = open(file_path, "r")

            for aline in out_file:
                if 'This epoch took' in aline:
                    values = aline.split()
                    # 2021-05-24 18:39:06.280340: This epoch took 263.490468 s
                    epoch_time = float(values[5])
                    print('epoch time: ', epoch_time)
                    epoch_count += 1
                    total_epoch_time += epoch_time
                    if epoch_time < min_epoch_time:
                        min_epoch_time = epoch_time
                    if epoch_time > max_epoch_time:
                        max_epoch_time = epoch_time
            out_file.close()
        else:
            continue
    print('min_epoch_time:', min_epoch_time)
    print('max_epoch_time:', max_epoch_time)
    print('avg_epoch_time:', total_epoch_time / epoch_count)


if __name__ == "__main__":
    directory = sys.argv[1]
    main(directory)
