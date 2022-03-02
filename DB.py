
import psycopg2

def execQuery(query):
    conn = psycopg2.connect(user="postgres", password="example", host="db", port='5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(query)
    json_response = []
    for i in cursor.fetchall():
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
    conn.commit()
    conn.close()
    return json_response

def getAllRecords():
    return execQuery("SELECT * FROM sample;")
