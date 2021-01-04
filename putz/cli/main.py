"""ckanapi command line interface
Usage:
  putz
  putz --version
Options:
  --version                 show version
"""

from docopt import docopt
from putz.version import __version__
from putz.putz import putz


def parse_arguments():
    # docopt is awesome
    return docopt(__doc__, version=__version__)


def main():
    arguments = parse_arguments()
    if arguments["--version"]:
        return __version__
    else:
        return putz()
