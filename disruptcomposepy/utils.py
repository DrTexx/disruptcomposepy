import os


def rmdir_recursive(path, removeRoot=True, verbose=True):
    """Adapted from https://gist.github.com/jacobtomlinson/9031697"""

    if not os.path.isdir(path):
        return

    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                rmdir_recursive(fullpath, verbose=verbose)

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0 and removeRoot:
        if verbose is True:
            print("Removing empty folder:", path)
        os.rmdir(path)


def in_directory(filepath, directory):
    """Adapted from https://stackoverflow.com/q/3812849"""

    # make both absolute
    directory = os.path.join(os.path.realpath(directory), "")
    filepath = os.path.realpath(filepath)

    # return true, if the common prefix of both is equal to directory
    # e.g. /a/b/c/d.rst and directory is /a/b, the common prefix is /a/b
    return os.path.commonprefix([filepath, directory]) == directory
