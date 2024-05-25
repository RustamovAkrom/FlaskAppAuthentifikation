# FlaskAppAuthentifikation
## Creating on Flask 

## Runing:
### 1. Create and activate enviroment
### Windows: 
~~~shell
python -m venv env
env\Scripts\activate
~~~
### Linux
~~~bash
python3 -m venv env
source env/bin/activate
~~~

### 2. Install modules
~~~shell
pip install -r requirements.txt
~~~

### 3. Initialization Database
~~~shell
flask db init
flas db migrate -m "Initial migration"
flask db upgrade
~~~
### 4. Run
~~~shell
python run.py
~~~
---
## Flask - Ci / Cd :
 + ### Create dir on your project.
 ```.github/workflows/python-app.yaml```

 + ### Example -
~~~yaml
## python-app.yaml

name: Python application

on:
  push:
    branches:
      - main

  pull_request:
    branches: 
      - main

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Load .env file
      run: |
        echo "SECRET_KEY = 'you-will-never-gues'" >> .env
        echo "DATABASE_URL = 'sqlite:///sqlite.db'" >> .env

    - name: Run tests
      run: |
        python -m pytest
~~~