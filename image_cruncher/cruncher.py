"""
:Project: Image Cruncher
:Contents: cruncher.py
:copyright: © 2019 Daniel Morell
:license: GPL-3.0, see LICENSE for more details.
:Author: DanielCMorell
:Added v0.0.1.dev -- 9/30/2019
"""
# Standard Library Imports
import os
import json

# Package Imports
import click
from PIL import Image

# Local Imports


class CruncherBase:

    def __init__(self, image, directory, output, image_path, version):
        self.image = image
        self.directory = directory
        self.output = output
        self.image_path = image_path
        self.version = version
        directory, filename = os.path.split(image_path)
        self.filename = self.generate_filename(filename, version)
        self.new_path = self.image_output_path(os.path.join(directory, filename))

        self.crunch_image(image_path, version)

    def image_output_path(self, image_path):
        # TODO write proper single image path calculation
        if self.mode == 'img':
            return image_path
        relative_path = os.path.relpath(image_path, self.directory)
        path = os.path.join(self.output, relative_path)
        return path

    def crunch_image(self, path, version):
        image = Image.open(path)
        directory, filename = os.path.split(path)
        filename = self.generate_filename(filename, version)
        new_path = self.image_output_path(os.path.join(directory, filename))
        exif = None
        if version['keep_metadata']:
            print(image.info)
            exif = image.info['exif']
        full = self.resize(image, (version['width'], version['height']), version)
        full.save(new_path, "JPEG", quality=version['quality'], optimize=True, progressive=True, exif=exif)

    def generate_filename(self, filename, version):
        return f"{filename}{version['append']}.{version['file_format']}"

    @staticmethod
    def resize(image, size=None, version=None):
        """
        The `resize()` function changes the size of an image without squashing or stretching
        as the PIL.Image.resize() function does. The `size` argument should be a tuple formatted
        as (width, height).

        :param image: PIL image object
        :param size: Tuple with 2 values (width, height)
        :param version: The image version dictionary.
        :return: PIL image object
        """

        if not size:
            return image

        old_aspect = image.width / image.height
        new_aspect = size[0] / size[1]

        if version['orientation']:
            # if one is horizontal and the other vertical flip the orientation
            if old_aspect < 0 <= new_aspect or old_aspect >= 0 > new_aspect:
                size = (size[1], size[0])
                new_aspect = size[0] / size[1]

        if size == (image.width, image.height):
            return image

        if new_aspect < old_aspect:
            image.thumbnail([size[1] * old_aspect, size[1]], Image.LANCZOS)
        else:
            image.thumbnail([size[0], size[0] * old_aspect], Image.LANCZOS)

        left = (image.width - size[0]) / 2
        top = (image.height - size[1]) / 2
        right = image.width - left
        bottom = image.height - top

        box = (left, top, right, bottom)

        cropped = image.crop(box)

        return cropped


class JPEGCruncher(CruncherBase):

    def __init__(self, image, directory, output, image_path, version):
        super().__init__(image, directory, output, image_path, version)

    def crunch_image(self, path, version):
        image = Image.open(path)
        exif = None
        if version['keep_metadata']:
            print(image.info)
            exif = image.info['exif']
        image = self.resize(image, (version['width'], version['height']), version)
        image.save(new_path, "JPEG", quality=version['quality'], optimize=True, progressive=True, exif=exif)

