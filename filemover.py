import os
import shutil
import re

def start():
    print('\nFilemover moves or copies all files and folders that contain your search word.\n')

    workdir = input('Choose work directory: ')
    if workdir == '':
        workdir = os.getcwd()
    os.chdir(workdir) # puts user input as work directory
    print('Set work directory to ' + workdir)

    foldername = input('Name for new folder: ')
    usersearch = input('Word in file name: ')
    search = re.compile(usersearch, re.I) # converts to regex, ignores case
    wish = input('[c]opy or [m]ove? (copies by default) ').lower()

    print('\nLooking for files that contain ' + usersearch + '...\n')

    showfiles = list(filter(search.search, os.listdir())) # list with found files

    listfiles(showfiles, foldername)
    movefiles(foldername, showfiles, wish)

def listfiles(showfiles, foldername):
    if len(showfiles) == 0:
        end = input('Couldn\'t find any files containing your searchphrase.\nPress enter to exit, press any key to retry')
        if end == '':
            exit()
        else:
            start()
    else:
        print('Files found, creating folder ' + foldername + '\nFound the following ' + str(len(showfiles)) + ' file(s):')
        print(*showfiles, sep = '\n') # shows list of files, but separated
        cont = input('\nPress enter to accept and continue or close window to cancel\n')
        os.mkdir(foldername)  # os.mkdir creates directory

def movefiles(foldername, showfiles, wish):
        count = 0
        while count < len(showfiles): # loop that moves files.
            filename = showfiles[count]

            if wish == 'move' or wish == 'm':
                if count == 0:
                    print('Moving following files to ' + foldername + ':')
                shutil.move(filename, foldername)  # copy found file to new folder
                count += 1
                print(filename)

            else:
                if count == 0:
                    print('Copying following files to ' + foldername + ':')
                shutil.copy(filename, foldername)  # copy found file to new folder
                count += 1
                print(filename)
        if wish == 'move' or wish == 'm':
            print('\nCompleted. Moved ' + str(count) + ' file(s).')
        else:
            print('\nCompleted. Copied ' + str(count) + ' file(s).')
        end = input('\nClose window to exit or \'enter\' to restart Filemover')
        start()

start()