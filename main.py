from DB import *
import time
from fastapi import FastAPI
from typing import Optional

app = FastAPI()
 
# Read all elements of DB
@app.get("/readAll")
def root():
    records = getAllRecords()
    return {"message": records}

