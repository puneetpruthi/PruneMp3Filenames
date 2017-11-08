# PruneMp3Filenames

#!/usr/bin/env python
import os
import re
import sys

# This is a script to remove garbage words/characters from names of file
# intended to be used for songs.pk or other downloaded songs.
#
# Usage:
#
# To just view new names of files after renaming (NOT ACTUALLY RENAME)
#	./<name> <Folder> n
#
# To ACTUALLY RENAME the files as well as see the new names
#	./<name> <Folder> y
#

def rename(path, flag):
    for file in os.listdir(path):
        fname = os.path.join(path, file)
        #if os.path.isdir(fname):
        #    rename(fname)
        renamefile(path, file, flag)

def renamefile(path, file, flag):
    #Specific substrings to replace with '*'
    newname = re.sub('\(Songs.PK\)', '*', file)
    newname = re.sub('\[Songs.PK\]', '*', newname)
    newname = re.sub('\(SongsPK.info\)', '*', newname)
    newname = re.sub('\[SongsPK.info\]', '*', newname)
    newname = re.sub('Mohenjo Mohenjo', '*', newname)
    newname = re.sub('\[Songspk.LIVE\]', '*', newname)
    newname = re.sub('\(Muskurahat.Com\)', '*', newname)
    newname = re.sub('\[Bollym4u.com\]', '*', newname)
    newname = re.sub('\[www.DJMaza.Com\]', '*', newname)
    newname = re.sub('\[Songspk.LINK\]', '*', newname)
    newname = re.sub('\[Songspk.SITE\]', '*', newname)
    newname = re.sub('\[Songspk.GURU\]', '*', newname)
    newname = re.sub('kbps', '*', newname)
    newname = re.sub('Kbps', '*', newname)
    newname = re.sub('Fmw11.com', '*', newname)
    newname = re.sub('apnaymp3.com', '*', newname)
    newname = re.sub('mp3', 'ooooo', newname)

    # Remove special characters that come often
    newname = re.sub('[^a-zA-Z._-]+', '_', newname)
    #newname = re.sub('[a-zA-Z -]+ -', '', newname)
    newname = re.sub('_-_', '-', newname)
    newname = re.sub('[_-]{2,}', '_', newname)
    newname = re.sub('[_-]+$', '', newname)
    newname = re.sub('^[_-]+', '', newname)
    newname = re.sub('_', ' ', newname)
    newname = re.sub('-', ' ', newname)
    newname = re.sub('ooooo', 'mp3', newname)
    newname = re.sub(' \.', '.', newname)
    newname = re.sub('\.\.', '.', newname)

    if newname != file:
        print os.path.join(path, file), os.path.join(path, newname)
        #os.rename(os.path.join(path, file), os.path.join(path, newname))
	if flag == 'y':
            os.rename(os.path.join(path, file), os.path.join(path, newname))


if __name__ == '__main__':
    rename(sys.argv[1], sys.argv[2])
