#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
A small python script to find new files in two similar directories.
"""

import os
import os.path
import hashlib
import argparse


def setup_options():
    """
    Parse options and get the location of the old and the new directory.
    """
    parser = argparse.ArgumentParser(
        description=('Run through two directories (including sub directories) '
                     'and find files that are the new directory but not in '
                     'the old directory.'))
    parser.add_argument(
        'old_files',
        metavar='old_directory',
        type=str,
        help='The old directory with the original files')
    parser.add_argument(
        'new_files',
        metavar='new_directory',
        type=str,
        help='The new directory with both original files and new ones.')
    parser.add_argument(
        '--output',
        '-o',
        metavar='Output file',
        type=str,
        help='Output the list to a file.')
    parser.add_argument(
        '--silent',
        '-s',
        action='store_true',
        help='Do not print a list of new files to the terminal.')

    return parser.parse_args()


def compare_two_directories(settings):
    """
    Run through two directories (including sub directories) and find files that
    are in the new directory but not in the old directory.
    """
    original_files = set()
    new_files = []

    # Run through the original directory and creates an MD5 sum each of the
    # files. MD5 is inscure because of known hash collisions, however we are
    # not trying to validate the file's contents so it's good enough, faster
    # and more memory efficent than SHA256.
    for dirpath, dirnames, filenames in os.walk(settings.old_files):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            original_files.add(file_hash)

    # Run through the new directory and print files who's md5 hash is not in
    # the original list of files.
    for dirpath, dirnames, filenames in os.walk(settings.new_files):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            if file_hash not in original_files:
                if not settings.silent:
                    print(file_path)
                new_files.append(file_path)

    # Print the list of new files out.
    if settings.output:
        with open(settings.output, 'w') as output_file:
            for new_file in new_files:
                output_file.write("%s\n" % new_file)


if __name__ == "__main__":
    compare_two_directories(setup_options())
