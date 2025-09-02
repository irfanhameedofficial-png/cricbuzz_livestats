import mysql.connector

# Direct connection
conn = mysql.connector.connect(
    host="127.0.0.1", 
    user="root",
    password="sql123",
    database="irfan",
    port=3306
)

cursor = conn.cursor()
