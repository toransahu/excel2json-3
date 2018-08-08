#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: Sat Feb 30 13:49:20 2018

"""
convert_excel_to_json.py

Provide a link to or a file of type .xlsx/.xls & convert a MS Excel sheet to a JSON file [using xlrd python module)
"""

__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the AGPL license.'


import os
import sys
import json
import argparse
import requests
from xlrd import open_workbook  # python module 'xlrd supports .xls & .xlsx both
from xlrd.biffh import XLRDError


def download_file(url):
    """
    Download a file from url as raw.

    :param url: url string
    :return: http response
    """
    res = requests.get(url)
    if res.status_code != 200:
        print(
            f'Something wrong with URL or Server. Status Code: {res.status_code}.'
        )
        return None
    return res


def save_file(loc, filename, response):
    """
    Save a raw file into disk.

    :param loc: directory path string (to save files)
    :param filename: excel file name string
    :param response: http response from url
    :return: 0 (Success) or 1 (Failure)
    """
    if response is None:
        return 1
    else:
        try:
            if not os.path.exists(loc):
                os.mkdir(loc)
            file = os.path.join(loc, filename)
            with open(file, 'wb') as f:
                f.write(response.content)
            return 0
        except FileNotFoundError as ex:
            print(f"Something wrong with the path {loc}. Error: {ex}.")
            return 1
        except Exception as ex:
            print(
                f"Something wrong happened while saving the file {filename}. Error: {ex}."
            )
            return 1


def read_excel_sheet(abspath, sheet_name):
    """
    Read the excel sheet and return it.

    :param abspath: absolute path string to excel file
    :param sheet_name: target excel sheet name string
    :return: worksheet object
    """
    # python module 'xlrd' supports .xls & .xlsx both
    try:
        workbook = open_workbook(abspath)
        worksheet = workbook.sheet_by_name(sheet_name)
        return worksheet
    except FileNotFoundError as ex:
        print(f"Something wrong with the path {abspath}. Error: {ex}.")
        return None
    except XLRDError as ex:
        print(
            f"Something wrong happened while reading the Excel file. Error: {ex}"
        )
        return None
    except Exception as ex:
        print(
            f"Something wrong happened while reading the Excel file. Error: {ex}"
        )
        return None


def jsonify(worksheet, loc):
    """
    Read excel sheet and save whole sheet as a json file.

    :param worksheet: worksheet object
    :param loc: directory path string (to save files)
    :return: 0 (Success) or 1 (Failure)
    """
    dict_list = []

    if worksheet is None:
        print("Empty worksheet found.")
        return 1

    # store row 1 (column headers)
    header = [cell.value for cell in worksheet.row(0)]

    # read each row except header, create dict per row and append to the list
    for row_idx in range(1, worksheet.nrows):
        # row_dict = {col: worksheet.cell(row_idx, col_idx).value for col_idx, col in enumerate(header)}
        row_dict = {
            header[col_idx]: cell.value
            for col_idx, cell in enumerate(worksheet.row(row_idx))
        }
        dict_list.append(row_dict)

    # dump list of dict to JSON file
    try:
        json_file = os.path.join(loc, worksheet.name + '.json')
        with open(json_file, 'w') as json_fd:
            json.dump(
                dict_list, json_fd, sort_keys=False,
                indent=4)  # beautify JSON with indentation
        return 0
    except FileNotFoundError as ex:
        print(f'Something wrong with the path "{loc}". Error: {ex}.')
        return 1
    except IOError as ex:
        print(
            f'Something wrong happened while saving the file "{worksheet.name}.json". Error: {ex}.'
        )
        return 1


def main():
    url = 'https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls'
    loc = '../data/'
    filename = 'ISO10383_MIC.xls'
    # filename = 'ISO10383_MIC.xlsx'
    abspath = os.path.join(loc, filename)
    sheet_name = 'MICs List by CC'

    print(f'Downloading the excel file "{filename}".')
    res = download_file(url)
    result = save_file(loc, filename, res)
    if result == 0:
        print(f'"{filename}" saved at path "{loc}".')
    else:
        return 1
    print(f'Reading "{filename}".')
    worksheet = read_excel_sheet(abspath, sheet_name)
    print(f'Extracting sheet "{sheet_name}".')
    result = jsonify(worksheet, loc)
    if result == 0:
        print(
            f'Imported data from sheet "{sheet_name}" into "{sheet_name}.json" at "{loc}".'
        )
    else:
        sys.exit(1)


def convert_from_url(url, in_memory=False):
    """
    GET file from URL & In-Memory convert to JSON.
    """
    pass


def convert_from_file(filepath):
    """
    Get file & convert to JSON.
    """
    pass


def run_in_cli():
    """
    Get file & convert to JSON.
    """
    pass


# main()
