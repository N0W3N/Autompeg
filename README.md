Autompeg - ffmpeg automation script 
==================
**Autompeg** is an automation script for the multimedia framework **FFmpeg**.  
FFmpeg has several nice features especially in terms of converting files or processing/dumping streams from the internet.  
Most of my time, I use FFmpeg to convert files with a specific file format into another file format (e.g. from .ts to .mp4 | from .wav to .mp3).
Unfortunately, FFmpeg doesn't provide an official way to convert multiple files stored in a folder on a disk in a single process, which makes it
incredibly annoying and timewasting, to write and enter the same command over and over again.

When entering a valid working directory, Autompeg scans the directory recursively (folder by folder, file by file) for the file extension and converting
it with FFmpeg in the background.
Autompeg is a simple extension to the framework and saved me an insane amount of time in the past.

--------------------------------
# Thoughts behind this project

When you work on your daily tasks with your favorite application, you'll ask yourself 
"Why do I need to type the same command over and over again, when there is always just one small change?"
As I already knew Python and also worked my way through "Automate the Boring Stuff with Python", 
I wanted to apply those learned skills into a real, very first project, that helps me to automate a daily task.

I use FFmpeg to convert and compress and convert a lot of files, they're mostly stored in the same directory for further action. 
So I want to get rid of typing (or let's say dragging the file into my terminal)
and just enter the file path and which file format should be converted into another one.

 -> PSEUDOCODE: 
 search file path E:/ for file format 'x'  
    if existing convert it to 'y'  
    else skip  
 
  
The biggest challenge was to understand how file paths were recognized by Python, FFmpeg and different OS such as Windows or Mac OSX.

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

Since the script already contains an example conversation usage, I highly recommend to change the commands given in subprocess.run() (`autompeg.py`)
into another commands by your own choice.

`python3 autompeg.py <WorkDir> <extType> <newExtType>`

* WorkDir = your folderpath with the media
* extType = the file format Autompeg should be looking for
* newExtType = the file format Autompeg should use for its conversion

**Windows**

e.g. `python3 autompeg.py E:\\Streams\ .MOV .MP4`

e.g  `python3 autompeg.py E:\\Music\\ OGG MP3`

**Mac**

e.g. `python3 autompeg.py /Volumes/Storage MOV MP4`

e.g. `python3 autompeg.py /Users/Test/Queue OGG MP3`

* subprocess.run() works in the same way as your terminal does, with the only exception that it separates each command with a comma. 

* the example subprocess in the code converts a transport stream (TS) without quality-loss (-c:v) (copy) to MP4 and also removes faulty audio streams (-bsf:a) (aac_adtstoasc).

* Don't worry if you use the wrong slash syntax on Windows. Autompeg automatically replaces it with the correct slash-syntax.
--------------------------------
# Known bugs/issues

As stated previously, file paths are handled very differently and are still a bit of an issue.  
Please make sure to enter all paths correctly depending on your OS, otherwise Autompeg could have problems to even start at all.

Down below all bugs/issues which are currently known and will probably be fixed in the future.

* (All) terminal/cmd isn't able to use the given argument if you haven't separate them correctly. subprocess needs all arguments within a new separated string/variable, it can't handle a single string with all arguments
* (All) In rare cases FFmpeg couldn't start at all, when an old version is installed/used
--------------------------------
