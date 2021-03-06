# Cruncher

Cruncher is a simple but powerful command line tool that optimizes images for the web.

[![Version](https://flat.badgen.net/badge/PyPI/v0.4.0)](https://pypi.org/project/cruncher/)

## Installing

Install and update Cruncher using [pip](https://pip.pypa.io/en/stable/quickstart/).

```commandline
$ pip install cruncher
```

It is highly recommenced that you run Cruncher with [virualenv](https://virtualenv.pypa.io/en/latest/). This can abstract away the peculiarities of running Cruncher across multiple operating systems.

**Cruncher is built for Python 3.** It is tested the last three minor versions of Python (currently 3.6 to 3.8).

## Basic Usage

Cruncher is run from the terminal. Simply specify the image or directory of images you wish to compress, and your preferred settings.

**Example:**
```commandline
$ cruncher -i "C:\path_to_image\the_image.jpg" -q 75 -s 300 500 -o "C:\path_to_output_dir"
```

In this example the following options are used.

`-i` Is the path to the image you wish to compress.

`-q` Is the output image quality.

`-s` Is the output images dimensions (width, height).

`-o` Is the output directory.

Please read the documentation for more details about these options and the others that exist.

## Documentation

[Cruncher Documentation](https://www.danielmorell.com/tools/cruncher/documentation)

1. [Installation](https://www.danielmorell.com/tools/cruncher/documentation/installation)
1. [CLI Options](https://www.danielmorell.com/tools/cruncher/documentation/cli-options)
1. [JSON Configuration](https://www.danielmorell.com/tools/cruncher/documentation/json-configuration)
1. [ICC Profile Conversion](https://www.danielmorell.com/tools/cruncher/documentation/icc-profile-conversion)
1. [Troubleshooting](https://www.danielmorell.com/tools/cruncher/documentation/troubleshooting)

## Contributors

[@danielmorell](https://github.com/danielmorell)

Copyright © 2020 [Daniel Morell](https://www.danielmorell.com/)