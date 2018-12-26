import os
import shutil
import re
import traceback

def start():
    print('\nFilemover moves or copies all files and folders that contain your search word.\n')

    workdir = input('Choose work directory: ')
    if workdir == '':
        workdir = os.getcwd()
    os.chdir(workdir) # puts user input as work directory
    print('Set work directory to ' + workdir)

    foldername = input('Name for new folder: ')
    usersearch = input('Word in file name (if blank, it lists everything): ')
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
        print(*showfiles, sep = '\n') # shows list of files, but separated by linebreak
        cont = input('\nPress enter to accept and continue or close window to cancel\n')
        os.mkdir(foldername)  # os.mkdir creates directory

def movefiles(foldername, showfiles, wish):
    count = 0

    if wish == 'move' or wish == 'm':
        fn  = shutil.move
        action = 'Moving'
    else:
        fn = shutil.copy
        action = 'Copying'

    while count < len(showfiles): # loop that moves files
        filename = showfiles[count]

        try:
            if count == 0:
                print(action + ' following files to ' + foldername + ':')
            fn(filename, foldername)  # copy found file to new folder
            count += 1
            print(filename)

        except PermissionError:
            end = input('An error has occurred: A file is being used by another process. Type \'error\' to see the full error message. \nSome files might still have been or moved. Press enter to restart.')
            if end.lower() == 'error':
                print(traceback.format_exc())
            start()

        except:
            print('An error has occurred: ' + traceback.format_exc())
            input('Press enter to try again')
            start()

    if wish == 'move' or wish == 'm':
        print('\nCompleted. Moved ' + str(count) + ' file(s).')

    else:
        print('\nCompleted. Copied ' + str(count) + ' file(s).')
    end = input('\nClose window to exit or press enter to restart Filemover')
    start()

start()