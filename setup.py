"""
setup.py

:Project: Image Cruncher
:Contents: setup.py
:copyright: © 2019 Daniel Morell
:license: GPL-3.0, see LICENSE for more details.
:Author: DanielCMorell
"""

import io
import re
from setuptools import setup

with io.open("image_cruncher/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

with io.open("README.md", "rt", encoding='utf8') as fh:
    readme = fh.read()

setup(
    name='image_cruncher',
    version=version,
    license='GPLv3+',
    url='https://github.com/danmorell/Image-Cruncher',
    author='Daniel Morell',
    author_email='office@carintek.com',
    description="Simple CLI to optimize images for the web.",
    long_description=readme,
    long_description_content_type="text/markdown",
    py_modules=['image_cruncher'],
    install_requires=[
        'Click',
        'Pillow',
    ],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points='''
        [console_scripts]
        image_cruncher=image_cruncher:cli
    ''',
)
