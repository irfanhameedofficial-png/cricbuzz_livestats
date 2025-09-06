from utils.db_connection import cursor, conn
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CricBuzz App", page_icon="🏏", layout="wide")
st.title("📖Full CRUD operations for data management")
st.header("Add new records, view existing records, update them, or delete them as needed.")  

option = st.selectbox("Select SQL Operation to perform", ["➕Create (Add Player)", "🔍Read (View Player)", "✏️Update (Edit Player)", "🗑️Delete (Remove Player)"],index=None)

# Create Player  ---------------------------------------------------------
if option == "➕Create (Add Player)":
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

    if submit_button:
        if id and name and country and role and matches and runs_scored and wickets_taken:
            try:
                cursor.execute("""
                    INSERT INTO crud_player_info (player_id, player_name, player_country, player_role, matches_played, runs_scored, wickets_taken)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (id, name, country, role, matches, runs_scored, wickets_taken))
                conn.commit()
                st.success(f"Player '{name}' added successfully!")
            except Exception as e:
                conn.rollback()
                if e.errno == 1062:
                    st.warning("Player ID already exists. Use a new one.")
                elif e.errno == 1366:
                    st.warning("Incorrect value entered for fields.")
                st.error(f"Error adding player: {e}")
        else:
            st.error("Please fill in all required fields.")
    

# Read Player  ---------------------------------------------------------
elif option == "🔍Read (View Player)":
    st.subheader("View Player")
    with st.form("search_player_form"):
        player_name = st.text_input("Player Name")
        submit_button = st.form_submit_button("Search Player")
    if submit_button:
        cursor.execute("SELECT * FROM crud_player_info where player_name like %s", [f"%{player_name}%"])
        players = cursor.fetchall()
        if players:
            df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)
        else:
            st.warning(f"Player: {player_name} not found in the database.")

    st.subheader("View All Players")
    with st.form("view_all_players"):
        #player_name = st.text_input("Player Name")
        submit_button = st.form_submit_button("View All Players")
    if submit_button:
        cursor.execute("SELECT * FROM crud_player_info")
        players = cursor.fetchall()
        if players:
            df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)
        else:
            st.warning(f"No Players found in the database.")


# Edit Player  ---------------------------------------------------------
elif option == "✏️Update (Edit Player)":
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

    if submit_button:
        if id and name and country and role and matches and wickets_taken and runs_scored:
            try:
                cursor.execute("""
                    UPDATE crud_player_info
                    SET player_id=%s, player_name=%s, player_country=%s, player_role=%s, matches_played=%s, runs_scored=%s, wickets_taken=%s
                    WHERE player_id=%s
                """, (id, name, country, role, matches, runs_scored, wickets_taken, id))
                conn.commit()
                if cursor.rowcount:
                    st.success(f"Player ID '{id}' updated successfully!")
                else:
                    st.warning(f"No player found with ID '{id}'.")
            except Exception as e:
                conn.rollback()
                if e.errno == 1366:
                    st.warning("Incorrect value entered for fields.")
                st.error(f"Error updating player: {e}")
        else:
            st.error("Please fill in all required fields.")

# Delete Player  ---------------------------------------------------------
elif option == "🗑️Delete (Remove Player)":
    st.subheader("Remove Player")
    with st.form("delete_player_form"):
        #id = st.number_input("Player ID to Delete", min_value=1, step=1)
        name = st.text_input("Player Name to Delete")
        submit_button = st.form_submit_button("Delete Player")

    if submit_button:
        if name:
            try:
                cursor.execute("DELETE FROM crud_player_info WHERE player_name=%s", (name,))
                conn.commit()
                if cursor.rowcount:
                    st.success(f"Player ID '{name}' deleted successfully!")
                else:
                    st.warning(f"No player found with Name '{name}'.")
            except Exception as e:
                conn.rollback()
                st.error(f"Error deleting player: {e}")
        else:
            st.error("Please provide a valid Player Name.") 





# cursor.execute("SELECT * from employees")
# tables = cursor.fetchall()

# # Build DataFrame with column names
# df = pd.DataFrame(tables, columns=[desc[0] for desc in cursor.description])
# st.dataframe(df, hide_index=True)




