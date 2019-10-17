Autompeg - ffmpeg automation script 
==================
Autompeg is an automation script for the multimedia framework **FFmpeg** to convert all files with a specific file format (e.g. TS or OGG) into another file format (e.g. MP4 or MP3).
Since FFmpeg doesn't provide an official way to convert multiple files, Autompeg is able to look through entire folders or even whole dictionaries / disks and convert them by its own.

--------------------------------
I made this script to get rid of the typing of the same arguments in FFmpeg again and again - especially when you need to convert hundreds of files.
Also Autompeg helps me to identify and convert files in confusingly dictionaries and disks.
--------------------------------
# Installation

1) git clone https://github.com/N0W3N/auto-ffmpeg-ts.git (directory)

or

1) download and unzip the package to your preferred path

2) Make sure to have the newest version of FFmpeg installed on your system - otherwise download it from https://ffmpeg.org/download.html

2) replace line 28 in main.py 
* 'E:\\ffmpeg\\ffmpeg.exe'
with your own ffmpeg path.
--------------------------------
# Usage

`python main.py <WorkDir> <extType> <newExtType>`

* WorkDir = your folderpath with the media
* extType = the file format Autompeg should be looking for
* newExtType = the file format Autompeg should use for its conversion

e.g. `python main.py E:\Streams\ MOV MP4`

e.g  `python main.py E:\Music\ OGG MP3`

* subprocess.call() takes all the arguments you'd type in your terminal/cmd to start ffmpeg

* the example subprocess converts a transport stream (TS) without quality-loss (-c:v) (copy) to MP4 and also removes faulty audio streams (-bsf:a) (aac_adtstoasc).
--------------------------------
# Known bugs/issues

Autompeg is very harsh when it comes to file path and structures.
Make sure and double check the file path of your folders and (most importantly) ffmpeg.

* (Windows) Autompeg couldn't find any files in `'E:/Media'` but was able to proceed with `'E:\Media'`
* (Windows) Autompeg couldn't start FFmpeg when the location was set to `E:\FFmpeg\ffmpeg.exe` and/or `E:/FFmpeg/ffmpeg.exe`
* (All) terminal/cmd isn't able to use the given argument if you haven't separate them correctly. subprocess needs all arguments within a new separated string, it can't handle a single string with all arguments
* (All) In rare cases FFmpeg couldn't start at all, when an old version is installed/used
--------------------------------