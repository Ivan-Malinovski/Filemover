import os
import shutil

def movefile():
    # TODO - option to list files
    print('\nFilemover automatically moves or copies all files and folders that contain your search word. By default it uses its own directory.\n')

    foldername = input('Name for new folder: ')
    search = input('Word in file name: ').lower()
    wish = input('[c]opy or [m]ove? ').lower()
    os.mkdir(foldername) # os.mkdir creates directory
    print('\nCreated folder ' + foldername + ', looking for files that contain ' + search + '...\n')

    count = len(os.listdir())-1 # counts how many files are in current directory
    found = 0
    while 0 < count: # loops as many times as there are files in current directory
        filename = os.listdir()[count] # finds filename

        if search in os.listdir()[count].lower(): # if users search word is anywhere in the filename ...
            if wish == 'move' or wish == 'm':
                shutil.move(filename, foldername) # move found file to
                print('moving ' + filename + ' to ' + foldername)
            elif wish == 'copy' or wish == 'c':
                shutil.copy(filename, foldername)  # kopier filen til brugerens nye mappe
                print('copying ' + filename + ' to ' + foldername)

            found = 1
            count = count - 1
        else:
            count = count - 1
    if found == 0: 
        print('No files found, deleting folder')
        os.rmdir(foldername) # delete user folder
    else:
        print('\nCompleted. Moved or copied ' + str(found+1) + ' file(s).')
    end = input('\nYou can now close the window')

movefile()