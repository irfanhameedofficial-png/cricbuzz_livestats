from utils.db_connection import cursor, conn
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CricBuzz App", page_icon="🌐", layout="wide")
st.title("Full CRUD operations for data management")
st.header("Perform Create, Read, Update, Delete operations here.")
st.text("You can add new records, view existing records, update them, or delete them as needed.")  

option = st.selectbox("Select SQL Operation to perform", ["Create (Add Player)", "Read (View Player)", "Update (Edit Player)", "Delete (Remove Player)"])

if option == "Create (Add Player)":
    st.subheader("Add a New Player")
    with st.form("add_player_form"):
        id = st.number_input("Player ID", min_value=1, step=1)
        name = st.text_input("Player Name")
        country = st.text_input("Country")
        role = st.selectbox("Role", ["Batsman", "Bowler", "All-Rounder", "Wicket-Keeper"])
        matches = st.text_input("Matches Played")
        runs_scored = st.text_input("Runs Scored")
        wickets_taken = st.text_input("Wickets Taken")
        submit_button = st.form_submit_button("Add Player")

    # if submit_button:
    #     if name and country and role:
    #         try:
    #             cursor.execute("""
    #                 INSERT INTO players (name, country, role, batting_style, bowling_style)
    #                 VALUES (%s, %s, %s, %s, %s)
    #             """, (name, country, role, batting_style, bowling_style))
    #             conn.commit()
    #             st.success(f"Player '{name}' added successfully!")
    #         except Exception as e:
    #             conn.rollback()
    #             st.error(f"Error adding player: {e}")
    #     else:
    #         st.error("Please fill in all required fields.")
    

elif option == "Read (View Player)":
    st.subheader("View Player")
    with st.form("search_player_form"):
        id = st.text_input("Player Name")
        submit_button = st.form_submit_button("Search Player")
    # cursor.execute("SELECT * FROM players")
    # players = cursor.fetchall()
    # if players:
    #     df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
    #     st.dataframe(df)
    # else:
    #     st.info("No players found in the database.")

elif option == "Update (Edit Player)":
    st.subheader("Edit Player Details")
    with st.form("edit_player_form"):
        id = st.number_input("Player ID to Edit", min_value=1, step=1)
        name = st.text_input("Player Name")
        country = st.text_input("Country")
        role = st.selectbox("Role", ["Batsman", "Bowler", "All-Rounder", "Wicket-Keeper"])
        matches = st.text_input("Matches Played")
        runs_scored = st.text_input("Runs Scored")
        wickets_taken = st.text_input("Wickets Taken")
        submit_button = st.form_submit_button("Update Player")

    # if submit_button:
    #     if id and name and country and role:
    #         try:
    #             cursor.execute("""
    #                 UPDATE players
    #                 SET name=%s, country=%s, role=%s, batting_style=%s, bowling_style=%s
    #                 WHERE id=%s
    #             """, (name, country, role, batting_style, bowling_style, id))
    #             conn.commit()
    #             if cursor.rowcount:
    #                 st.success(f"Player ID '{id}' updated successfully!")
    #             else:
    #                 st.warning(f"No player found with ID '{id}'.")
    #         except Exception as e:
    #             conn.rollback()
    #             st.error(f"Error updating player: {e}")
    #     else:
    #         st.error("Please fill in all required fields.")

elif option == "Delete (Remove Player)":
    st.subheader("Remove Player")
    with st.form("delete_player_form"):
        id = st.number_input("Player ID to Delete", min_value=1, step=1)
        submit_button = st.form_submit_button("Delete Player")

    # if submit_button:
    #     if id:
    #         try:
    #             cursor.execute("DELETE FROM players WHERE id=%s", (id,))
    #             conn.commit()
    #             if cursor.rowcount:
    #                 st.success(f"Player ID '{id}' deleted successfully!")
    #             else:
    #                 st.warning(f"No player found with ID '{id}'.")
    #         except Exception as e:
    #             conn.rollback()
    #             st.error(f"Error deleting player: {e}")
    #     else:
    #         st.error("Please provide a valid Player ID.") 

# cursor.execute("SELECT * from employees")
# tables = cursor.fetchall()

# # Build DataFrame with column names
# df = pd.DataFrame(tables, columns=[desc[0] for desc in cursor.description])
# st.dataframe(df, hide_index=True)




