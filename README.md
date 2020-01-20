Autompeg - ffmpeg automation script 
==================
Autompeg is an automation script for the multimedia framework **FFmpeg** to convert all files with a specific file format (e.g. TS or OGG) into another file format (e.g. MP4 or MP3).
Since FFmpeg doesn't provide an official way to convert multiple files, Autompeg is able to go through entire folders or even whole disks and convert them by its own.

--------------------------------
When you work on your daily tasks with your favorite application, you'll ask yourself "Why do I need to type the same command over and over again, when there is always just one small change?"
As I already knew Python and also worked my way through "Automate the Boring Stuff with Python", I wanted to apply those learned skills into a real, very first project, that helps me to automate a daily task.

I use FFmpeg to convert and compress a lot of files, they're mostly stored in the same directory for further action. So I want to get rid of typing (or let's say dragging the file into my terminal)
and just enter the file path and which file format should be converted into another one.
 -> PSEUDOCODE: search file path E:/ for file format 'x' if existing convert it to 'y' else skip
 
  
The biggest challenge was to understand how file paths were recognized by Python, FFmpeg and different OS such as Windows or Mac OSX.
Down below, I wrote the known and commong problems, when entering a file path, that couldn't be handled due to slashes/backslashes.

# Installation

1)`git clone https://github.com/N0W3N/Autompeg.git`

or

1) download and unzip the package to your preferred path

2) make sure to have the newest version of FFmpeg installed on your system - otherwise download it from https://ffmpeg.org/download.html

3) run `install.py`

4) enter the file path where ffmpeg is located 
* please keep in my mind that Python handles file paths differently depending on the running OS.
* Windows: e.g. `E:\\ffmpeg\\ffmpeg.exe`
* Mac OSX: e.g. `/Users/ffmpeg/./ffmpeg`
* Linux: e.g. (in work)
--------------------------------
# Usage

`python autompeg.py <WorkDir> <extType> <newExtType>`

* WorkDir = your folderpath with the media
* extType = the file format Autompeg should be looking for
* newExtType = the file format Autompeg should use for its conversion

e.g. `python autompeg.py E:\Streams\ MOV MP4`

e.g  `python autompeg.py E:\Music\ OGG MP3`

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
