from  model import Coffeeflavour
"""RUN MOTOR WHICH IS THE MONGO DB DRIVER"""
import motor.motor_asyncio

"""CLIENT TO COONECT THE DB.py AND MONGO DB"""
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')

"""CREATE A DATABASE CALLED COFFEECUPMENU AND A TABLE CALLED COFFEEFLAVOUR"""
database = client.CoffeeMenu
collection = database.coffeeflavour

"""FUNCTION ASYNC TO GET 1 COFFEEFLAVOUR BY NAME"""
async def fetch_one_coffeeflavour(name):
    document = await collection.find_one({"name:name"})
    return document

"""FUNCTION ASYNC TO GET ALL COFFEEFLAVOURS BY LOOPING THROUGH THE VARIBALE CURSOR  | INSERT OR FIND ARE MONGO DB METHODS TO INTERACT WITH PYTHON WHILE RUNNING MOTOR DRIVER"""
async def fetch_all_coffeeflavours():
    coffeeflavours = []
    cursor = collection.find({})
    async for document in cursor:
        coffeeflavours.append(Coffeeflavour(**document))
        return coffeeflavours

"""FUNCTION TO CREATE A COFFEEFLAVOUR"""
async def create_coffeeflavour(coffeeflavour):
    document = coffeeflavour
    result = await collection.insert_one(document)
    return document

"""UPDATE A COFFEEFLAVOUR"""
async def update_coffeeflavour(name, desc):
    await collection.update_one(
        {"name":name},
        {"$set":{
            "description":desc}})
    document = await collection.find_one({"name:name"})
    return document

"""FUNCTION ASYNC TO DELETE A COFFEEFLAVOUR"""
async def remove_coffeeflavour(name):
    await collection.delete_one({"name":name})
    return True