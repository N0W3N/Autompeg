""" This tool has the purpose to automatically search for files with a specific file extension in a given folder path and convert them with ffmpeg
into another file format or file extension.
I made this tool because it can be very frustrating to manually convert a lot of files into another file format (e.g. ts -> mp4)
and a hell of waste of time.
I do recommend to start the script via cmd / terminal, because it doesn't show the progress inside your IDE (atleast PyCharm)
It has been successfully tested under Windows 10 with Python 3.7 and the newest ffmpeg version.

# import all necessarily modules

import os
import subprocess

# choose a file extension the script should scan for and proceed with it

exttype = 'ts'

# enter the path of the folder which includes the chosen file extension from above
# if the path doesn't exist, it will display an error message

user_input = input(r'Path of the folder: ')
assert os.path.exists(user_input), 'Folder at, ' + str(user_input) + "does not exist"
workdir = user_input

filesInWorkDir = os.listdir(workdir)  #cache all the existig files in the directory
for file in filesInWorkDir:
    if str(file).split('.')[-1] == exttype:  #scan for files with the extension given in 'exttype'
        newFile = str(file).split('.' + exttype)[0] + '.mp4' #  replace the extension with a new one
        filepath = workdir + '\\' + file
        newfilepath = workdir + '\\' + newFile
        
        """ffmpeg location needs to be changed if you run it from or its stored in another location.
           You can use as many ffmpeg args as you want, just seperate each arg from another arg as a string.
           It's highly recommended to assign filepaths as variables to avoid any errors caused by whitespaces or (back)slashes"""
           
        subprocess.call(['E:\\ffmpeg\\ffmpeg.exe', '-i', filepath, '-c:v', 'copy', '-bsf:a', 'aac_adtstoasc',
                         newfilepath])
                         
