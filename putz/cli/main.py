"""ckanapi command line interface
Usage:
  putz
  putz --version
Options:
  --version                 show version
"""

import sys
import os
import random
import string
import webbrowser
from docopt import docopt
from pypi_search.search import find_packages

from putz.version import __version__


def parse_arguments():
    return docopt(__doc__, version=__version__)


def main():
    query_string = "".join(random.choice(string.ascii_lowercase) for i in range(2))
    try:
        query_result = find_packages(query_string + "&o=-zscore")
        random_choice = random.choice(query_result)
        pypi_url_result = "https://pypi.org/project/" + random_choice["name"]
        webbrowser.open(pypi_url_result, new=2)
        output_string = pypi_url_result + "\n" + random_choice["description"] + "\n"
        return output_string
    except:
        return "Error querying PyPI."
