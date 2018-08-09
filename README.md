# Excel to JSON Converter
[![Build Status](https://travis-ci.org/toransahu/excel2json-3.svg?branch=master)](https://travis-ci.org/toransahu/excel2json-3)
[![PyPI version](https://badge.fury.io/py/excel2json-3.svg)](https://badge.fury.io/py/excel2json-3)
![Python Version](https://img.shields.io/badge/python-3%2C%203.6-yellow.svg)
[![Say Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/toransahu)

A minimal API that converts MS Excel (.xls & .xlsx) files, or from a given URL into JSON files.

## Features
- Download as package using [`pip`](https://pypi.org/project/pip/) and use in your code. 
- Supports both type of MS Excel file formats
    - MS Excel 2003 (.xls)
    - MS Excel 2007 (.xlsx)

- It also comes with command line interface (CLI) which facilitates the conversion from URL or local MS Excel file to JSON files.

    Example:

    - GET file from URL & convert to JSON.
    ```bash
    python -m excel2json-3 --urls https://example.com/example.xls
    ```
    
    - GET file from disk & convert to JSON.
    ```bash
    python -m excel2json-3 --file /home/ubuntu/Documents/example.xlsx
    ```


## Contribution
You can contribute in following ways:

- Report bugs
- Add more "APIs" 
- Give suggestions to make it better
- Fix issues & submit a pull request
