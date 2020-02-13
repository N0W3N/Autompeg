from configparser import ConfigParser


config = ConfigParser(allow_no_value=True)

ffmpeg_path = input("Enter the path where ffmpeg is located: ")

config.add_section('Path of ffmpeg')
config.set('Path of ffmpeg', 'Path', str(ffmpeg_path))

try:
    with open('config.ini', 'w') as cfg:
        config.write(cfg)
except IOError:
    print("File either doesn't exist or isn't writeable. \n")