Autompeg - ffmpeg automation script 
==================
Autompeg is an automation script for the multimedia framework **FFmpeg** to convert all files with a specific file format (e.g. TS or OGG) into another file format (e.g. MP4 or MP3).
Since FFmpeg doesn't provide an official way to convert multiple files, Autompeg is able to look through entire folders or even whole dictionaries / disks and convert them by its own.

--------------------------------
I made this script to get rid of the typing of the same arguments in FFmpeg again and again - especially when you need to convert hundreds of files.
Also Autompeg helps me to identify and convert files in confusingly dictionaries and disks.

##Installation

1) git clone https://github.com/N0W3N/auto-ffmpeg-ts.git (directory)

or

1) download and unzip the package to your preferred path

2) Make sure to have the newest version of FFmpeg installed on your system - otherwise download it from https://ffmpeg.org/download.html

2) replace line 28 in main.py 
* 'E:\\ffmpeg\\ffmpeg.exe'

with your own ffmpeg path.

##Usage

`python main.py <WorkDir> <extType> <newExtType>`

* WorkDir = your folderpath with the media
* extType = the file format Autompeg should be looking for
* newExtType = the file format Autompeg should use for its conversion

e.g. `python main.py E:\Streams\ MOV MP4`

e.g `python main.py E:\Music\ OGG MP3`

