import streamlit as st
from utils.db_connection import cursor, conn
import pandas as pd
st.set_page_config(page_title="CricBuzz App", page_icon="🏏", layout="wide")
st.title("🗄️SQL-Driven Analytics")

option = st.selectbox(
    "Choose the type of SQL query to run:",
    [
        "Q1: Indian players - full details",
        "Q2: Recent matches",
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

elif option == "Q2: Recent matches":
    st.subheader("Recent matches")
    st.write("This query fetches the recent matches played.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select series_name,match_desc,teams,venue,city,match_date from recent_matches order by match_date desc;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select series_name,match_desc,teams,venue,city,match_date from recent_matches order by match_date desc")
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
        select team_name, wins from county_points_table order by wins desc;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select team_name, wins from county_points_table order by wins desc")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q6: Player count by role":
    st.subheader("Player count by role")
    st.write("This query counts players based on their roles (batsman, bowler, all-rounder).")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select role,count(role) from players group by role;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select role,count(role) from players group by role")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q7: Highest score by format":
    st.subheader("Highest score by format")
    st.write("This query finds the highest individual scores in different formats (Test, ODI, T20).")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select * from highest_score;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select * from highest_score")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q8: Series started in 2024":
    st.subheader("Series started in 2024")
    st.write("This query lists all series that began in the year 2024.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select id, series_name, host_country, match_type, start_date, total_matches from series_2024 order by start_date;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select id, series_name, host_country, match_type, start_date, total_matches from series_2024 order by start_date")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q9: All-rounders (1000+ runs, 50+ wickets)":
    st.subheader("All-rounders (1000+ runs, 50+ wickets)")
    st.write("This query identifies all-rounders with over 1000 runs and 50 wickets.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select p.name, a.runs,a.wickets,a.format from players p  join players_details a on p.id = a.player_id where a.runs>=1000 and a.wickets>50;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select p.name, a.runs,a.wickets,a.format from players p  join players_details a on p.id = a.player_id where a.runs>=1000 and a.wickets>50")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q10: Last 20 completed matches":
    st.subheader("Last 20 completed matches")
    st.write("This query retrieves details of the last 20 completed matches.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select match_desc, teams, winner, victory_margin, victory_type, venue from recent_matches10 order by match_date desc limit 20;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("select match_desc, teams, winner, victory_margin, victory_type, venue from recent_matches10 order by match_date desc limit 20")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q11: Player format comparison":
    st.subheader("Player format comparison")
    st.write("This query compares player statistics across different formats.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT p.name, MAX(CASE WHEN a.format = 'Test' THEN a.average END) AS test_avg, MAX(CASE WHEN a.format = 'ODI'  THEN a.average END) AS odi_avg, MAX(CASE WHEN a.format = 'T20'  THEN a.average END) AS t20_avg
        FROM players p JOIN players_details a ON p.id = a.player_id
        WHERE a.format IN ('Test', 'ODI', 'T20') GROUP BY p.name;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("""
SELECT 
    p.name,
    MAX(CASE WHEN a.format = 'Test' THEN a.average END) AS test_avg,
    MAX(CASE WHEN a.format = 'ODI'  THEN a.average END) AS odi_avg,
    MAX(CASE WHEN a.format = 'T20'  THEN a.average END) AS t20_avg
FROM players p
JOIN players_details a 
    ON p.id = a.player_id
WHERE a.format IN ('Test', 'ODI', 'T20')
GROUP BY p.name
        """)
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q12: Team home vs away wins":
    st.subheader("Team home vs away wins")
    st.write("This query compares the number of home wins versus away wins for each team.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT m.winner AS team,CASE WHEN v.country = m.winner THEN 'Home' ELSE 'Away' END AS match_location,COUNT(*) AS wins FROM matches m JOIN venue v ON m.ground = v.venue AND m.city = v.city WHERE m.winner IS NOT NULL GROUP BY m.winner, match_location ORDER BY m.winner, match_location;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("""
SELECT 
    m.winner AS team,
    CASE 
        WHEN v.country = m.winner THEN 'Home'
        ELSE 'Away'
    END AS match_location,
    COUNT(*) AS wins
FROM matches m
JOIN venue v 
    ON m.ground = v.venue 
   AND m.city = v.city
WHERE m.winner IS NOT NULL
GROUP BY m.winner, match_location
ORDER BY m.winner, match_location
        """)
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q13: 100+ run partnerships (consecutive batsmen)":
    st.subheader("100+ run partnerships (consecutive batsmen)")
    st.write("This query identifies partnerships of 100 or more runs between consecutive batsmen.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT batsman1, batsman2, match_id, series_name, match_desc, innings_id, partnership_runs FROM partnerships WHERE partnership_runs >= 100 ORDER BY partnership_runs DESC;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("SELECT batsman1, batsman2, match_id, series_name, match_desc, innings_id, partnership_runs FROM partnerships WHERE partnership_runs >= 100 ORDER BY partnership_runs DESC")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q14: Bowler venue performance":
    st.subheader("Bowler venue performance")
    st.write("This query analyzes bowler performance at different venues.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select b.player_name, b.matches_played,v.venue, b.economy as average_economy, b.wickets_taken 
        from bowl_performance b join venue v on b.venue_name = v.venue
        order by wickets_taken desc;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("""
        select b.player_name, b.matches_played,v.venue, b.economy as average_economy, b.wickets_taken 
 from bowl_performance b join venue v on b.venue_name = v.venue
 order by wickets_taken desc
""")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q15: Player performance in close matches":
    st.subheader("Player performance in close matches")
    st.write("This query evaluates player performance in matches decided by a small margin.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select b.player_name, avg(b.runs) as average_runs, count(b.match_id) as close_matches, count(b.match_id) as wins
        from batsmen_scores b join matches m on b.match_id = m.match_id
        group by b.player_name having avg(runs) > 0 order by average_runs desc;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("""select b.player_name, avg(b.runs) as average_runs, count(b.match_id) as close_matches, count(b.match_id) as wins
from batsmen_scores b join matches m
on b.match_id = m.match_id
group by b.player_name 
having avg(runs) > 0
order by average_runs desc""")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

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
        select toss_descision, count(*) as total_matches, SUM(CASE WHEN toss = winner THEN 1 ELSE 0 END) as toss_winner_wins,
        ROUND(100.0 * SUM(CASE WHEN toss = winner THEN 1 ELSE 0 END) / COUNT(*), 2) as win_percentage
        from matches group by toss_descision;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("""
select toss_descision, count(*) as total_matches,
    SUM(CASE WHEN toss = winner THEN 1 ELSE 0 END) as toss_winner_wins,
    ROUND(
        100.0 * SUM(CASE WHEN toss = winner THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) as win_percentage
from matches group by toss_descision
        """)
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q18: Most economical bowlers (ODI/T20)":
    st.subheader("Most economical bowlers (ODI/T20)")
    st.write("This query identifies the most economical bowlers in ODI and T20 formats.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT p.name, a.format, a.wickets, a.economy FROM players p join players_details a on p.id=a.player_id WHERE (format IN ('ODI', 'T20') and a.innings>10 and wickets>0) order by a.economy asc;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("SELECT p.name, a.format, a.wickets, a.economy FROM players p join players_details a on p.id=a.player_id WHERE (format IN ('ODI', 'T20') and a.innings>10 and wickets>0) order by a.economy asc")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

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
        SELECT p.name, MAX(CASE WHEN a.format = 'Test' THEN a.matches END) AS test_matches, MAX(CASE WHEN a.format = 'Test' THEN a.average END) AS test_avg, MAX(CASE WHEN a.format = 'ODI'  THEN a.matches END) AS odi_matches,
        MAX(CASE WHEN a.format = 'ODI'  THEN a.average END) AS odi_avg, MAX(CASE WHEN a.format = 'T20'  THEN a.matches END) AS t20_matches, MAX(CASE WHEN a.format = 'T20'  THEN a.average END) AS t20_avg
        FROM players p JOIN players_details a ON p.id = a.player_id WHERE a.matches > 20 AND a.format IN ('Test', 'ODI', 'T20') GROUP BY p.name;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("""SELECT 
    p.name,
    MAX(CASE WHEN a.format = 'Test' THEN a.matches END) AS test_matches,
    MAX(CASE WHEN a.format = 'Test' THEN a.average END) AS test_avg,
    MAX(CASE WHEN a.format = 'ODI'  THEN a.matches END) AS odi_matches,
    MAX(CASE WHEN a.format = 'ODI'  THEN a.average END) AS odi_avg,
    MAX(CASE WHEN a.format = 'T20'  THEN a.matches END) AS t20_matches,
    MAX(CASE WHEN a.format = 'T20'  THEN a.average END) AS t20_avg
FROM players p
JOIN players_details a 
    ON p.id = a.player_id
WHERE a.matches > 20
  AND a.format IN ('Test', 'ODI', 'T20')
GROUP BY p.name""")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)
        #Can use dataframe to combine the queries

elif option == "Q21: Player performance ranking":
    st.subheader("Player performance ranking")
    st.write("This query ranks players based on their overall performance metrics.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        select p.name, a.format,
        ((a.runs * 0.1) + (a.average * 0.5) + (a.strike_rate * 0.3)) AS batting_points,
        ((a.wickets * 2) + ((50 - a.average) * 0.5) + ((6 - a.economy) * 2)) AS bowling_points,
        (((a.runs * 0.1) + (a.average * 0.5) + (a.strike_rate * 0.3)) +
        ((a.wickets * 2) + ((50 - a.average) * 0.5) + ((6 - a.economy) * 2))) AS total_points,
        DENSE_RANK() OVER (
        PARTITION BY a.format
        order by
            (((a.runs * 0.1) + (a.average * 0.5) + (a.strike_rate * 0.3)) +
             ((a.wickets * 2) + ((50 - a.average) * 0.5) + ((6 - a.economy) * 2))) desc
        ) as format_based_rank
        from players p join players_details a on p.id = a.player_id where a.format IN ('Test','ODI','T20');
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("""select p.name, a.format,
    ((a.runs * 0.1) + (a.average * 0.5) + (a.strike_rate * 0.3)) AS batting_points,
    ((a.wickets * 2) + ((50 - a.average) * 0.5) + ((6 - a.economy) * 2)) AS bowling_points,
    (((a.runs * 0.1) + (a.average * 0.5) + (a.strike_rate * 0.3)) +
     ((a.wickets * 2) + ((50 - a.average) * 0.5) + ((6 - a.economy) * 2))) AS total_points,
    DENSE_RANK() OVER (
        PARTITION BY a.format
        order by
            (((a.runs * 0.1) + (a.average * 0.5) + (a.strike_rate * 0.3)) +
             ((a.wickets * 2) + ((50 - a.average) * 0.5) + ((6 - a.economy) * 2))) desc
    ) as format_based_rank
from players p join players_details a on p.id = a.player_id where a.format IN ('Test','ODI','T20')""")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

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
        SELECT 
        LEAST(batsman1, batsman2) AS player1,
        GREATEST(batsman1, batsman2) AS player2,
        COUNT(*) AS total_partnerships,
        ROUND(AVG(partnership_runs), 2) AS avg_runs,
        SUM(CASE WHEN partnership_runs > 50 THEN 1 ELSE 0 END) AS fifty_plus_partnerships,
        MAX(partnership_runs) AS highest_partnership,
        ROUND(100.0 * SUM(CASE WHEN partnership_runs > 50 THEN 1 ELSE 0 END) / COUNT(*),2) AS success_rate
        FROM partnerships GROUP BY LEAST(batsman1, batsman2), GREATEST(batsman1, batsman2) HAVING COUNT(*) >= 5
        ORDER BY success_rate DESC;
        """, language='sql')
    btn2 = st.button("Execute Query")
    if btn2:
        cursor.execute("""
                       SELECT 
    LEAST(batsman1, batsman2) AS player1,
    GREATEST(batsman1, batsman2) AS player2,
    COUNT(*) AS total_partnerships,
    ROUND(AVG(partnership_runs), 2) AS avg_runs,
    SUM(CASE WHEN partnership_runs > 50 THEN 1 ELSE 0 END) AS fifty_plus_partnerships,
    MAX(partnership_runs) AS highest_partnership,
    ROUND(
        100.0 * SUM(CASE WHEN partnership_runs > 50 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS success_rate
FROM partnerships
GROUP BY LEAST(batsman1, batsman2), GREATEST(batsman1, batsman2)
HAVING COUNT(*) >= 5
ORDER BY success_rate DESC""")
        players = cursor.fetchall()
        df = pd.DataFrame(players, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df,hide_index=True)

elif option == "Q25: Player performance time-series":
    st.subheader("Player performance time-series")
    st.write("This query provides a time-series analysis of player performance over their career.")
    btn = st.button("View Query")
    if btn:
        st.code("""
        SELECT * FROM players WHERE country = 'India';
        """, language='sql')
    st.table()


