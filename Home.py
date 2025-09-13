import streamlit as st


st.set_page_config(page_title="CricBuzz App", page_icon="🏏", layout="wide")

st.title("🏏 Cricbuzz Home Page")
st.write("Welcome to the CricBuzz App! Navigate through the pages using the sidebar to view live scores, explore player stats, perform CRUD operations on the player data and run SQL queries for in-depth cricket analytics.")

st.subheader("CRUD Operations")
st.markdown("""
🔹 This page allows you to create, view, edit, and delete players from the database.
""")

st.subheader("Live Scores")
st.markdown("""
🔹 This page provides live scores and recent cricket match details.
""")

st.subheader("Player Stats")
st.markdown("""
🔹 This page provides up-to-date player statistics.
""")

st.subheader("SQL Queries")
st.markdown("""
🔹 This page provides SQL queries for in-depth cricket analytics.
""")

st.subheader("About")
st.markdown("""
   🔹 This Web App was developed by **Hameed Badhusha Irfan F**. Feel free to reach out for any queries or feedback!
""")

