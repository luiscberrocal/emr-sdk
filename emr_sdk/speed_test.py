import csv
from datetime import datetime
from pathlib import Path
from time import sleep

import speedtest


def write_header(output_filename):
    with open(output_filename, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['computer', 'ssid', 'time_stamp', 'Download MB/s', 'Upload MS/s'])


def measure_speed(output_filename, computer, ssid, frequency):
    write_header(output_filename)
    for i in range(1, 11):
        speed = speedtest.Speedtest()
        dnld = speed.download() / 1024 / 1024
        upld = speed.upload() / 1024 / 1024
        print(f'{i}. Download: {dnld} MB/s')
        print(f'     Upload  : {upld} MB/s')
        print('-' * 50)
        with open(output_filename, 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            spamwriter.writerow([computer, ssid, time_stamp, dnld, upld])
        sleep(frequency)


if __name__ == '__main__':
    output_fn = Path(__file__).parent.parent / \
                f'output/speed_test_mac_{datetime.now().strftime("%Y-%m-%d_%H%M")}.csv'

    measure_speed(output_fn, 'MacBook Pro', 'New Beginning', 10)
