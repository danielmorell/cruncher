"""
:Project: Image Cruncher
:Contents: __init__.py
:copyright: © 2019 Daniel Morell
:license: GPL-3.0, see LICENSE for more details.
:Author: DanielCMorell
:Added v0.0.1.dev -- 9/26/2019
"""
# Standard Library Imports
import os

# Package Imports
import click

# Local Imports
from .core import CrunchHandler, OUTPUT_FILE_FORMATS


@click.command()
@click.option(
    '-I', '--image', 'image',
    type=click.Path(exists=True, readable=True, file_okay=True),
    help='The path of the image to crunch.'
)
@click.option(
    '-D', '--directory', 'directory',
    type=click.Path(exists=True, readable=True, dir_okay=True),
    default=os.getcwd(),
    show_default='current directory',
    help='The path of directory of images to crunch.'
)
@click.option(
    '-O', '--output', 'output',
    type=click.Path(),
    default=None,
    show_default='current directory /crunched',
    help='The the directory to place the crunched images in.'
)
@click.option(
    '-F', '--format', 'file_format',
    type=click.Choice(OUTPUT_FILE_FORMATS, case_sensitive=False),
    default='JPEG',
    show_default=True,
    help='The output image file_format of the final crunched image.'
)
@click.option(
    '-Q', '--quality', 'quality',
    type=click.IntRange(1, 100, clamp=True),
    default=80,
    show_default=True,
    help='The quality of the image after it is crunched. [range: 1 - 100]'
)
@click.option(
    '-S', '--size', 'size',
    type=(int, int),
    default=(None, None),
    help='The pixel width / height of the image after it is crunched. [Format: -S <WIDTH HEIGHT>]'
)
@click.option(
    '-A', '--append', 'append',
    type=str,
    default=None,
    help='Append a string to the filename.'
)
@click.option(
    '--ignore-orientation', 'orientation',
    is_flag=True,
    help='Include this flag to ignore the original image orientation. I.e. if '
         '--size is landscape all portrait images will be cropped as landscape.'
)
@click.option(
    '-M', '--keep-metadata', 'metadata',
    is_flag=True,
    help='Include this flag to keep the image meta/exif. It is removed by default.'
)
@click.option(
    '-V', '--versions', 'nversions',
    default=1,
    show_default=True,
    help='The number of versions to create for each image. If this is set to more '
         'than one you will be prompted to enter --file_format, --quality, --size, '
         '--append, --ignore-orientation, and --keep-metadata.'
)
@click.option(
    '-R', '--recursive', 'recursive',
    is_flag=True,
    help='Get images from sub directories also. Only applicable if --directory '
         'is used.'
)
@click.option(
    '-C', '--config', 'config',
    type=click.Path(),
    default=None,
    help='Specify a JSON file with your settings, this will override all other settings.'
)
def cli(image, directory, output, file_format, quality, size, append, metadata, orientation, nversions, recursive, config):
    """
    Image Cruncher

    This is a simple CLI image optimization wrapper for the Python Image
    Library fork Pillow. Image Cruncher takes images and scales them to
    the specified size and quality.
    """

    # click.echo('Image:        ' + str(image))
    # click.echo('Directory:    ' + str(directory))
    # click.echo('Output:       ' + str(output))
    # click.echo('file_format:  ' + str(file_format))
    # click.echo('Quality:      ' + str(quality))
    # click.echo('Size:         ' + str(size))
    # click.echo('Append:       ' + str(append))
    # click.echo('Metadata:     ' + str(metadata))
    # click.echo('orientation:  ' + str(orientation))
    # click.echo('Num Versions: ' + str(nversions))
    # click.echo('Recursive:    ' + str(recursive))
    click.echo('Config:       ' + str(config))

    image_cruncher = CrunchHandler(image=image, directory=directory, output=output, file_format=file_format,
                                   quality=quality, size=size, append=append, metadata=metadata,
                                   orientation=orientation, nversions=nversions, recursive=recursive,
                                   config=config)

    # click.echo('Mode :        ' + str(image_cruncher.mode))
    # click.echo('Image:        ' + str(image_cruncher.image))
    # click.echo('Directory:    ' + str(image_cruncher.directory))
    # click.echo('Output:       ' + str(image_cruncher.output))
    # click.echo('file_format:  ' + str(image_cruncher.file_format))
    # click.echo('Quality:      ' + str(image_cruncher.quality))
    # click.echo('Size:         ' + str(image_cruncher.size))
    # click.echo('Append:       ' + str(image_cruncher.append))
    # click.echo('Metadata:     ' + str(image_cruncher.metadata))
    # click.echo('orientation:  ' + str(image_cruncher.orientation))
    # click.echo('Num Versions: ' + str(image_cruncher.nversions))
    # click.echo('Recursive:    ' + str(image_cruncher.recursive))
    click.echo('Config:       ' + str(image_cruncher.config))


if __name__ == '__main__':
    cli()

__version__ = '0.0.1.dev'
