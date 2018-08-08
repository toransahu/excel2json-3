"""Testing  'convert_excel_to_json' module using 'pytest'."""


import os
try:
    from convert_excel_to_json import download_file, save_file, read_excel_sheet, jsonify
except:
    from src.excel2json.convert_excel_to_json import download_file, save_file, read_excel_sheet, jsonify


URL = 'https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls'  # Correct
URL1 = 'https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MI.xls'  # C is missing before .xls
LOC = '../../data/'
LOC1 = ''
LOC2 = 'abc'
FILENAME = 'ISO10383_MIC.xls'
INVALID_FILE = 'invalid_file.xls'
SHEET_NAME_INCORRECT = 'MICs List by'  # correct one is 'MICs List by CC'
SHEET_NAME = 'MICs List by CC'


# passed Invalid URL
def test_download_file_negative():
    assert download_file(URL1) is None


# passed None response
def test_save_file_negative1():
    assert save_file(LOC, FILENAME, None) == 1


# passed invalid directory location/path
def test_save_file_negative2():
    assert save_file(LOC1, FILENAME, download_file(URL)) == 1


# passed invalid excel file
def test_read_excel_sheet_negative():
    assert read_excel_sheet(os.path.join(LOC, INVALID_FILE),
                            SHEET_NAME) is None


# passed invalid sheet name
def test_read_excel_sheet_negative():
    assert read_excel_sheet(os.path.join(LOC, FILENAME),
                            SHEET_NAME_INCORRECT) is None


# passed invalid directory path
def test_read_excel_sheet_negative():
    assert read_excel_sheet(os.path.join(LOC2, FILENAME), SHEET_NAME) is None


# passed empty worksheet
def test_jsonify_negative():
    assert jsonify(None, LOC) == 1


# passed invalid path
def test_jsonify_negative():
    assert jsonify(
        read_excel_sheet(os.path.join(LOC, FILENAME), SHEET_NAME), LOC2) == 1
