# Pre-requisites
1. Linux
2. Python 3.6.4

# Installation
Install requirements in virtual environment

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

4. Install from requirements.pip
    ```
    pip install -r requirements.pip
    ```

# Code Execution
1. Change to 'src' directory
    ```
    cd excel-to-json/src/
    ``` 
2. Run the application
    ```
    python convert_excel_to_json.py
    ``` 

    
# Testing
1. Test convert_excel_to_json.py module
    ```
    cd excel-to-json/src/
    pytest test.py
    ``` 