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
from .resize import resize


@click.command()
@click.option('--directory', '-D', help='The path of directory of images to crunch.')
@click.option('--file', '-F', help='The path of the image to crunch.')
@click.option('--quality', '-Q', default=80, help='The quality of the .jpg after it is crunched. (default 80)')
@click.option('--height', '-H', help='The pixel height of the image after it is crunched.')
@click.option('--width', '-W', help='The pixel width of the image after it is crunched.')
@click.option('--output', '-O', default='crunched', help='The the directory to place the crunched images in.')
@click.option('--versions', '-V', default=1, help='The number of versions to create for each image.')
def cli(directory, file, quality, height, width, output, versions):
    """
    Image Cruncher

    This is a simple CLI image optimization wrapper for the Python Image
    Library fork Pillow. Image Cruncher takes images and scales them to
    the specified size and quality.
    """
    if not directory and not file:
        click.echo('You must specify either a file or directory.', err=True, color='red')
    if not directory:
        directory = os.getcwd()

    click.echo(directory)


if __name__ == '__main__':
    cli()

__version__ = '0.0.1.dev'
