## Installation

### Using [`pipenv`](https://pypi.org/project/pipenv/) (Recommended)

```bash
pipenv install excel2json-3
```

### Using [`pip`](https://pypi.org/project/pip/)

```bash
pip install excel2json-3
```

## Uses

### Convert MS Excel File to JSON file

```python
from excel2json import convert_from_file


EXCEL_FILE = '../example.xls'  # or '../example.xlsx'
convert(EXCEL_FILE)
```
### Convert to JSON file directly from URL 

```python
from excel2json import convert_from_url


EXCEL_FILE_URL = 'https://www.example.com/example.xlsx'
convert(EXCEL_FILE_URL)
```
