# FastAPI + mongodb CRUD

This project uses FastAPI to create a Rest api with all the CRUD operations of a todo list.

## To execute the project: 

* You can use a virtual environment to keep the dependencies locally
* You have to set up a mongodb database locally
1. ```pip install -r requirements.txt```
2. ```uvicorn main:app --reload``` or use the makefile command: ```make start-dev```
3. Access on browser: http://localhost:8000/docs to get the swagger doc.