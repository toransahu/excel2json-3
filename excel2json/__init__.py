#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-08-08 23:08

"""
__init__.py
"""

import os
import sys
from api.convert import convert_from_file, convert_from_url, jsonify


__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the MIT license.'


# url = 'https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls'


def cli():
    """
    Command line utility
    """
    try:
        if sys.argv[-2] == "--file":
            if os.path.isfile(sys.argv[-1]):
                convert_from_file(sys.argv[-1])
            else:
                print("Not an Excel file")
        elif sys.argv[-2] == "--url":
            if sys.argv[-1].startswith('http://') or sys.argv[-1].startswith('https://'):
                convert_from_url(sys.argv[-1])
            else:
                print("Not a valid link")
        else:
            print("Invalid option")
    except:
        print("Provided some options!")