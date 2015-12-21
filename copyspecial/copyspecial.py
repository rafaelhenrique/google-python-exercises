#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import os
import shutil
import shlex
import subprocess

"""Copy Special exercise

"""


def get_special_paths(dir, show_output=True):
    """
    returns a list of the absolute paths of the
    special files in the given directory
    """
    dirpath = os.path.abspath(dir)
    files = os.listdir(dirpath)
    allfiles = []
    for f in files:
        fullfile = "{}/{}".format(dirpath, f)
        if show_output:
            print(fullfile)
        else:
            allfiles.append(fullfile)
    return allfiles


def copy_to(paths, dir):
    """
    given a list of paths, copies those files into the given directory
    """
    if not os.path.exists(dir):
        os.makedirs(dir)

    for path in paths:
        if os.path.isfile(path):
            name = os.path.basename(path)
            shutil.copy2(path, "{}/{}".format(dir, name))


def zip_to(paths, zippath):
    """
    given a list of paths, zip those files up into the given zipfile
    """

    command = "zip -j {} ".format(zippath)
    for path in paths:
        if os.path.isfile(path):
            command += " {} ".format(path)

    args = shlex.split(command)
    print("Command I'm going to do: \n\n{}".format(command))
    print("\nOutput:\n")
    subprocess.Popen(args)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)
    elif len(args) > 0 and not tozip and not todir:
        for arg in args:
            get_special_paths(arg)
    elif todir:
        for arg in args:
            files = get_special_paths(arg, show_output=False)
            copy_to(files, todir)
    elif tozip:
        allfiles = []
        for arg in args:
            allfiles += get_special_paths(arg, show_output=False)
        zip_to(allfiles, tozip)

if __name__ == "__main__":
    main()
