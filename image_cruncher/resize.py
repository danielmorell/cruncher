"""
resize.py

Project: Image Cruncher
Contents: resize.py
Author: DanielCMorell
Added v0.0.1.dev -- 9/27/2019
"""
# Standard Library Imports

# Package Imports
from PIL import Image

# Local Imports


def resize(image, size: tuple):
    """
    The `resize()` function changes the size of an image without squashing or stretching
    as the PIL.Image.resize() function does. The `size` argument should be a tuple formatted
    as (width, height).

    :param image: PIL image object
    :param size: Tuple with 2 values (width, height)
    :return: PIL image object
    """

    old_aspect = image.width / image.height
    new_aspect = size[0] / size[1]

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
