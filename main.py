# import all necessarily modules

import os.path
import subprocess
import sys

# working dir and extenstion type will be passed through CLI

workDir = sys.argv[1]
extType = sys.argv[2]
newExtType = sys.argv[3]

# exception-clause to prevent a faulty workdir and ffmpeg process
try:
    filesInWorkDir = os.listdir(workDir)  #cache all the existig files in the directory
except IOError:
    print("Filepath not found. Please check the location of your media file(s).\n")
else:
    for file in filesInWorkDir:
        if str(file).split('.')[-1] == extType:  #scan for files with the extension given in 'exttype'
            newFile = str(file).split('.' + extType)[0] + '.mp4' #  replace the extension with 'newExtType'
            filepath = workDir + '\\' + file
            newfilepath = workDir + '\\' + newFile

            # no need to include an exception-clause here yet, since ffmpeg automatically detects a faulty filepath

            subprocess.call(['E:\\ffmpeg\\ffmpeg.exe', '-i', filepath, '-c:v', 'copy', '-bsf:a', 'aac_adtstoasc',
                             newfilepath])
