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
from .core import ImageCruncher
from .resize import resize


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
    '-F', '--format', 'format',
    type=click.Choice(['jpg', 'webp', 'gif', 'png'], case_sensitive=False),
    default='jpg',
    show_default=True,
    help='The output image format of the final crunched image.'
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
    '-V', '--versions', 'versions',
    default=1,
    show_default=True,
    help='The number of versions to create for each image. If this is set to more '
         'than one you will be prompted to enter --format, --quality, --size, '
         '--append, --ignore-orientation, and --keep-metadata.'
)
@click.option(
    '-C', '--config', 'config',
    type=click.Path(),
    default=None,
    help='Specify a JSON file with your settings, this will override all other settings.'
)
def cli(image, directory, output, format, quality, size, append, metadata, orientation, versions, config):
    """
    Image Cruncher

    This is a simple CLI image optimization wrapper for the Python Image
    Library fork Pillow. Image Cruncher takes images and scales them to
    the specified size and quality.
    """

    click.echo('Image:       ' + str(image))
    click.echo('Directory:   ' + str(directory))
    click.echo('Output:      ' + str(output))
    click.echo('format:      ' + str(format))
    click.echo('Quality:     ' + str(quality))
    click.echo('Size:        ' + str(size))
    click.echo('Append:      ' + str(append))
    click.echo('Metadata:    ' + str(metadata))
    click.echo('orientation: ' + str(orientation))
    click.echo('Versions:    ' + str(versions))
    click.echo('Config:      ' + str(config))

    image_cruncher = ImageCruncher(image=image, directory=directory, output=output, format=format,
                                   quality=quality, size=size, append=append, metadata=metadata,
                                   orientation=orientation, versions=versions, config=config)

    click.echo('Image:       ' + str(image_cruncher.image))
    click.echo('Directory:   ' + str(image_cruncher.directory))
    click.echo('Output:      ' + str(image_cruncher.output))
    click.echo('format:      ' + str(image_cruncher.format))
    click.echo('Quality:     ' + str(image_cruncher.quality))
    click.echo('Size:        ' + str(image_cruncher.size))
    click.echo('Append:      ' + str(image_cruncher.append))
    click.echo('Metadata:    ' + str(image_cruncher.metadata))
    click.echo('orientation: ' + str(image_cruncher.orientation))
    click.echo('Versions:    ' + str(image_cruncher.versions))
    click.echo('Config:      ' + str(image_cruncher.config))


if __name__ == '__main__':
    cli()

__version__ = '0.0.1.dev'
