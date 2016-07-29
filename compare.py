#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Run through two directories (including sub directories) find files that are the
second directory but not in the first.
"""
import os
import os.path
import hashlib

# Original Directory
FIRST_DIRECTORY = '/home/michael/directory-old-files'
# Directory with new files.
SECOND_DIRECTORY = '/home/michael/directory-new-files'

original_files = set()
new_files = []


# Run through the original directory and creates an md5 sum each of the files.
# md5 is inscure because of known hash colisions, however because we are not
# trying to validate the file's contents so it's good enough, faster and more
# memory efficent than SHA256.
for dirpath, dirnames, filenames in os.walk(ORIGINAL_DIRECTORY):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
        original_files.add(file_hash)


# Run through the new directory and print files who's md5 hash is not in the
# original list of files.
for dirpath, dirnames, filenames in os.walk(NEW_DIRECTORY):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
        if file_hash not in original_files:
            print(file_path)
            new_files.append(file_path)


# Print the list of new files out.
with open('new-files.txt', 'w') as output_file:
    for new_file in new_files:
        output_file.write("%s\n" % new_file)
