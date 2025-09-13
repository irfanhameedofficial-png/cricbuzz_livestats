import mysql.connector

# Direct connection
conn = mysql.connector.connect(
    host="127.0.0.1", 
    user="root",
    password="sql123",
    database="cricbuzz_livestats",
    port=3306
)

cursor = conn.cursor()

api_key = "4acde6c146msha2eb7fb3b8c113ep1351fcjsnee5fb67d30b3"
api_key2 = "4879a17e0cmsh37b379d4ab14552p161d4djsncf56613e28e8"