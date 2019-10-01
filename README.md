# Image Cruncher

Image Cruncher is a simple but powerful command line tool that optimizes images for the web.

## Installing

Install and update Image Cruncher using [pip](https://pip.pypa.io/en/stable/quickstart/).

```
$ pip install <pypi name here>
```

**Image Cruncher is built for Python 3.** It is tested on Python 3.6 and newer.

## Usage

### CLI Options

### `-i` and `--image`
 
**Input:** _Path_

**Default** `None`

The absolute path to the image to be crunched.

**Example:**
```commandline
$ image_cruncher -i "C:\path_to_image\the_image.jpg"
```

### `-d` and `--directory`
 
**Input:** _Path_

**Default** _Current working directory_

The absolute path to the directory of images to be crunched.

**Example:**
```commandline
$ image_cruncher -d "C:\path_to_images_dir"
```

### `-o` and `--output`
 
**Input:** _Path_

**Default** _Current working directory`/crunched`_

The absolute path to the directory where crunched images will be placed.

**Example:**
```commandline
$ image_cruncher -o "C:\path_to_output_dir"
```

### `-f` and `--format`
 
**Input:** _String_

**Default** `JPEG`

The output image format of the final crunched image. Options are `GIF`, `JPEG`, `JPEG 2000`, `PNG`, and `WebP`.

**Example:**
```commandline
$ image_cruncher -f PNG
```

### `-q` and `--quality`
 
**Input:** _Integer_

**Default** `80`

The quality of the image after it is crunched. May be any integer between `1` and `100`.

**Example:**
```commandline
$ image_cruncher -q 75
```

### `-s` and `--size`
 
**Input:** _Integer Integer_

**Default** `None None`

The pixel `width height` of the image after it is crunched. This should be two integers with a space between. If none is set, the original image size is used.

**Example:**
```commandline
$ image_cruncher -s 300 200
```

### `-a` and `--append`
 
**Input:** _String_

**Default** `None`

Append a string to the image filename.

**Example:**
```commandline
$ image_cruncher -a "_thumbnail"
```

### `--ignore-orientation`
 
**Input:** _None_

**Default** `False`

Include this flag to ignore the original image orientation. I.e. if `--size` is landscape all portrait images will be cropped as landscape.

**Example:**
```commandline
$ image_cruncher --ignore-orientation
```

### `-m` and `--keep-metadata`
 
**Input:** _None_

**Default** `False`

Include this flag to keep the image meta/exif. Metadata is removed by default.

**Example:**
```commandline
$ image_cruncher -m
```

### `-v` and `--versions`
 
**Input:** _Integer_

**Default** `1`

The number of versions to create for each image. If this is set to more than `1` you will be prompted to enter `--format`, `--quality`, `--size`, `--append`, `--ignore-orientation`, and `--keep-metadata` for each version.

**Example:**
```commandline
$ image_cruncher -v 2
Please enter the needed information for each version.
Version 1
Size WIDTH HEIGHT: 200 200
File format: JPEG
Quality: 75
Append filename: _thumbnail
Ignore orientation: False
Keep metadata: False
Version 2
Size WIDTH HEIGHT: 600 400
File format: JPEG
Quality: 75
Append filename: _small
Ignore orientation: True
Keep metadata: False
```

### `-r` and `--recursive`
 
**Input:** _None_

**Default** `False`

Get images from sub directories also. Only applicable if `--directory` is used.

**Warning:** If you use recursive mode multiple times on the same directory make sure your `--output` directory is not a subdirectory or you will crunch the images you already crunched.

**Example:**
```commandline
$ image_cruncher -r
```

### `-c` and `--config`
 
**Input:** _Path_

**Default** `None`

Specify the absolute path to a JSON file with your settings. JSON configs will override command line configs if set.

**Example:**
```commandline
$ image_cruncher -c "C:\path_to_config_file\config.json"
```

### `--help`

Show the help message and exit.

**Example:**
```commandline
$ image_cruncher -help
```

### JSON Config Options

You can simplify complex multi-version crunches by creating a JSON config file.

Any settings in the config file will override the same setting if it was provided via command line arguments.

For example, if the following command pointed to the example config file below, The image `directory` would be `C:\path_to_images_dir\images`.

```commandline
$ image_cruncher -d "C:\other_image_dir\" -c "C:\path_to_config\config.json"
```

```json
{
    "image": "",
    "directory": "C:\\path_to_images_dir\\images",
    "output": "C:\\path_to_images_dir\\images\\crunched",
    "recursive": true,
    "versions": [
        {
            "file_format": "JPEG",
            "quality": 70,
            "width": 200,
            "height": 200,
            "append": "thumb",
            "keep_orientation": false,
            "keep_metadata": false
        },
        {
            "file_format": "JPEG",
            "quality": 70,
            "width": 600,
            "height": 400,
            "append": "full",
            "keep_orientation": false,
            "keep_metadata": false
        }
    ]
}
```

**Note:** Be sure to escape the slashes in the paths in your JSON config file.

## Troubleshooting

#### Path does not exist

```
$ image_cruncher -i C:\Projects\Image Dir\image.png -S 1000 600

Error: Invalid value for "-i" / "--file": Path "C:\Projects\Image" does not exist.
```

This error is cause because there is a blank space in the path to correct this wrap the path in double quotes.

```
$ image_cruncher -i "C:\Projects\Image Dir\image.png" -S 1000 600
```

This applies to `--directory`, `--image`, `--output`, and `--config` options.

## Contributors

[@danmorell](https://github.com/danmorell)

Copyright © 2019 Daniel Morell