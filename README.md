# Image Cruncher

Image Cruncher is a simple but powerful command line tool that optimizes images for the web.

## Installing

Install and update Image Cruncher using [pip](https://pip.pypa.io/en/stable/quickstart/).

```
$ pip install <pypi name here>
```

**Image Cruncher is built for Python 3.** It is tested on Python 3.7 and newer.

## Usage


### Options

```
  -i, --image PATH                The path of the image to crunch.
  -d, --directory PATH            The path of directory of images to crunch. [default: (current directory)]
  -o, --output PATH               The the directory to place the crunched images in.
  -f, --format [JPEG|JPEG 2000|WebP|GIF|PNG]
                                  The output image file_format of the final runched image.  [default: JPEG]
  -q, --quality INTEGER RANGE     The quality of the image after it is crunched. [range: 1 - 100]  [default: 80]
  -s, --size <INTEGER INTEGER>    The pixel width / height of the image after it is crunched. [Format: -S <WIDTH HEIGHT>]
  -a, --append TEXT               Append a string to the filename.
  --ignore-orientation            Include this flag to ignore the original image orientation. I.e. if --size is landscape all portrait images will be cropped as landscape.
  -m, --keep-metadata             Include this flag to keep the image meta/exif. It is removed by default.
  -c, --versions INTEGER          The number of versions to create for each image. If this is set to more than one you will be prompted to enter --file_format, --quality, --size, --append, --ignore-orientation, and --keep-metadata.  [default: 1]
  -r, --recursive                 Get images from sub directories also. Only applicable if --directory is used.
  -c, --config PATH               Specify a JSON file with your settings, this will override all other settings.
  --help                          Show the help message and exit.
```

## Troubleshooting

#### Path does not exist

```
$ image_cruncher -F C:\Projects\Image Dir\image.png -S 1000 600

Error: Invalid value for "-F" / "--file": Path "C:\Projects\Image" does not exist.
```

This error is cause because there is a blank space in the path to correct this wrap the path in double quotes.

```
$ image_cruncher -F "C:\Projects\Image Dir\image.png" -S 1000 600
```

This applies to `--directory`, `--file`, and `--output` options.

## Contributors

[@danmorell](https://github.com/danmorell)

Copyright © 2019 Daniel Morell