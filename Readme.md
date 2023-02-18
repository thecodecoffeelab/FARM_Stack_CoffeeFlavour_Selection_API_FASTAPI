1 - FastApi version 0.6.1
2 - Uvicorn: A ASGI web implementation for Python version 0.14.0
3 - Motor:  Asynchronous Python driver for MongoDB version 2.4.0 | Motor works with Tornado framework as well.

******************************************************************************
Install pipenv -> pip is packet manager for Python to create virtual environment
Run pip shell to create the virtual env -> comd: pipenv shell

******************************************************************************
In case pipenv shell is not working for you:
******************************************************************************
You need to run pipenv with the python associated with the pip3.

so python3 -m pipenv shell considers that pip3 is associaed with python3.

If it is not working then you can install pipenv again with the python as

python3 -m pip install pipenv

and python3 -m pipenv shell

I case uvicorn main app is not running on 3000 do this: uvicorn main:app --host 127.0.0.1 --port 3000 --reload 
documentation: https://fastapi.tiangolo.com/deployment/manually/
******************************************************************************
Make sure u have install a react app with npx create-react-app your_app_name -> here it is frontend part
Dependencies:
- Axios: sending requests from client to server and getting request from backend server to the client
- Bootstrap for just template
******************************************************************************
IN CASE YOU SEE WARNING ERRORS ON IMPORTS IN BACKEND SECTION WITH PYTHON
******************************************************************************
Just do Ctrl+shift+p and search for Python: Select Interpreter and use the correct one. Warning issues will disappear