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

list_of_files = set()
new_files = []

for dirpath, dirnames, filenames in os.walk(FIRST_DIRECTORY):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
        list_of_files.add(file_hash)

for dirpath, dirnames, filenames in os.walk(SECOND_DIRECTORY):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
        if file_hash not in list_of_files:
            print(file_path)
            new_files.append(file_path)
