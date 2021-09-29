import csv
import os
import platform
import random
from datetime import datetime
from pathlib import Path
from time import sleep

import speedtest


def write_header(output_filename):
    with open(output_filename, 'w') as csv_file:
        csv_riter = csv.writer(csv_file)
        csv_riter.writerow(['computer', 'ssid', 'time_stamp', 'Download MB/s',
                             'Upload MS/s', 'Comment'])


def measure_speed(output_filename, computer, ssid, frequency=600,
                  measurement_count=100, comment=''):
    write_header(output_filename)
    for i in range(1, measurement_count):
        time_stamp = datetime.now()
        waiting_for = frequency+random.randint(60, 120)
        try:
            speed = speedtest.Speedtest()
            download = speed.download() / 1024 / 1024
            upload = speed.upload() / 1024 / 1024
            log_comment = comment
        except speedtest.SpeedtestBestServerFailure:
            download = 0
            upload = 0
            log_comment = 'Error'

        speed_data = [computer, ssid, time_stamp.strftime("%Y-%m-%d %H:%M:%S"), download, upload, log_comment]
        print_to_console(i, measurement_count, download, upload, log_comment, waiting_for, time_stamp)
        with open(output_filename, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(speed_data)
        sleep(waiting_for)


def print_to_console(i, measurement_count, download, upload, log_comment, waiting_for, time_stamp):
    print(f'{i:=3d}/{measurement_count:d}. Download: {download:5.2f} MB/s {log_comment}')
    print(f'       Upload  : {upload:5.2f} MB/s')
    print(f'Waiting {waiting_for / 60:.2f} min  {time_stamp.strftime("%a %H:%M:%S")}')
    print('-' * 50)


if __name__ == '__main__':
    output_fn = Path(__file__).parent.parent / \
                f'output/speed_test_mac_{datetime.now().strftime("%Y-%m-%d_%H%M")}.csv'
    computer_name = platform.node()
    print(computer_name)
    ssid = 'New Beggining'
    comment = '2.4GHz off'
    count = 3
    frequency_secs = 10
    measure_speed(output_fn, computer_name, ssid, comment=comment, frequency=frequency_secs,
                  measurement_count=count)
