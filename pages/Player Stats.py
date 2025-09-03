import streamlit as st

st.set_page_config(page_title="CricBuzz App", page_icon="🏏", layout="wide")

st.title("📊Detailed Player Statistics")
st.write("Displaying player statistics from CricBuzz.")

st.write("🔍Enter the player's name to fetch their stats.")
player_name = st.text_input("Player Name:", placeholder="e.g., Virat Kohli")
submit = st.button("Fetch Stats")

# Note: Actual data fetching and display logic would go here.
if submit and player_name:
    #Show the list of players matching the name as dropdown with the list of matching names
    st.write(f"Fetching stats for: {player_name}")
    # For now, just a placeholder message
    st.write("Player stats functionality is under development.")

    

