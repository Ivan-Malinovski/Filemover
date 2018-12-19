# Filemover
It moves and copies files. I primarily made this because I wanted a quick way to put a bunch of stuff in folders.
It supports regex, so you can search ``` example*.*mkv ``` and it'll find all mkv files with the word example in the file. So if you want to put all your completely legal Game of Thrones episodes in a folder, can just search ``` game*.*thrones*.*mkv ```, and it'll find every mkv file with those words.

Usage:
Put Filemover.exe somewhere and run it.

It'll ask you for work directory; it's the directory where all your files are.

Folder name is the new folder, where your files go. 

Before it moves anything, it'll list the files it's about to move, so you have a chance to confirm.


The Romeo and Juliet files are just meant for testing.


Current limitations (and things to be fixed):
It's not good at handling errors. For example, if a program like uTorrent locks a file, Filemover will just quit. This is also why Filemover defaults to copying, if no option is chosen.
