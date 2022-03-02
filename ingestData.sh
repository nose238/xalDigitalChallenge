## Conf Vars
user='postgres'
pw='example'
ip='db'
table='sample'
# Create Table
PGPASSWORD=$pw psql -h $ip -U $user -c " CREATE TABLE IF NOT EXISTS $table (first_name varchar(30),\
last_name varchar(30),\
company_name varchar(30),\
address varchar(50),\
city varchar(20),\
state varchar(2),\
zip varchar(5),\
phone1 varchar(12),\
phone2 varchar(12),\
email varchar(40),\
department varchar(30)
);"
# Copy CVS to table created
PGPASSWORD=$pw psql -h $ip -U $user  -c "\\COPY $table (first_name,last_name,company_name,address,city,state,zip,phone1,phone2,email,department) FROM '/code/Sample.csv' DELIMITER ',' CSV HEADER"
