#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-08-07 19:15

"""
setup.py
"""

import os
import sys
import setuptools
from codecs import open


__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the AGPL license.'

here = os.path.abspath(os.path.dirname(__file__))

##
# Shortcut to publish the package.
# setup.py publish
##
if sys.argv[-2:] == ['--test', 'publish']:
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload --repository-url https://test.pypi.org/legacy/ dist/*')
    sys.exit()
elif sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    # os.system('twine upload --repository-url https://upload.pypi.org/legacy/ dist/*')
    sys.exit()


##
# sub-packages to include 
##
packages = ['excel2json']


##
# get basic info about the package
##
about = {}
with open(os.path.join(here, '__about__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

##
# get long description about the package from README.md
##
with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join(here, "docs", "USES.md"), "r") as f:
    uses_description = f.read()

with open(os.path.join(here, "docs", "DEVELOPMENT.md"), "r") as f:
    dev_description = f.read()


setuptools.setup(
        name=about['__title__'],
        version=about['__version__'],
        author=about['__author__'],
        author_email=about['__author_email__'],
        description=about['__description__'],
        long_description=long_description + uses_description + dev_description,
        long_description_content_type="text/markdown",
        url=about['__github__'],
        license=about['__license__'],
        # packages=setuptools.find_packages(),
        packages=packages,
        classifiers=(
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
            "Operating System :: OS Independent",
            'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Archiving :: Packaging',
            "Topic :: Text Processing",
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: Information Technology",
            "Natural Language :: English",

        ),
        keywords=(
            "excel to json", 
            "xlsx to json", "xls to json", 
            "xlsx", "xls", "json",
        ),
        install_requires=(
            "xlrd",
            "openpyxl",
            "requests",
        )
            
)
