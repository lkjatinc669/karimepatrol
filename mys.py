import mysql.connector

# Establishing Connection 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lkjatinc669",
  database="temporary",
  auth_plugin="mysql_native_password"
)

# Creatng Cursor 
mycursor = mydb.cursor()

# Creating Table 
createtablequery = '''CREATE TABLE IF NOT EXISTS employee 
(id INTEGER NOT NULL PRIMARY KEY, 
addharno INTEGER NOT NULL,
empname vARCHAR(30) NOT NULL, 
empdept VARCHAR(30) NOT NULL, 
empage INTEGER NOT NULL)'''
mycursor.execute(createtablequery)
print("Table Created Successfully")

# Inserting Data 
insertquery = "INSERT INTO employee (id, addharno, empname, empdept, empage) VALUES (%s, %s, %s, %s, %s)"
value = [
  (1, int('000000000011'), "Nikita", "MARKETING", 21),
  (2, int('000000000022'), "Ishita", "MARKETING", 30),
  (3, int('000000000033'), "Tripti", "STAFF", 41),
  (4, int('000000000044'), "Shruti", "MANAGEMENT", 29),
  (5, int('000000000055'), "Aarti", "STAFF", 43)
]

mycursor.executemany(insertquery, value)
mydb.commit()
print(mycursor.rowcount, " rows inserted successfully")

# Updating The Data 
sql = "UPDATE employee SET empdept = '_ERP' WHERE empage >= 40"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " Records Updated")
