import sys

from . import dahuacam
from . import discover
from . import grabber


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'discover':
            sys.argv.pop(1)
            discover.cmdline_run()
        elif sys.argv[1] == 'configure':
            sys.argv.pop(1)
            dahuacam.cmdline_run()
        else:
            grabber.cmdline_run()
    else:
        grabber.cmdline_run()
