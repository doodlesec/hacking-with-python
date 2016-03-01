from os import rename, listdir, path
import sys

def renameFilesRec(fullpath):
    #~ Listing all the contents(files/directories) in the specified path ~#
    items = listdir(fullpath)

    #~ Looping through each item ~#
    for item in items:
        directory = path.join(fullpath, item)
        if path.isdir(directory):
            print "DIRECTORY: ", directory
            for File in listdir(directory):
                if str.isalpha(File[0:1]) and File.rfind('.mp4')>=0:
                    part1 = File[0:File.rfind('-')]
                    part2 = File[File.rfind('-')+1:File.rfind('.')]
                    newName = File.replace(File, part2+'-'+part1+'.mp4')
                    print newName
                    rename(path.join(fullpath, File), path.join(fullpath, newName))

        else:
            if str.isalpha(item[0:1]) and item.rfind('.mp4')>=0:
                newName = item[item.rfind('-') + 1 : item.find('.')] + '-' + item[ : item.rfind('-')] + item[item.find('.'):]

                print newName
                rename(path.join(fullpath, item), path.join(fullpath, newName))  


try:
    renameFilesRec(sys.argv[1])
except OSError:
    print 'Invalid path.'       


