"""
core.py

Project: Project Files
Contents: core.py
Author: DanielCMorell
Added v0.0.1.dev -- 9/27/2019
"""
# Standard Library Imports
import os

# Package Imports
import click

# Local Imports


class ImageCruncher:

    def __init__(self, image, directory, output, format, quality, size,
                 append,  metadata, orientation, versions, config):
        self.image = image
        self.directory = directory
        self.output = output
        self.format = format
        self.quality = quality
        self.size = size
        self.append = append
        self.metadata = metadata
        self.orientation = orientation
        self.versions = versions
        self.config = config

        click.echo('Init')

        if directory != os.getcwd():
            click.echo('Custom Dir')

        if output is None:
            self.output = os.path.join(directory, 'crunched')

        if not os.path.isdir(self.output):
            click.echo('-- New Output Dir')
            os.makedirs(self.output)
        else:
            click.echo('-- Output Dir Exists')
