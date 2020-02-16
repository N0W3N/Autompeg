from configparser import ConfigParser
import sys
import os

config = ConfigParser(allow_no_value=True)

def checker():
    ffmpeg_path = input("File path of FFmpeg: ")
    if os.path.exists('config.ini'):
        print('Config file already exists.')
        with open('config.ini', 'r') as cfg:
            path = config.get('Path of ffmpeg', 'path')
            if path in ffmpeg_path:
                print("File path is also the same as in the config file.")
                pass
                sys.exit()
    else:
        return ffmpeg_path


def config_writer(ffmpeg_path):
    config.add_section('Path of ffmpeg')
    config.set('Path of ffmpeg', 'Path', str(ffmpeg_path))

    with open('config.ini', 'w') as cfg:
        config.write(cfg)
        print('Config has successfully created. \n'
              f'Path of ffmpeg as been set to {ffmpeg_path}')


def main():
    config_writer(checker())


if __name__ == '__main__':
    main()
