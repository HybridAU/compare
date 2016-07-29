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


for dirpath, dirnames, filenames in os.walk(FIRST_DIRECTORY):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        print(full_path)
        print(hashlib.md5(open(full_path, 'rb').read()).hexdigest())
