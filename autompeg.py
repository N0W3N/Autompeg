# import all necessarily modules

import os.path
import subprocess
import sys

# working dir and extension types will be passed through CLI

workDir = sys.argv[1]
extType = sys.argv[2]
newExtType = sys.argv[3]

# exception-clause to prevent a faulty WorkDir and ffmpeg process

try:
    filesInWorkDir = os.listdir(workDir)  # cache all the existing files in the directory
except IOError:
    print("Filepath not found. Please check the location of your media file(s).\n")
else:
    for file in filesInWorkDir:
        if str(file).split(".")[-1] == extType:  # scan for files with the extension given in 'extType'
            newFile = str(file).split("." + extType)[0] + newExtType  # replace the extension with 'newExtType'
            filepath = workDir + "\\" + file
            newfilepath = workDir + "\\" + newFile

            # no need to include an exception-clause here yet, since ffmpeg automatically detects a faulty filepath

            subprocess.call(
                [
                    "E:\\ffmpeg\\ffmpeg.exe", # path of ffmpeg
                    "-i", # input argument for file
                    filepath, # file path of the 'old' media file
                    "-c:v", # select video stream
                    "copy", # copy video stream and don't convert it (to prevent quality loss)
                    "-bsf:a", # select bitstream filter for the audio stream
                    "aac_adtstoasc", # remove the ADTS header from the audio stream
                    newfilepath, # file path of the 'new' media file
                ]
            )
