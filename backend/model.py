"""PYDANTIC IS A KIND OF ORM THAT HELPS TO CREATE OUR JSON SCHEMA FROM THE MODEL"""
from pydantic import BaseModel

"""CREATE CLASS COFFEEFLAVOUR"""
class Coffeeflavour(BaseModel):
    name: str
    description: str