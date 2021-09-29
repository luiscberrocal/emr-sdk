import csv
import os
import platform
import random
from datetime import datetime
from pathlib import Path
from time import sleep

import speedtest


def write_header(output_filename):
    with open(output_filename, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['computer', 'ssid', 'time_stamp', 'Download MB/s',
                             'Upload MS/s', 'Comment'])


def measure_speed(output_filename, computer, ssid, frequency=600,
                  measurement_count=100, comment=''):
    write_header(output_filename)
    for i in range(1, measurement_count):
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

        print(f'{i}/{measurement_count}. Download: {download} MB/s {comment}')
        print(f'       Upload  : {upload} MB/s')
        print(f'Waiting {waiting_for/60} min')
        print('-' * 50)
        with open(output_filename, 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([computer, ssid, time_stamp, download, upload, log_comment])
        sleep(waiting_for)


if __name__ == '__main__':
    output_fn = Path(__file__).parent.parent / \
                f'output/speed_test_mac_{datetime.now().strftime("%Y-%m-%d_%H%M")}.csv'
    computer_name = platform.node()
    print(computer_name)
    ssid = 'New Beggining'
    comment = '2.4GHz off'
    measure_speed(output_fn, computer_name, ssid, comment=comment)
