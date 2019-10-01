"""
:Project: Image Cruncher
:Contents: core.py
:copyright: © 2019 Daniel Morell
:license: GPL-3.0, see LICENSE for more details.
:Author: DanielCMorell
:Added v0.0.1.dev -- 9/26/2019
"""
# Standard Library Imports
import os
import json

# Package Imports
import click

# Local Imports
from .cruncher import GIFCruncher, JPEGCruncher, JPEG2000Cruncher, PNGCruncher, WebPCruncher

SUPPORTED_FILES_EXTENSIONS = ['bmp', 'dib', 'jpg', 'jpeg', 'gif', 'tif', 'webp', 'png', 'ico', 'j2p', 'jpx']
OUTPUT_FILE_FORMATS = ['JPEG', 'JPEG 2000', 'WebP', 'GIF', 'PNG']


class CrunchHandler:

    def __init__(self, image, directory, output, file_format, quality, size,
                 append, metadata, orientation, nversions, recursive, config):
        self.image = image
        self.directory = directory
        self.output = output
        self.file_format = file_format
        self.quality = quality
        self.size = size
        self.append = append
        self.metadata = metadata
        self.orientation = orientation
        self.nversions = nversions
        self.recursive = recursive
        self.versions = []
        self.images = []
        self.config = config

        click.echo('Init')

        if directory != os.getcwd():
            click.echo('Custom Dir')

        self.mode = self.check_mode()

        self.get_output_dir(output, directory)
        self.generate_versions()
        self.get_images()

        self.ncruches = self.get_num_crunches()

    def get_output_dir(self, output, directory):
        if output is None:
            self.output = os.path.join(directory, 'crunched')

        if not os.path.isdir(self.output):
            click.echo('-- New Output Dir')
            os.makedirs(self.output)
        else:
            click.echo('-- Output Dir Exists')

    def generate_versions(self):
        if self.nversions > 1 and self.config is None:
            click.echo('Please enter the needed information for each version.')
            i = 1
            while i <= self.nversions:
                click.echo(f'Version {i}'),
                size = self.parse_size(click.prompt(f'Size WIDTH HEIGHT', type=str))
                self.versions.append({
                    'version': i,
                    'file_format': click.prompt(f'File format', type=click.Choice(OUTPUT_FILE_FORMATS),
                                                show_choices=False),
                    'width': size[0],
                    'height': size[1],
                    'quality': click.prompt(f'Quality',  type=click.IntRange(1, 100, clamp=True), default=80),
                    'append': click.prompt(f'Append filename',  type=str, default='', show_default=False),
                    'orientation': click.prompt(f'Ignore orientation', type=bool, default=False),
                    'metadata': click.prompt(f'Keep Metadata', type=bool, default=False),
                })
                i += 1

        elif self.config:
            with open(self.config) as json_config:
                configs = json.load(json_config)
                self.parse_json_configs(configs)

        else:
            self.versions.append({
                'version': 1,
                'file_format': self.file_format,
                'width': self.parse_size(self.size)[0],
                'height': self.parse_size(self.size)[1],
                'quality': self.quality,
                'append': self.append,
                'orientation': self.orientation,
                'metadata': self.metadata
            })

    def get_images(self):
        if self.mode == 'img':
            self.images = [self.image]
        elif self.recursive:
            self.images = [image for image in self.scan_directory()]
        else:
            for file in os.scandir(self.directory):
                if file.is_file(follow_symlinks=False) and file.name.split('.')[-1] in SUPPORTED_FILES_EXTENSIONS:
                    self.images.append(file.path)

        # click.echo(self.images)

    def scan_directory(self, path=None):
        """
        Finds all supported images in the given directory. If in recursive mode
        subdirectories are also checked.

        :param path: The path of the directory to scan.
        :return:
        """
        if not path:
            path = self.directory
        for node in os.scandir(path):
            if self.recursive and node.is_dir(follow_symlinks=False):
                yield from self.scan_directory(node.path)
            elif node.is_file(follow_symlinks=False) and node.name.split('.')[-1] in SUPPORTED_FILES_EXTENSIONS:
                click.echo(node.path)
                yield node.path

    def get_num_crunches(self):
        """
        Calculate the number of crunches to be completed. This is calculated
        by multiplying the number of images by the number of versions.

        :return: Total number of crunches.
        """
        return len(self.images) * len(self.versions)

    @staticmethod
    def parse_size(size):
        if isinstance(size, tuple):
            return size
        size = size.split(' ')
        return tuple([int(size[0]), int(size[1])])

    def parse_json_configs(self, configs):
        self.image = self.get_config(configs, 'image', self.image)
        self.directory = self.get_config(configs, 'directory', self.directory)
        self.output = self.get_config(configs, 'output', self.output)
        self.recursive = self.get_config(configs, 'recursive', self.recursive)
        self.versions = []
        versions = configs.get('versions')
        for version in versions:
            self.versions.append({
                'file_format': self.get_config(version, 'file_format', 'jpg'),
                'quality': self.get_config(version, 'quality', 80),
                'width': self.get_config(version, 'width'),
                'height': self.get_config(version, 'height'),
                'append': self.get_config(version, 'append'),
                'orientation': self.get_config(version, 'keep_orientation', False),
                'metadata': self.get_config(version, 'keep_metadata', False),
            })
        self.nversions = len(versions)
        self.mode = self.check_mode()

    @staticmethod
    def get_config(configs, setting, default=None):
        """
        Checks if the setting exists in the configs dictionary. If it exists
        it is returned. Otherwise the default is returned.

        :param configs: Configs dictionary from the JSON config file.
        :param setting: The setting to be checked.
        :param default: The default to return if there is no setting.
        :return: The final config setting.
        """
        if configs.get(setting):
            return configs.get(setting)
        else:
            return default

    def check_mode(self):
        """
        Check if Image or Directory mode should be used.

        :return: 'img' or 'dir'
        """
        if self.image:
            return 'img'
        else:
            return 'dir'

    def run_cruncher(self):
        with click.progressbar(self.images, len(self.images), "Crunching images") as images:
            for image in images:
                for version in self.versions:
                    if self.mode == 'img':
                        path = self.image
                    else:
                        path = self.directory
                    if version.get('file_format') == 'GIF':
                        GIFCruncher(self.mode, path, self.output, image, version)
                    if version.get('file_format') == 'JPEG':
                        JPEGCruncher(self.mode, path, self.output, image, version)
                    if version.get('file_format') == 'JPEG2000':
                        JPEG2000Cruncher(self.mode, path, self.output, image, version)
                    if version.get('file_format') == 'PNG':
                        PNGCruncher(self.mode, path, self.output, image, version)
                    if version.get('file_format') == 'WebP':
                        WebPCruncher(self.mode, path, self.output, image, version)
