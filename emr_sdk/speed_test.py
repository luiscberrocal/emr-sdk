from time import sleep

import speedtest


def main():
    for i in range(1, 11):
        speed = speedtest.Speedtest()
        print(f'{i}. Download: {speed.download() / 1024 / 1024} MB/s')
        print(f'{i}. Upload  : {speed.upload() / 1024 / 1024} MB/s')
        print('-' * 50)
        sleep(5)


if __name__ == '__main__':
    main()
