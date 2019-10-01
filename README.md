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

Option         | Argument            | Information | Default
---------------|---------------------|-------------|--------
Image path         | `-i`, `--image`         | The absolute path to the image to be crunched. | None
Directory path     | `-d`, `--directory`     | The absolute path to the directory of images to be crunched. | The current working directory
Output path        | `-o`, `--output`        | The absolute path to the directory where crunched images will be placed. | The current working directory `/crunched`
Format             | `-f`, `--format`        | The output image format of the final crunched image. Options are `GIF`, `JPEG`, `JPEG 2000`, `PNG`, and `WebP`.  | `JPEG`
Quality            | `-q`, `--quality`       | The quality of the image after it is crunched. May be any integer between `1` and `100`. | `80`
Size               | `-s`, `--size`          | The pixel `width height` of the image after it is crunched. This should be two integers with a space between. If none is set, the original image size is used. | None
Append Filename    | `-a`, `--append`        | Append a string to the image filename. | None
Ignore Orientation | `--ignore-orientation`  | Include this flag to ignore the original image orientation. I.e. if `--size` is landscape all portrait images will be cropped as landscape. | `False`
Keep Metadata      | `-m`, `--keep-metadata` | Include this flag to keep the image meta/exif. | Metadata is removed by default.
Number of Versions | `-v`, `--versions`      | The number of versions to create for each image. If this is set to more than `1` you will be prompted to enter `--format`, `--quality`, `--size`, `--append`, `--ignore-orientation`, and `--keep-metadata` for each version. | `1`
Recursive Mode     | `-r`, `--recursive`     | Get images from sub directories also. Only applicable if `--directory` is used. | `False`
Config File        | `-c`, `--config`        | Specify the absolute path to a JSON file with your settings. JSON configs will override command line configs if set. | None
Help               | `--help`                | Show the help message and exit. |

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