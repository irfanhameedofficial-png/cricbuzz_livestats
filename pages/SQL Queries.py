import streamlit as st
from utils.db_connection import cursor, conn
import pandas as pd
st.set_page_config(page_title="CricBuzz App", page_icon="🏏", layout="wide")
st.title("🗄️SQL-Driven Analytics")

option = st.selectbox(
    "Choose the type of SQL query to run:",
    [
        "Q1: Indian players - full details",
        "Q2: Recent matches (last 30 days)",
        "Q3: Top 10 ODI run scorers",
        "Q4: Venues with 50,000+ capacity",
        "Q5: Team wins count",
        "Q6: Player count by role",
        "Q7: Highest score by format",
        "Q8: Series started in 2024",
        "Q9: All-rounders (1000+ runs, 50+ wickets)",
        "Q10: Last 20 completed matches",
        "Q11: Player format comparison",
        "Q12: Team home vs away wins",
        "Q13: 100+ run partnerships (consecutive batsmen)",
        "Q14: Bowler venue performance",
        "Q15: Player performance in close matches",
        "Q16: Batting trends by year (since 2020)",
        "Q17: Toss win impact analysis",
        "Q18: Most economical bowlers (ODI/T20)",
        "Q19: Consistent batsmen (since 2022)",
        "Q20: Player match count & averages by format",
        "Q21: Player performance ranking",
        "Q22: Head-to-head team analysis",
        "Q23: Recent player form & momentum",
        "Q24: Best batting partnerships",
        "Q25: Player performance time-series"
    ]
)

if option == "Q1: Indian players - full details":
    st.subheader("Indian players - full details")
    st.write("This query retrieves all details of cuurent players from India.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT name,role,battingStyle,bowlingStyle FROM indian_players;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("SELECT name,role,battingStyle,bowlingStyle FROM indian_players")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

    

elif option == "Q2: Recent matches (last 30 days)":
    st.subheader("Recent matches (last 30 days)")
    st.write("This query fetches matches played in the last 30 days.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select * from recent_matches order by match_date desc;

        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select * from recent_matches order by match_date desc")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q3: Top 10 ODI run scorers":
    st.subheader("Top 10 ODI run scorers")
    st.write("This query lists the top 10 run scorers in ODI format.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT r.id, r.name, r.matches, r.innings, r.runs, r.average, h.odi_hundreds FROM runs_odi r left join hundreds h on r.id=h.id limit 10;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("SELECT r.id, r.name, r.matches, r.innings, r.runs, r.average, h.odi_hundreds FROM runs_odi r left join hundreds h on r.id=h.id limit 10")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)


elif option == "Q4: Venues with 50,000+ capacity":
    st.subheader("Venues with 50,000+ capacity")
    st.write("This query identifies venues that can accommodate more than 50,000 spectators.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select * from venue where capacity>50000;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select * from venue where capacity>50000")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q5: Team wins count":
    st.subheader("Team wins count")
    st.write("This query counts the number of wins for each team.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q6: Player count by role":
    st.subheader("Player count by role")
    st.write("This query counts players based on their roles (batsman, bowler, all-rounder).")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select role,count(role) from indian_players group by role;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select role,count(role) from indian_players group by role")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q7: Highest score by format":
    st.subheader("Highest score by format")
    st.write("This query finds the highest individual scores in different formats (Test, ODI, T20).")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q8: Series started in 2024":
    st.subheader("Series started in 2024")
    st.write("This query lists all series that began in the year 2024.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q9: All-rounders (1000+ runs, 50+ wickets)":
    st.subheader("All-rounders (1000+ runs, 50+ wickets)")
    st.write("This query identifies all-rounders with over 1000 runs and 50 wickets.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q10: Last 20 completed matches":
    st.subheader("Last 20 completed matches")
    st.write("This query retrieves details of the last 20 completed matches.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q11: Player format comparison":
    st.subheader("Player format comparison")
    st.write("This query compares player statistics across different formats.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q12: Team home vs away wins":
    st.subheader("Team home vs away wins")
    st.write("This query compares the number of home wins versus away wins for each team.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q13: 100+ run partnerships (consecutive batsmen)":
    st.subheader("100+ run partnerships (consecutive batsmen)")
    st.write("This query identifies partnerships of 100 or more runs between consecutive batsmen.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q14: Bowler venue performance":
    st.subheader("Bowler venue performance")
    st.write("This query analyzes bowler performance at different venues.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q15: Player performance in close matches":
    st.subheader("Player performance in close matches")
    st.write("This query evaluates player performance in matches decided by a small margin.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q16: Batting trends by year (since 2020)":
    st.subheader("Batting trends by year (since 2020)")
    st.write("This query analyzes batting trends on a yearly basis since 2020.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q17: Toss win impact analysis":
    st.subheader("Toss win impact analysis")
    st.write("This query examines the impact of winning the toss on match outcomes.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q18: Most economical bowlers (ODI/T20)":
    st.subheader("Most economical bowlers (ODI/T20)")
    st.write("This query identifies the most economical bowlers in ODI and T20 formats.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q19: Consistent batsmen (since 2022)":
    st.subheader("Consistent batsmen (since 2022)")
    st.write("This query finds batsmen with consistent performance since 2022.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q20: Player match count & averages by format":
    st.subheader("Player match count & averages by format")
    st.write("This query retrieves the number of matches played and batting/bowling averages for players by format.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q21: Player performance ranking":
    st.subheader("Player performance ranking")
    st.write("This query ranks players based on their overall performance metrics.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q22: Head-to-head team analysis":
    st.subheader("Head-to-head team analysis")
    st.write("This query analyzes head-to-head statistics between different teams.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q23: Recent player form & momentum":
    st.subheader("Recent player form & momentum")
    st.write("This query evaluates recent player performance to identify form and momentum.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q24: Best batting partnerships":
    st.subheader("Best batting partnerships")
    st.write("This query identifies the best batting partnerships in terms of runs scored.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()

elif option == "Q25: Player performance time-series":
    st.subheader("Player performance time-series")
    st.write("This query provides a time-series analysis of player performance over their career.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()


    