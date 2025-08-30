from utils.db_connection import cursor, conn
import streamlit as st

st.set_page_config(page_title="CricBuzz App", page_icon="🌐", layout="wide")
st.title("Full CRUD operations for data management")
st.write("Perform Create, Read, Update, Delete operations here.")

st.write("You can add new records, view existing records, update them, or delete them as needed.")  

cursor.execute("SELECT * from irfan")
tables = cursor.fetchall()  
st.table(tables)