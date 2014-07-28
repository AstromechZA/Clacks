import os
import shelve
import atexit

_CONFIG_FILE = '~/.config/clacks/settings'

def _load_config(read_only=True):
    """
    Load the Clacks settings structure. This creates the directory '~/.clacks'
    if it does not exist.
    """

    # expand user squiggle
    expanded = os.path.expanduser(_CONFIG_FILE)

    # ensure directory
    directory = os.path.dirname(expanded)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(expanded):
        t = shelve.open(expanded)
        t.close()

    file_mode = 'r' if read_only else 'c'

    # open the shelve settings file
    shelf = shelve.open(expanded, flag=file_mode)

    # because we don't keep track of the instance, lets make sure it is closed
    # at the end.
    atexit.register(lambda: shelf.close())

    return shelf

config = _load_config()

