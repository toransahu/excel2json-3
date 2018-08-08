# Pre-requisites
1. Python 3

# Installation

## Create Virtual Enviroment

### Using [`pipenv`](https://pypi.org/project/pipenv/) (Recommended)

1. Install pipenv
    ```
    pip install pipenv
    ```
2. Create env
    ```
    cd excel2json-3  # cd <repo_dir>
    pipenv --three install
    ```

3. Activate env
    ```
    pipenv shell
    ```

4. Install requirements from Pipefile
    ```
    pipenv sync
    ```


### Using [`virtualenv`](https://pypi.org/project/virtualenv/)

1. Install virtualenv
    ```
    pip install virtualenv
    ```
2. Create virtualenv
    ```
    mkdir myvenv
    cd myvenv
    virtualenv myvenv
    ```

3. Activate `myvenv` venv
    ```
    source myvenv/bin/activate
    
    or 
    
    . myvenv/bin/activate
    ```

4. Install from requirements.txt
    ```
    pip install -r requirements.txt
    ```

# Testing
    ```
    pytest tests/test.py
    ``` 
