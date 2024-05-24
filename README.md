# FlaskAppAuthentifikation

## Runing...
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