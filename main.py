from optparse import Option
from DB import *
import time
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/getElements")
async def readWithConditions(first_name: Optional[str]=None, last_name: Optional[str]=None,
                            city: Optional[str]=None, state: Optional[str]=None, department: Optional[str]=None,
                            limit: Optional[int]=None):
    extraQuery = "" # Aux to prepare extra query clauses (WHERE, LIMIT)
    # If some condition exists, add WHERE clause
    if first_name or last_name or city or state or department:
        extraQuery = extraQuery + " WHERE "
    # Prepare query with condition in specific field
    if first_name:
        extraQuery = extraQuery + "  first_name LIKE '"+ first_name +"' AND"
    if last_name:
        extraQuery = extraQuery + "  last_name LIKE '"+ last_name +"' AND"
    if city: 
        extraQuery = extraQuery + "  city LIKE '"+ city +"' AND"
    if state:
        extraQuery = extraQuery + "  state LIKE '"+ state +"' AND"
    if department:
        extraQuery = extraQuery + "  department LIKE '"+ department +"' AND"
    extraQuery = extraQuery[:-3] # Eliminate 3 last chars (A,N,D) from query condition
    # IF Limit exists, add the correct clause
    if limit:
        extraQuery = extraQuery + " LIMIT " + str(limit)
    # Call Function which actually executes query  
    records = getAllRecords(extraQuery)
    return {"elements": records}

@app.post("/insertElement")
async def addRow(row: dict):
    return insertIntoDB(row)
