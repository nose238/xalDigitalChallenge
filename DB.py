import psycopg2

# Connect to DB and return connection
def connectToDB():
    conn = psycopg2.connect(user="postgres", password="example", host="db", port='5432')
    conn.autocommit = True
    cursor = conn.cursor()
    c = {}
    c["cursor"] = cursor
    c["connection"] = conn
    return c
#hola
# Excec a query inside DB
def execQuery(query):
    connection = connectToDB()
    connection["cursor"].execute(query)
    json_response = []
    for i in connection["cursor"].fetchall():
        first_name = i[0]
        last_name = i[1]
        company_name = i[2] 
        address = i[3]
        city = i[4]
        state = i[5]
        zip = i[6]
        phone1 = i[7]
        phone2 = i[8]
        email = i[9]
        department = i[10]
        json_element = {"first_name": first_name, "last_name": last_name , \
        "company_name": company_name, "address": address, "city": city, \
        "state": state, "zip": zip, "phone1": phone1, "phone2": phone2, \
        "email": email, "department": department}
        json_response.append(json_element)
    connection["connection"].commit()
    connection["connection"].close()
    return json_response

# Get all records. It may use extra query (WHERE & LIMIT clauses)
def getAllRecords(extraQuery=""):
    completeQuery = "SELECT * FROM sample " + extraQuery + ";"
    return execQuery(completeQuery)

# 
def insertIntoDB(elementToInsert):
    estatusElement = elementIsValid(elementToInsert)
    if  estatusElement == 0:
        query = "INSERT INTO sample (first_name,last_name,company_name,address,city,state,zip,phone1,phone2,email,department) VALUES " 
        query = query + "('" + elementToInsert["first_name"] + "' , '" + elementToInsert["last_name"] + \
            "', '" + elementToInsert["company_name"] + "', '" + elementToInsert["address"] + "' , '" + \
            elementToInsert["city"] + "' , '" + elementToInsert["state"] + "' , '" + \
            elementToInsert["zip"] + "' , '" + elementToInsert["phone1"] + "' , '" + elementToInsert["phone2"] + \
            "' , '" + elementToInsert["email"] +  "' , '" + elementToInsert["department"] + "') ; "
        connection = connectToDB()
        connection["cursor"].execute(query)
        connection["connection"].commit()
        connection["connection"].close()
        return "OK! Row inserted"
    elif estatusElement == 1:
        return "phone2 is the optional field. The rest of them are required"
    elif estatusElement == 2:
        return "length of city must be equals to 2"

# True if element is valid. False if it's not 
def elementIsValid(element):
    if  "first_name" not in element or "last_name" not in element or \
        "company_name" not in element or "address" not in element or  \
        "address" not in element or "city" not in element or  \
        "state" not in element or "zip" not in element or \
        "phone1" not in element or "email" not in element or \
        "department" not in element:
        return 1
    elif "phone2" not in element:
        element["phone2"] = " "
    if len(element["state"]) > 2:
        return 2
    else:
        return 0
    