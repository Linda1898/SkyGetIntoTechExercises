
# QUESTION FOR MARTINA: DO WE SAVE FILES IN SCRIPT SECTION?
# Get the directory name
# Construct a portable wildcard pattern
# TODO: Use the glob.glob() function to obtain the list of filenames
# TODO: use os.path.getsize to find each file's size
# TODO: Add a test to only display files that are not zero length
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

import sys, glob, os
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

pattern = os.path.join(hdir,'*')
Filenames= glob.glob(pattern)
print("Here is a list of files within the homepath that are more than 0 bites: ")
for name in range(len(Filenames)):
    Filesize = os.path.getsize(Filenames[name])
    if Filesize > 0:
        print(os.path.basename(Filenames[name])," is ", Filesize, "bites")
    else:
        continue
