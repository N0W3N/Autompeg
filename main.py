# import all necessarily modules

import os.path
import subprocess
import sys

# choose a file extension the script should scan for and proceed with it

workDir = sys.argv[0]
exttype = sys.argv[1]

# enter the path of the folder which includes the chosen file extension from above
# if the path doesn't exist, it will display an error message

try:

    filesInWorkDir = os.listdir(workDir)  #cache all the existig files in the directory
    for file in filesInWorkDir:
        if str(file).split('.')[-1] == exttype:  #scan for files with the extension given in 'exttype'
            newFile = str(file).split('.' + exttype)[0] + '.mp4' #  replace the extension with a new one
            filepath = workDir + '\\' + file
            newfilepath = workDir + '\\' + newFile

            subprocess.call(['E:\\ffmpeg\\ffmpeg.exe', '-i', filepath, '-c:v', 'copy', '-bsf:a', 'aac_adtstoasc',
                             newfilepath])
except IOError:
    print("Filepath not found.")
