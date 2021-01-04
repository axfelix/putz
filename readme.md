## putz

A CLI tool and Python module for putzing around and discovering new Python libraries.

Relies heavily on [pypi-search](https://github.com/asadmoosvi/pypi-search), because PyPI has recently deprecated its main lookup API and retrieving results currently requires screen-scraping 😱!

Currently this (ab)uses PyPI's "Trending" relevance ranking, which is not otherwise exposed or explained, in order to return libraries that are likely to be well-maintained. Right now there is no better way to do a fully serendiptious search of Python packages; results are no doubt somewhat biased by this.

## Installation

```
pip install putz
```

## Usage

Just run `putz`. It'll open a browser window to a randomly-selected, not-abandoned library from PyPI.

## FAQ

### Why did you start this project?

I wanted to ease myself into my first day at the [Recurse Center](https://www.recurse.com/), and I'd never actually shipped a Python CLI library via PyPI before, so I thought I'd figure out how that works!

Also, formatting with [Black](https://github.com/psf/black), because I don't usually organize solo projects very well and wanted the excuse to do that too.

### Why did you give it such a stupid name?

I read the name of the [Python time zone library](https://pypi.org/project/pytz/) too many times and my brain worked its magic.

## License

MIT. Please see [COPYING](COPYING) for full details.