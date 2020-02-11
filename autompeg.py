# import all necessarily modules

import os.path
import subprocess
import sys
from configparser import ConfigParser

# working dir and extension types will be passed through CLI

workDir = sys.argv[1]
extType = sys.argv[2]
newExtType = sys.argv[3]

# Config Parser

config = ConfigParser(allow_no_value=True)

try:
    with open('config.ini', 'r') as cfg:
        config.read_file(cfg)
        path = config.get('Path of ffmpeg', 'path')
except IOError:
    print("Couldn't find or open configuration file for ffmpeg. Process is exiting now..")
    sys.exit()

# exception-clause to prevent a faulty WorkDir and therefore the following ffmpeg process

try:
    filesInWorkDir = os.listdir(workDir)  # cache all the existing files in the directory
except IOError:
    print("Filepath not found. Please check the location of your media file(s).\n")
else:
    for file in filesInWorkDir:
        if sys.platform.startswith('win32'):
            newfilename = str(file.split(".") + extType[0] + newExtType)
            slash = "\\"
        elif sys.platform.startswith('darwin'):
            newfilename = str(file.split(extType)[0] + newExtType)
            slash = "//"
            if str(file).split(".")[-1] == extType:  # scan for files with the extension given in 'extType'
                filepath = workDir + slash + file
                newfilepath = workDir + slash + newfilename

                # no need to include an exception-clause here yet, since ffmpeg automatically detects a faulty filepath

                subprocess.run(
                    [

                        path,  # path of ffmpeg
                        "-i",  # input argument for file
                        filepath,  # file path of the 'old' media file
                        "-c:v",  # select video stream
                        "copy",  # copy video stream and don't convert it (to prevent quality loss)
                        "-bsf:a",  # select bitstream filter for the audio stream
                        "aac_adtstoasc",  # remove the ADTS header from the audio stream
                        newfilepath,  # file path of the 'new' media file
                    ]
                )
