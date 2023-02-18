"""ADDING HHTTPEXCEPTION TO HANDLE REQUEST ERROR EXCEPTIONS"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from  model import Coffeeflavour

app = FastAPI()

"""IMPORT ALL FUNCTIONS FROM DB.py"""
from database import (
    fetch_one_coffeeflavour,
    fetch_all_coffeeflavours,
    create_coffeeflavour,
    update_coffeeflavour,
    remove_coffeeflavour,
)

#SPECIFYING THE HOST ORIGIN - LOCALLY: LOCALHOST:8000 TO ALLOW ACCESS TO HEADERS, METHODS AND SON ON...
origins = ["http://localhost:8000"]
#CREATING AN OBJECT APP TO INSTANTIATE THE FAST API CLASS | /docs GIVES THE FAST API DOCS - DOCS IS CALLED SWAGGER UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#CHECKING SERVER RESPONSE -> SUCCESSFUL | API COFFEEFLAVOUR
@app.get("/")
async def main():
    return {"Message": "HTTP Request"}

#GET Coffeeflavour
@app.get("/api/coffeeflavour")
async def get_coffeeflavour():
    response = await fetch_all_coffeeflavours()
    return response

#GET Coffeeflavour BY ID
@app.get("/api/coffeeflavour{name}, response_model=Coffeeflavour")
async def get_coffeeflavour_by_id(name):
    response = await fetch_one_coffeeflavour(name)
    if response:
        return response
    raise HTTPException(404, f"We do not have a coffee flavour with this name{name}")

#POST coffeeflavour
@app.post("/api/coffeeflavour", response_model=Coffeeflavour)
async def post_coffeeflavour(coffeeflavour:Coffeeflavour):
    response = await create_coffeeflavour(coffeeflavour.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong with the request")

#UPDATE Coffeeflavour
@app.put("/api/coffeeflavour{name}/", response_model=Coffeeflavour)
async def put_coffeeflavour(name:str, desc:str):
    response = await update_coffeeflavour(name, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no Coffeeflavour in the menu with this name{name}")

#DELETE COFFECUP
@app.delete("/api/coffeeflavour{name}")
async def delete_coffeeflavour(name):
    response = await remove_coffeeflavour(name) 
    if response:
        return "Successfully deleted coffee flavour in menu!"
    raise HTTPException(404, f"There is no Coffeeflavour in the menu with this name{name}")
