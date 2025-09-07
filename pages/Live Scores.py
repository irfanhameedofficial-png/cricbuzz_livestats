import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="CricBuzz App", page_icon="🏏", layout="wide")
st.title("📡Live Cricket Scores")

try:
    st.subheader("Displaying live cricket scores from CricBuzz.")
    #Live Matches API
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
        "x-rapidapi-key": "4879a17e0cmsh37b379d4ab14552p161d4djsncf56613e28e8",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    #Remove comment in below line for live execution
    # response = requests.get(url, headers=headers)
    # response.raise_for_status()
    # data = response.json()

    #Add comment line below for live execution
    data = {'typeMatches': [{'matchType': 'International', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10267, 'seriesName': 'Sri Lanka tour of Zimbabwe, 2025', 'matches': [{'matchInfo': {'matchId': 122968, 'seriesId': 10267, 'seriesName': 'Sri Lanka tour of Zimbabwe, 2025', 'matchDesc': '2nd T20I', 'matchFormat': 'T20', 'startDate': '1757158200000', 'endDate': '1757170800000', 'state': 'Toss', 'status': 'Zimbabwe opt to bowl', 'team1': {'teamId': 12, 'teamName': 'Zimbabwe', 'teamSName': 'ZIM', 'imageId': 172127}, 'team2': {'teamId': 5, 'teamName': 'Sri Lanka', 'teamSName': 'SL', 'imageId': 172119}, 'venueInfo': {'id': 69, 'ground': 'Harare Sports Club', 'city': 'Harare', 'timezone': '+02:00', 'latitude': '-17.814114', 'longitude': '31.050962'}, 'seriesStartDt': '1756339200000', 'seriesEndDt': '1757289600000', 'isTimeAnnounced': True, 'stateTitle': 'Toss'}}]}}]}, {'matchType': 'Domestic', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matches': [{'matchInfo': {'matchId': 123677, 'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matchDesc': '2nd Semi-Final', 'matchFormat': 'TEST', 'startDate': '1756958400000', 'endDate': '1757242800000', 'state': 'In Progress', 'status': 'Day 3: 3rd Session - Central Zone lead by 54 runs', 'team1': {'teamId': 234, 'teamName': 'West Zone', 'teamSName': 'WZONE', 'imageId': 172287}, 'team2': {'teamId': 237, 'teamName': 'Central Zone', 'teamSName': 'CZONE', 'imageId': 172290}, 'venueInfo': {'id': 1438102, 'ground': 'BCCI Centre of Excellence Ground B', 'city': 'Bengaluru', 'timezone': '+05:30', 'latitude': '13.174092', 'longitude': '77.706999'}, 'currBatTeamId': 237, 'seriesStartDt': '1756252800000', 'seriesEndDt': '1757980800000', 'isTimeAnnounced': True, 'stateTitle': 'In Progress'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 438, 'wickets': 10, 'overs': 108.0}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 492, 'wickets': 6, 'overs': 138.2}}}}, {'matchInfo': {'matchId': 123672, 'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matchDesc': '1st Semi-Final', 'matchFormat': 'TEST', 'startDate': '1756958400000', 'endDate': '1757242800000', 'state': 'In Progress', 'status': 'Day 3: 3rd Session - North Zone trail by 302 runs', 'team1': {'teamId': 236, 'teamName': 'South Zone', 'teamSName': 'SZONE', 'imageId': 172289}, 'team2': {'teamId': 233, 'teamName': 'North Zone', 'teamSName': 'NZONE', 'imageId': 172286}, 'venueInfo': {'id': 1438087, 'ground': 'BCCI Centre of Excellence Ground', 'city': 'Bengaluru', 'timezone': '+05:30', 'latitude': '12.978853', 'longitude': '77.599533'}, 'currBatTeamId': 233, 'seriesStartDt': '1756252800000', 'seriesEndDt': '1757980800000', 'isTimeAnnounced': True, 'stateTitle': 'In Progress'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 536, 'wickets': 10, 'overs': 169.2}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 234, 'wickets': 3, 'overs': 66.2}}}}]}}]}, {'matchType': 'Women', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10697, 'seriesName': 'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025', 'matches': [{'matchInfo': {'matchId': 131664, 'seriesId': 10697, 'seriesName': 'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025', 'matchDesc': '3rd place play-off', 'matchFormat': 'T20', 'startDate': '1757143800000', 'endDate': '1757156400000', 'state': 'Innings Break', 'status': 'Innings Break', 'team1': {'teamId': 483, 'teamName': 'Tanzania Women', 'teamSName': 'TANW', 'imageId': 172531}, 'team2': {'teamId': 448, 'teamName': 'Uganda Women', 'teamSName': 'UGAW', 'imageId': 172496}, 'venueInfo': {'id': 1438021, 'ground': 'Namibia Cricket Ground', 'city': ' Windhoek', 'timezone': '+02:00', 'latitude': '-22.5872377', 'longitude': '17.0677249'}, 'currBatTeamId': 483, 'seriesStartDt': '1756512000000', 'seriesEndDt': '1757203200000', 'isTimeAnnounced': True, 'stateTitle': 'Ings Break'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 109, 'wickets': 5, 'overs': 19.6}}}}]}}]}], 'filters': {'matchType': ['International', 'League', 'Domestic', 'Women']}, 'appIndex': {'seoTitle': 'Live Cricket Score - Scorecard and Match Results', 'webURL': 'www.cricbuzz.com/live-cricket-scores/'}, 'responseLastUpdated': '1757157603'}

    matches_list = []
    team1_scores_list = []
    team2_scores_list = []
    series_name_list = []
    match_state_list = []
    match_status_list = []
    match_venue_list = []
    match_format_list = []
    match_id_list = []
    team1_list = []
    team2_list = []

    for type_match in data['typeMatches']:

        for series in type_match['seriesMatches']:
            if "seriesAdWrapper" not in series:
                continue  

            series_data = series['seriesAdWrapper']

            for match in series_data['matches']:
                info = match['matchInfo']
                score = match.get('matchScore', {}) 

                #Appending Details in list
                mt = f"{info['team1']['teamName']} vs {info['team2']['teamName']}"
                matches_list.append(mt)
                format = info.get('matchFormat')
                match_format_list.append(format)
                venue = f"{info['venueInfo']['ground']} - {info['venueInfo']['city']}"
                match_venue_list.append(venue)
                state = info.get('state')
                match_state_list.append(state)
                status = info.get('status')
                match_status_list.append(status)
                series_name = info.get('seriesName')
                series_name_list.append(series_name)
                id = info.get('matchId')
                match_id_list.append(id)
                team1 = info['team1']['teamName']
                team1_list.append(team1)
                team2 = info['team2']['teamName']
                team2_list.append(team2)

                # Team 1 score (if available)
                if 'team1Score' in score:
                    inngs1 = score['team1Score'].get('inngs1', {})
                                
                    #Getting Scores list
                    t1 = f"{inngs1.get('runs', '-')} - {inngs1.get('wickets', '-')} in {inngs1.get('overs', '-')} overs"
                    team1_scores_list.append(t1)

                else:
                    t1 = f"Yet to Play"
                    team1_scores_list.append(t1)

                # Team 2 score (if available)
                if 'team2Score' in score:
                    inngs1 = score['team2Score'].get('inngs1', {})
                    
                    t2 = f"{inngs1.get('runs', '-')} - {inngs1.get('wickets', '-')} in {inngs1.get('overs', '-')} overs"
                    team2_scores_list.append(t2)

                else:
                    t2 = f"Yet to Play"
                    team2_scores_list.append(t2)


    options = st.selectbox("Select the Match", matches_list, key="live_matches")
    index = matches_list.index(options)

    #Reading Scorecard API
    url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{match_id_list[index]}/hscard"

    headers = {
        "x-rapidapi-key": "4879a17e0cmsh37b379d4ab14552p161d4djsncf56613e28e8",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    #Remove comment line below for live execution
    # response = requests.get(url, headers=headers)
    # data2 = response.json()
    #Add comment line below for live execution
    data2 = {'scoreCard': [{'matchId': 122968, 'inningsId': 1, 'timeScore': 1757162903000, 'batTeamDetails': {'batTeamId': 5, 'batTeamName': 'Sri Lanka', 'batTeamShortName': 'SL', 'batsmenData': {'bat_1': {'batId': 13682, 'batName': 'Pathum Nissanka', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 8, 'balls': 8, 'dots': 0, 'fours': 1, 'sixes': 0, 'mins': 0, 'strikeRate': 100.0, 'outDesc': 'c Munyonga b Brad Evans', 'bowlerId': 19592, 'fielderId1': 14800, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 1, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_2': {'batId': 9494, 'batName': 'Kusal Mendis', 'batShortName': '', 'isCaptain': False, 'isKeeper': True, 'runs': 1, 'balls': 3, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 33.33, 'outDesc': 'c Ngarava b Muzarabani', 'bowlerId': 13316, 'fielderId1': 11229, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_3': {'batId': 13886, 'batName': 'Kamil Mishara', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 20, 'balls': 20, 'dots': 0, 'fours': 4, 'sixes': 0, 'mins': 0, 'strikeRate': 100.0, 'outDesc': 'b Brad Evans', 'bowlerId': 19592, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 4, 'sixers': 0, 'wicketCode': 'BOWLED', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': 'IN'}, 'bat_4': {'batId': 13187, 'batName': 'Nuwanidu Fernando', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 1, 'balls': 3, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 33.33, 'outDesc': 'c Raza b Muzarabani', 'bowlerId': 13316, 'fielderId1': 9354, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_5': {'batId': 10934, 'batName': 'Asalanka', 'batShortName': '', 'isCaptain': True, 'isKeeper': False, 'runs': 18, 'balls': 23, 'dots': 0, 'fours': 1, 'sixes': 0, 'mins': 0, 'strikeRate': 78.26, 'outDesc': 'b Raza', 'bowlerId': 9354, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 1, 'sixers': 0, 'wicketCode': 'BOWLED', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_6': {'batId': 10940, 'batName': 'Kamindu Mendis', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 4, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': 'lbw b Raza', 'bowlerId': 9354, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'LBW', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_7': {'batId': 8422, 'batName': 'Shanaka', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 15, 'balls': 21, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 71.43, 'outDesc': 'c Tinotenda Maposa b Sean Williams', 'bowlerId': 441, 'fielderId1': 47311, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_8': {'batId': 35640, 'batName': 'Dushan Hemantha', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 7, 'balls': 10, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 70.0, 'outDesc': 'run out (Tinotenda Maposa/T Marumani)', 'bowlerId': 0, 'fielderId1': 15877, 'fielderId2': 15877, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'RUNOUT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_9': {'batId': 8393, 'batName': 'Chameera', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 2, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': 'lbw b Raza', 'bowlerId': 9354, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'LBW', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_10': {'batId': 18504, 'batName': 'M Theekshana', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 6, 'balls': 12, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 50.0, 'outDesc': 'c Raza b Brad Evans', 'bowlerId': 19592, 'fielderId1': 9354, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_11': {'batId': 9498, 'batName': 'B Fernando', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 1, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': 'not out', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': 'IN'}}}, 'bowlTeamDetails': {'bowlTeamId': 12, 'bowlTeamName': 'Zimbabwe', 'bowlTeamShortName': 'ZIM', 'bowlersData': {'bowl_4': {'bowlerId': 9354, 'bowlName': 'Raza', 'bowlShortName': '', 'isCaptain': True, 'isKeeper': False, 'overs': 4.0, 'maidens': 0, 'runs': 11, 'wickets': 3, 'economy': 2.8, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 40, 'runsPerBall': 0.28, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_3': {'bowlerId': 19592, 'bowlName': 'Brad Evans', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 2.4, 'maidens': 0, 'runs': 15, 'wickets': 3, 'economy': 5.6, 'no_balls': 1, 'wides': 0, 'dots': 0, 'balls': 24, 'runsPerBall': 0.63, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_6': {'bowlerId': 441, 'bowlName': 'Sean Williams', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 4.0, 'maidens': 0, 'runs': 19, 'wickets': 1, 'economy': 4.8, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 40, 'runsPerBall': 0.48, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_5': {'bowlerId': 47311, 'bowlName': 'Tinotenda Maposa', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 2.0, 'maidens': 0, 'runs': 7, 'wickets': 0, 'economy': 3.5, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 20, 'runsPerBall': 0.35, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_2': {'bowlerId': 13316, 'bowlName': 'Muzarabani', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 3.0, 'maidens': 0, 'runs': 14, 'wickets': 2, 'economy': 4.7, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 30, 'runsPerBall': 0.47, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_1': {'bowlerId': 11229, 'bowlName': 'Ngarava', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 2.0, 'maidens': 0, 'runs': 11, 'wickets': 0, 'economy': 5.5, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 20, 'runsPerBall': 0.55, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}}}, 'scoreDetails': {'ballNbr': 106, 'isDeclared': False, 'isFollowOn': False, 'overs': 17.4, 'revisedOvers': 0.0, 'runRate': 4.53, 'runs': 80, 'wickets': 10, 'runsPerBall': 0.46}, 'extrasData': {'noBalls': 1, 'total': 4, 'byes': 1, 'penalty': 0, 'wides': 0, 'legByes': 2}, 'ppData': {}, 'wicketsData': {'wkt_1': {'batId': 9494, 'batName': 'Kusal Mendis', 'wktNbr': 1, 'wktOver': 1.1, 'wktRuns': 4, 'ballNbr': 11}, 'wkt_2': {'batId': 13682, 'batName': 'Pathum Nissanka', 'wktNbr': 2, 'wktOver': 3.3, 'wktRuns': 17, 'ballNbr': 33}, 'wkt_3': {'batId': 13187, 'batName': 'Nuwanidu Fernando', 'wktNbr': 3, 'wktOver': 4.5, 'wktRuns': 24, 'ballNbr': 45}, 'wkt_4': {'batId': 13886, 'batName': 'Kamil Mishara', 'wktNbr': 4, 'wktOver': 5.4, 'wktRuns': 37, 'ballNbr': 54}, 'wkt_5': {'batId': 10940, 'batName': 'Kamindu Mendis', 'wktNbr': 5, 'wktOver': 6.5, 'wktRuns': 38, 'ballNbr': 65}, 'wkt_6': {'batId': 8422, 'batName': 'Shanaka', 'wktNbr': 6, 'wktOver': 12.6, 'wktRuns': 64, 'ballNbr': 126}, 'wkt_7': {'batId': 10934, 'batName': 'Asalanka', 'wktNbr': 7, 'wktOver': 13.3, 'wktRuns': 66, 'ballNbr': 133}, 'wkt_8': {'batId': 8393, 'batName': 'Chameera', 'wktNbr': 8, 'wktOver': 13.5, 'wktRuns': 66, 'ballNbr': 135}, 'wkt_9': {'batId': 35640, 'batName': 'Dushan Hemantha', 'wktNbr': 9, 'wktOver': 17.1, 'wktRuns': 79, 'ballNbr': 171}, 'wkt_10': {'batId': 18504, 'batName': 'M Theekshana', 'wktNbr': 10, 'wktOver': 17.4, 'wktRuns': 80, 'ballNbr': 174}}, 'partnershipsData': {'pat_1': {'bat1Id': 13682, 'bat1Name': 'Nissanka', 'bat1Runs': 3, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 9494, 'bat2Name': 'Kusal Mendis', 'bat2Runs': 1, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 4, 'totalBalls': 7, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_2': {'bat1Id': 13682, 'bat1Name': 'Nissanka', 'bat1Runs': 5, 'bat1fours': 1, 'bat1sixes': 0, 'bat2Id': 13886, 'bat2Name': 'Kamil Mishara', 'bat2Runs': 7, 'bat2fours': 1, 'bat2sixes': 0, 'totalRuns': 13, 'totalBalls': 14, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_3': {'bat1Id': 13187, 'bat1Name': 'Fernando', 'bat1Runs': 1, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 13886, 'bat2Name': 'Kamil Mishara', 'bat2Runs': 5, 'bat2fours': 1, 'bat2sixes': 0, 'totalRuns': 7, 'totalBalls': 8, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_4': {'bat1Id': 10934, 'bat1Name': 'Asalanka', 'bat1Runs': 4, 'bat1fours': 1, 'bat1sixes': 0, 'bat2Id': 13886, 'bat2Name': 'Kamil Mishara', 'bat2Runs': 8, 'bat2fours': 2, 'bat2sixes': 0, 'totalRuns': 13, 'totalBalls': 5, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_5': {'bat1Id': 10934, 'bat1Name': 'Asalanka', 'bat1Runs': 1, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 10940, 'bat2Name': 'Kamindu Mendis', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 1, 'totalBalls': 7, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_6': {'bat1Id': 10934, 'bat1Name': 'Asalanka', 'bat1Runs': 11, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 8422, 'bat2Name': 'Shanaka', 'bat2Runs': 15, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 26, 'totalBalls': 37, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_7': {'bat1Id': 10934, 'bat1Name': 'Asalanka', 'bat1Runs': 2, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 35640, 'bat2Name': 'Hemantha', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 2, 'totalBalls': 3, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_8': {'bat1Id': 8393, 'bat1Name': 'Chameera', 'bat1Runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 35640, 'bat2Name': 'Hemantha', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 0, 'totalBalls': 2, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_9': {'bat1Id': 18504, 'bat1Name': 'Theekshana', 'bat1Runs': 5, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 35640, 'bat2Name': 'Hemantha', 'bat2Runs': 7, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 12, 'totalBalls': 20, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_10': {'bat1Id': 18504, 'bat1Name': 'Theekshana', 'bat1Runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 9498, 'bat2Name': 'Binura Fernando', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 1, 'totalBalls': 3, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}}}, {'matchId': 122968, 'inningsId': 2, 'timeScore': 1757165708000, 'batTeamDetails': {'batTeamId': 12, 'batTeamName': 'Zimbabwe', 'batTeamShortName': 'ZIM', 'batsmenData': {'bat_1': {'batId': 23616, 'batName': 'Brian Bennett', 'batShortName': 'Brian Bennett', 'isCaptain': False, 'isKeeper': False, 'runs': 7, 'balls': 13, 'dots': 7, 'fours': 0, 'sixes': 0, 'mins': 25, 'strikeRate': 53.85, 'outDesc': 'batting', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 5, 'twos': 1, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_2': {'batId': 15877, 'batName': 'Tadiwanashe Marumani', 'batShortName': 'T Marumani', 'isCaptain': False, 'isKeeper': True, 'runs': 17, 'balls': 12, 'dots': 6, 'fours': 3, 'sixes': 0, 'mins': 14, 'strikeRate': 141.67, 'outDesc': 'c Kusal Mendis b Chameera', 'bowlerId': 8393, 'fielderId1': 9494, 'fielderId2': 0, 'fielderId3': 0, 'ones': 2, 'twos': 0, 'threes': 1, 'fives': 0, 'boundaries': 3, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_3': {'batId': 441, 'batName': 'Sean Williams', 'batShortName': 'Sean Williams', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 2, 'dots': 2, 'fours': 0, 'sixes': 0, 'mins': 1, 'strikeRate': 0.0, 'outDesc': 'b Chameera', 'bowlerId': 8393, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'BOWLED', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_4': {'batId': 9354, 'batName': 'Sikandar Raza', 'batShortName': 'Raza', 'isCaptain': True, 'isKeeper': False, 'runs': 2, 'balls': 7, 'dots': 5, 'fours': 0, 'sixes': 0, 'mins': 8, 'strikeRate': 28.57, 'outDesc': 'b Chameera', 'bowlerId': 8393, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 2, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'BOWLED', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_5': {'batId': 8454, 'batName': 'Ryan Burl', 'batShortName': 'Ryan Burl', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_6': {'batId': 47129, 'batName': 'Tashinga Musekiwa', 'batShortName': 'Tashinga Musekiwa', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_7': {'batId': 14800, 'batName': 'Tony Munyonga', 'batShortName': 'Munyonga', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_8': {'batId': 19592, 'batName': 'Brad Evans', 'batShortName': 'Brad Evans', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_9': {'batId': 47311, 'batName': 'Tinotenda Maposa', 'batShortName': 'Tinotenda Maposa', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_10': {'batId': 11229, 'batName': 'Richard Ngarava', 'batShortName': 'Ngarava', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_11': {'batId': 13316, 'batName': 'Blessing Muzarabani', 'batShortName': 'Muzarabani', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}}}, 'bowlTeamDetails': {'bowlTeamId': 5, 'bowlTeamName': 'Sri Lanka', 'bowlTeamShortName': 'SL', 'bowlersData': {'bowl_3': {'bowlerId': 8393, 'bowlName': 'Dushmantha Chameera', 'bowlShortName': 'Chameera', 'isCaptain': False, 'isKeeper': False, 'overs': 1.4, 'maidens': 0, 'runs': 3, 'wickets': 3, 'economy': 1.8, 'no_balls': 0, 'wides': 1, 'dots': 0, 'balls': 14, 'runsPerBall': 0.21, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_2': {'bowlerId': 18504, 'bowlName': 'Maheesh Theekshana', 'bowlShortName': 'M Theekshana', 'isCaptain': False, 'isKeeper': False, 'overs': 2.0, 'maidens': 0, 'runs': 16, 'wickets': 0, 'economy': 8.0, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 20, 'runsPerBall': 0.8, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_1': {'bowlerId': 9498, 'bowlName': 'Binura Fernando', 'bowlShortName': 'B Fernando', 'isCaptain': False, 'isKeeper': False, 'overs': 2.0, 'maidens': 0, 'runs': 8, 'wickets': 0, 'economy': 4.0, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 20, 'runsPerBall': 0.4, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': 'IN'}}}, 'scoreDetails': {'ballNbr': 34, 'isDeclared': False, 'isFollowOn': False, 'overs': 5.4, 'revisedOvers': 0.0, 'runRate': 4.76, 'runs': 27, 'wickets': 3, 'runsPerBall': 0.5}, 'extrasData': {'noBalls': 0, 'total': 1, 'byes': 0, 'penalty': 0, 'wides': 1, 'legByes': 0}, 'ppData': {}, 'wicketsData': {'wkt_1': {'batId': 15877, 'batName': 'Tadiwanashe Marumani', 'wktNbr': 1, 'wktOver': 3.2, 'wktRuns': 20, 'ballNbr': 32}, 'wkt_2': {'batId': 441, 'batName': 'Sean Williams', 'wktNbr': 2, 'wktOver': 3.4, 'wktRuns': 20, 'ballNbr': 34}, 'wkt_3': {'batId': 9354, 'batName': 'Sikandar Raza', 'wktNbr': 3, 'wktOver': 5.4, 'wktRuns': 27, 'ballNbr': 54}}, 'partnershipsData': {'pat_1': {'bat1Id': 23616, 'bat1Name': 'Brian Bennett', 'bat1Runs': 3, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 15877, 'bat2Name': 'Marumani', 'bat2Runs': 17, 'bat2fours': 3, 'bat2sixes': 0, 'totalRuns': 20, 'totalBalls': 20, 'bat1balls': 8, 'bat2balls': 12, 'bat1Ones': 3, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 2, 'bat2Twos': 0, 'bat2Threes': 1, 'bat2Fives': 0, 'bat2Boundaries': 3, 'bat2Sixers': 0}, 'pat_2': {'bat1Id': 23616, 'bat1Name': 'Brian Bennett', 'bat1Runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 441, 'bat2Name': 'Williams', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 0, 'totalBalls': 2, 'bat1balls': 0, 'bat2balls': 2, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_3': {'bat1Id': 23616, 'bat1Name': 'Brian Bennett', 'bat1Runs': 4, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 9354, 'bat2Name': 'Raza', 'bat2Runs': 2, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 7, 'totalBalls': 12, 'bat1balls': 5, 'bat2balls': 7, 'bat1Ones': 2, 'bat1Twos': 1, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 2, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}}}], 'matchHeader': {'matchId': 122968, 'matchDescription': '2nd T20I', 'matchFormat': 'HUN', 'matchType': 'International', 'complete': False, 'domestic': False, 'matchStartTimestamp': 1757158200000, 'matchCompleteTimestamp': 1757169000000, 'dayNight': False, 'year': 2025, 'state': 'In Progress', 'status': 'Zimbabwe need 54 runs in 86 balls', 'tossResults': {'tossWinnerId': 12, 'tossWinnerName': 'Zimbabwe', 'decision': 'Bowling'}, 'result': {'winningTeam': '', 'winByRuns': False, 'winByInnings': False}, 'revisedTarget': {'reason': ''}, 'playersOfTheMatch': [], 'playersOfTheSeries': [], 'matchTeamInfo': [{'battingTeamId': 5, 'battingTeamShortName': 'SL', 'bowlingTeamId': 12, 'bowlingTeamShortName': 'ZIM'}, {'battingTeamId': 12, 'battingTeamShortName': 'ZIM', 'bowlingTeamId': 5, 'bowlingTeamShortName': 'SL'}], 'isMatchNotCovered': False, 'team1': {'id': 12, 'name': 'Zimbabwe', 'playerDetails': [], 'shortName': 'ZIM'}, 'team2': {'id': 5, 'name': 'Sri Lanka', 'playerDetails': [], 'shortName': 'SL'}, 'seriesDesc': 'Sri Lanka tour of Zimbabwe, 2025', 'seriesId': 10267, 'seriesName': 'Sri Lanka tour of Zimbabwe, 2025', 'alertType': 'auto', 'livestreamEnabled': False}, 'isMatchComplete': False, 'status': 'Zimbabwe need 54 runs in 86 balls', 'videos': [], 'responseLastUpdated': 1757165759}
    # data2 = response.json()

    #Showing Live Match Details
    st.header(options)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div style="padding:15px; border-radius:10px; background-color:#f0faff;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom:10px;">
                <p><b>🏷️ Match ID:</b> {match_id_list[index]}</p>
                <p><b>🏏 Team 1:</b> {team1_list[index]}</p>
                <p><b>🏏 Team 2:</b> {team2_list[index]}</p>
                <p><b>📋 Format:</b> {match_format_list[index]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style="padding:15px; border-radius:10px; background-color:#f0faff;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom:10px;">
                <p><b>📌 Status:</b> {match_status_list[index]}</p>
                <p><b>🛑 State:</b> {match_state_list[index]}</p>
                <p><b>🏟️ Venue:</b> {match_venue_list[index]}</p>
                <p><b>🔢 Team 1 Score:</b> {team1_scores_list[index]}</p>
                <p><b>🔢 Team 2 Score:</b> {team2_scores_list[index]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


    batting_details = []
    bowling_details = []

    for innings in data2['scoreCard']:
        # Batting Data
        bat_team = innings["batTeamDetails"]["batsmenData"]
        bat_column = ['Batsmen','Runs','Balls','4s','6s','Strike Rate','Out / Not Out']
        bat_df = pd.DataFrame(bat_team.values())
        bat_df = bat_df[['batName','runs','balls','fours','sixes','strikeRate','outDesc',]]
        bat_df.columns = bat_column
        batting_details.append(bat_df)
        #Bowling Data
        bowl_team = innings["bowlTeamDetails"]["bowlersData"]
        bowl_column = ['Bowler','Overs','Maidens','Runs','Wickets','Economy']
        bowl_df = pd.DataFrame(bowl_team.values())
        bowl_df = bowl_df[['bowlName','overs','maidens','runs','wickets','economy']]
        bowl_df.columns = bowl_column
        bowling_details.append(bowl_df)

    st.header("Scorecard")
    tabs = st.tabs([f"Innings {i+1}" for i in range(len(batting_details))])

    for i, tab in enumerate(tabs):
        with tab:
            st.subheader(f"🏏 Innings {i+1} - Batting")
            st.dataframe(batting_details[i], hide_index=True)
            st.subheader(f"🎯 Innings {i+1} - Bowling")
            st.dataframe(bowling_details[i], hide_index=True)

except Exception as e:
    st.info("No Live Matches Found. Showing the recent matches.")


    try:
        st.subheader("Displaying recent cricket scores from CricBuzz.")
        #Recent Matches API
        url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

        headers = {
            "x-rapidapi-key": "4879a17e0cmsh37b379d4ab14552p161d4djsncf56613e28e8",
            "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
        }

        #Remove comment in below line for live execution
        # response = requests.get(url, headers=headers)
        # response.raise_for_status()
        # data = response.json()

        #Add comment line below for live execution
        data = {'typeMatches': [{'matchType': 'International', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10267, 'seriesName': 'Sri Lanka tour of Zimbabwe, 2025', 'matches': [{'matchInfo': {'matchId': 122968, 'seriesId': 10267, 'seriesName': 'Sri Lanka tour of Zimbabwe, 2025', 'matchDesc': '2nd T20I', 'matchFormat': 'T20', 'startDate': '1757158200000', 'endDate': '1757170800000', 'state': 'Toss', 'status': 'Zimbabwe opt to bowl', 'team1': {'teamId': 12, 'teamName': 'Zimbabwe', 'teamSName': 'ZIM', 'imageId': 172127}, 'team2': {'teamId': 5, 'teamName': 'Sri Lanka', 'teamSName': 'SL', 'imageId': 172119}, 'venueInfo': {'id': 69, 'ground': 'Harare Sports Club', 'city': 'Harare', 'timezone': '+02:00', 'latitude': '-17.814114', 'longitude': '31.050962'}, 'seriesStartDt': '1756339200000', 'seriesEndDt': '1757289600000', 'isTimeAnnounced': True, 'stateTitle': 'Toss'}}]}}]}, {'matchType': 'Domestic', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matches': [{'matchInfo': {'matchId': 123677, 'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matchDesc': '2nd Semi-Final', 'matchFormat': 'TEST', 'startDate': '1756958400000', 'endDate': '1757242800000', 'state': 'In Progress', 'status': 'Day 3: 3rd Session - Central Zone lead by 54 runs', 'team1': {'teamId': 234, 'teamName': 'West Zone', 'teamSName': 'WZONE', 'imageId': 172287}, 'team2': {'teamId': 237, 'teamName': 'Central Zone', 'teamSName': 'CZONE', 'imageId': 172290}, 'venueInfo': {'id': 1438102, 'ground': 'BCCI Centre of Excellence Ground B', 'city': 'Bengaluru', 'timezone': '+05:30', 'latitude': '13.174092', 'longitude': '77.706999'}, 'currBatTeamId': 237, 'seriesStartDt': '1756252800000', 'seriesEndDt': '1757980800000', 'isTimeAnnounced': True, 'stateTitle': 'In Progress'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 438, 'wickets': 10, 'overs': 108.0}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 492, 'wickets': 6, 'overs': 138.2}}}}, {'matchInfo': {'matchId': 123672, 'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matchDesc': '1st Semi-Final', 'matchFormat': 'TEST', 'startDate': '1756958400000', 'endDate': '1757242800000', 'state': 'In Progress', 'status': 'Day 3: 3rd Session - North Zone trail by 302 runs', 'team1': {'teamId': 236, 'teamName': 'South Zone', 'teamSName': 'SZONE', 'imageId': 172289}, 'team2': {'teamId': 233, 'teamName': 'North Zone', 'teamSName': 'NZONE', 'imageId': 172286}, 'venueInfo': {'id': 1438087, 'ground': 'BCCI Centre of Excellence Ground', 'city': 'Bengaluru', 'timezone': '+05:30', 'latitude': '12.978853', 'longitude': '77.599533'}, 'currBatTeamId': 233, 'seriesStartDt': '1756252800000', 'seriesEndDt': '1757980800000', 'isTimeAnnounced': True, 'stateTitle': 'In Progress'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 536, 'wickets': 10, 'overs': 169.2}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 234, 'wickets': 3, 'overs': 66.2}}}}]}}]}, {'matchType': 'Women', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10697, 'seriesName': 'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025', 'matches': [{'matchInfo': {'matchId': 131664, 'seriesId': 10697, 'seriesName': 'ICC Womens T20 World Cup Africa Region Division One Qualifier 2025', 'matchDesc': '3rd place play-off', 'matchFormat': 'T20', 'startDate': '1757143800000', 'endDate': '1757156400000', 'state': 'Innings Break', 'status': 'Innings Break', 'team1': {'teamId': 483, 'teamName': 'Tanzania Women', 'teamSName': 'TANW', 'imageId': 172531}, 'team2': {'teamId': 448, 'teamName': 'Uganda Women', 'teamSName': 'UGAW', 'imageId': 172496}, 'venueInfo': {'id': 1438021, 'ground': 'Namibia Cricket Ground', 'city': ' Windhoek', 'timezone': '+02:00', 'latitude': '-22.5872377', 'longitude': '17.0677249'}, 'currBatTeamId': 483, 'seriesStartDt': '1756512000000', 'seriesEndDt': '1757203200000', 'isTimeAnnounced': True, 'stateTitle': 'Ings Break'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 109, 'wickets': 5, 'overs': 19.6}}}}]}}]}], 'filters': {'matchType': ['International', 'League', 'Domestic', 'Women']}, 'appIndex': {'seoTitle': 'Live Cricket Score - Scorecard and Match Results', 'webURL': 'www.cricbuzz.com/live-cricket-scores/'}, 'responseLastUpdated': '1757157603'}

        matches_list = []
        team1_scores_list = []
        team2_scores_list = []
        series_name_list = []
        match_state_list = []
        match_status_list = []
        match_venue_list = []
        match_format_list = []
        match_id_list = []
        team1_list = []
        team2_list = []

        for type_match in data['typeMatches']:

            for series in type_match['seriesMatches']:
                if "seriesAdWrapper" not in series:
                    continue  

                series_data = series['seriesAdWrapper']

                for match in series_data['matches']:
                    info = match['matchInfo']
                    score = match.get('matchScore', {}) 

                    #Appending Details in list
                    mt = f"{info['team1']['teamName']} vs {info['team2']['teamName']}"
                    matches_list.append(mt)
                    format = info.get('matchFormat')
                    match_format_list.append(format)
                    venue = f"{info['venueInfo']['ground']} - {info['venueInfo']['city']}"
                    match_venue_list.append(venue)
                    state = info.get('state')
                    match_state_list.append(state)
                    status = info.get('status')
                    match_status_list.append(status)
                    series_name = info.get('seriesName')
                    series_name_list.append(series_name)
                    id = info.get('matchId')
                    match_id_list.append(id)
                    team1 = info['team1']['teamName']
                    team1_list.append(team1)
                    team2 = info['team2']['teamName']
                    team2_list.append(team2)

                    # Team 1 score (if available)
                    if 'team1Score' in score:
                        inngs1 = score['team1Score'].get('inngs1', {})
                                    
                        #Getting Scores list
                        t1 = f"{inngs1.get('runs', '-')} - {inngs1.get('wickets', '-')} in {inngs1.get('overs', '-')} overs"
                        team1_scores_list.append(t1)

                    else:
                        t1 = f"Yet to Play"
                        team1_scores_list.append(t1)

                    # Team 2 score (if available)
                    if 'team2Score' in score:
                        inngs1 = score['team2Score'].get('inngs1', {})
                        
                        t2 = f"{inngs1.get('runs', '-')} - {inngs1.get('wickets', '-')} in {inngs1.get('overs', '-')} overs"
                        team2_scores_list.append(t2)

                    else:
                        t2 = f"Yet to Play"
                        team2_scores_list.append(t2)


        options = st.selectbox("Select the Match", matches_list, key="recent_matches")
        index = matches_list.index(options)

        #Reading Scorecard API
        url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{match_id_list[index]}/hscard"

        headers = {
            "x-rapidapi-key": "4879a17e0cmsh37b379d4ab14552p161d4djsncf56613e28e8",
            "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
        }

        #Remove comment line below for live execution
        # response = requests.get(url, headers=headers)
        # data2 = response.json()
        #Add comment line below for live execution
        data2 = {'scoreCard': [{'matchId': 122968, 'inningsId': 1, 'timeScore': 1757162903000, 'batTeamDetails': {'batTeamId': 5, 'batTeamName': 'Sri Lanka', 'batTeamShortName': 'SL', 'batsmenData': {'bat_1': {'batId': 13682, 'batName': 'Pathum Nissanka', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 8, 'balls': 8, 'dots': 0, 'fours': 1, 'sixes': 0, 'mins': 0, 'strikeRate': 100.0, 'outDesc': 'c Munyonga b Brad Evans', 'bowlerId': 19592, 'fielderId1': 14800, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 1, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_2': {'batId': 9494, 'batName': 'Kusal Mendis', 'batShortName': '', 'isCaptain': False, 'isKeeper': True, 'runs': 1, 'balls': 3, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 33.33, 'outDesc': 'c Ngarava b Muzarabani', 'bowlerId': 13316, 'fielderId1': 11229, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_3': {'batId': 13886, 'batName': 'Kamil Mishara', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 20, 'balls': 20, 'dots': 0, 'fours': 4, 'sixes': 0, 'mins': 0, 'strikeRate': 100.0, 'outDesc': 'b Brad Evans', 'bowlerId': 19592, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 4, 'sixers': 0, 'wicketCode': 'BOWLED', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': 'IN'}, 'bat_4': {'batId': 13187, 'batName': 'Nuwanidu Fernando', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 1, 'balls': 3, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 33.33, 'outDesc': 'c Raza b Muzarabani', 'bowlerId': 13316, 'fielderId1': 9354, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_5': {'batId': 10934, 'batName': 'Asalanka', 'batShortName': '', 'isCaptain': True, 'isKeeper': False, 'runs': 18, 'balls': 23, 'dots': 0, 'fours': 1, 'sixes': 0, 'mins': 0, 'strikeRate': 78.26, 'outDesc': 'b Raza', 'bowlerId': 9354, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 1, 'sixers': 0, 'wicketCode': 'BOWLED', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_6': {'batId': 10940, 'batName': 'Kamindu Mendis', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 4, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': 'lbw b Raza', 'bowlerId': 9354, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'LBW', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_7': {'batId': 8422, 'batName': 'Shanaka', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 15, 'balls': 21, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 71.43, 'outDesc': 'c Tinotenda Maposa b Sean Williams', 'bowlerId': 441, 'fielderId1': 47311, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_8': {'batId': 35640, 'batName': 'Dushan Hemantha', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 7, 'balls': 10, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 70.0, 'outDesc': 'run out (Tinotenda Maposa/T Marumani)', 'bowlerId': 0, 'fielderId1': 15877, 'fielderId2': 15877, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'RUNOUT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_9': {'batId': 8393, 'batName': 'Chameera', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 2, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': 'lbw b Raza', 'bowlerId': 9354, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'LBW', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_10': {'batId': 18504, 'batName': 'M Theekshana', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 6, 'balls': 12, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 50.0, 'outDesc': 'c Raza b Brad Evans', 'bowlerId': 19592, 'fielderId1': 9354, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_11': {'batId': 9498, 'batName': 'B Fernando', 'batShortName': '', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 1, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': 'not out', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': 'IN'}}}, 'bowlTeamDetails': {'bowlTeamId': 12, 'bowlTeamName': 'Zimbabwe', 'bowlTeamShortName': 'ZIM', 'bowlersData': {'bowl_4': {'bowlerId': 9354, 'bowlName': 'Raza', 'bowlShortName': '', 'isCaptain': True, 'isKeeper': False, 'overs': 4.0, 'maidens': 0, 'runs': 11, 'wickets': 3, 'economy': 2.8, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 40, 'runsPerBall': 0.28, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_3': {'bowlerId': 19592, 'bowlName': 'Brad Evans', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 2.4, 'maidens': 0, 'runs': 15, 'wickets': 3, 'economy': 5.6, 'no_balls': 1, 'wides': 0, 'dots': 0, 'balls': 24, 'runsPerBall': 0.63, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_6': {'bowlerId': 441, 'bowlName': 'Sean Williams', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 4.0, 'maidens': 0, 'runs': 19, 'wickets': 1, 'economy': 4.8, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 40, 'runsPerBall': 0.48, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_5': {'bowlerId': 47311, 'bowlName': 'Tinotenda Maposa', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 2.0, 'maidens': 0, 'runs': 7, 'wickets': 0, 'economy': 3.5, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 20, 'runsPerBall': 0.35, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_2': {'bowlerId': 13316, 'bowlName': 'Muzarabani', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 3.0, 'maidens': 0, 'runs': 14, 'wickets': 2, 'economy': 4.7, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 30, 'runsPerBall': 0.47, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_1': {'bowlerId': 11229, 'bowlName': 'Ngarava', 'bowlShortName': '', 'isCaptain': False, 'isKeeper': False, 'overs': 2.0, 'maidens': 0, 'runs': 11, 'wickets': 0, 'economy': 5.5, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 20, 'runsPerBall': 0.55, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}}}, 'scoreDetails': {'ballNbr': 106, 'isDeclared': False, 'isFollowOn': False, 'overs': 17.4, 'revisedOvers': 0.0, 'runRate': 4.53, 'runs': 80, 'wickets': 10, 'runsPerBall': 0.46}, 'extrasData': {'noBalls': 1, 'total': 4, 'byes': 1, 'penalty': 0, 'wides': 0, 'legByes': 2}, 'ppData': {}, 'wicketsData': {'wkt_1': {'batId': 9494, 'batName': 'Kusal Mendis', 'wktNbr': 1, 'wktOver': 1.1, 'wktRuns': 4, 'ballNbr': 11}, 'wkt_2': {'batId': 13682, 'batName': 'Pathum Nissanka', 'wktNbr': 2, 'wktOver': 3.3, 'wktRuns': 17, 'ballNbr': 33}, 'wkt_3': {'batId': 13187, 'batName': 'Nuwanidu Fernando', 'wktNbr': 3, 'wktOver': 4.5, 'wktRuns': 24, 'ballNbr': 45}, 'wkt_4': {'batId': 13886, 'batName': 'Kamil Mishara', 'wktNbr': 4, 'wktOver': 5.4, 'wktRuns': 37, 'ballNbr': 54}, 'wkt_5': {'batId': 10940, 'batName': 'Kamindu Mendis', 'wktNbr': 5, 'wktOver': 6.5, 'wktRuns': 38, 'ballNbr': 65}, 'wkt_6': {'batId': 8422, 'batName': 'Shanaka', 'wktNbr': 6, 'wktOver': 12.6, 'wktRuns': 64, 'ballNbr': 126}, 'wkt_7': {'batId': 10934, 'batName': 'Asalanka', 'wktNbr': 7, 'wktOver': 13.3, 'wktRuns': 66, 'ballNbr': 133}, 'wkt_8': {'batId': 8393, 'batName': 'Chameera', 'wktNbr': 8, 'wktOver': 13.5, 'wktRuns': 66, 'ballNbr': 135}, 'wkt_9': {'batId': 35640, 'batName': 'Dushan Hemantha', 'wktNbr': 9, 'wktOver': 17.1, 'wktRuns': 79, 'ballNbr': 171}, 'wkt_10': {'batId': 18504, 'batName': 'M Theekshana', 'wktNbr': 10, 'wktOver': 17.4, 'wktRuns': 80, 'ballNbr': 174}}, 'partnershipsData': {'pat_1': {'bat1Id': 13682, 'bat1Name': 'Nissanka', 'bat1Runs': 3, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 9494, 'bat2Name': 'Kusal Mendis', 'bat2Runs': 1, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 4, 'totalBalls': 7, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_2': {'bat1Id': 13682, 'bat1Name': 'Nissanka', 'bat1Runs': 5, 'bat1fours': 1, 'bat1sixes': 0, 'bat2Id': 13886, 'bat2Name': 'Kamil Mishara', 'bat2Runs': 7, 'bat2fours': 1, 'bat2sixes': 0, 'totalRuns': 13, 'totalBalls': 14, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_3': {'bat1Id': 13187, 'bat1Name': 'Fernando', 'bat1Runs': 1, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 13886, 'bat2Name': 'Kamil Mishara', 'bat2Runs': 5, 'bat2fours': 1, 'bat2sixes': 0, 'totalRuns': 7, 'totalBalls': 8, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_4': {'bat1Id': 10934, 'bat1Name': 'Asalanka', 'bat1Runs': 4, 'bat1fours': 1, 'bat1sixes': 0, 'bat2Id': 13886, 'bat2Name': 'Kamil Mishara', 'bat2Runs': 8, 'bat2fours': 2, 'bat2sixes': 0, 'totalRuns': 13, 'totalBalls': 5, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_5': {'bat1Id': 10934, 'bat1Name': 'Asalanka', 'bat1Runs': 1, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 10940, 'bat2Name': 'Kamindu Mendis', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 1, 'totalBalls': 7, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_6': {'bat1Id': 10934, 'bat1Name': 'Asalanka', 'bat1Runs': 11, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 8422, 'bat2Name': 'Shanaka', 'bat2Runs': 15, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 26, 'totalBalls': 37, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_7': {'bat1Id': 10934, 'bat1Name': 'Asalanka', 'bat1Runs': 2, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 35640, 'bat2Name': 'Hemantha', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 2, 'totalBalls': 3, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_8': {'bat1Id': 8393, 'bat1Name': 'Chameera', 'bat1Runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 35640, 'bat2Name': 'Hemantha', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 0, 'totalBalls': 2, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_9': {'bat1Id': 18504, 'bat1Name': 'Theekshana', 'bat1Runs': 5, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 35640, 'bat2Name': 'Hemantha', 'bat2Runs': 7, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 12, 'totalBalls': 20, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_10': {'bat1Id': 18504, 'bat1Name': 'Theekshana', 'bat1Runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 9498, 'bat2Name': 'Binura Fernando', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 1, 'totalBalls': 3, 'bat1balls': 0, 'bat2balls': 0, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}}}, {'matchId': 122968, 'inningsId': 2, 'timeScore': 1757165708000, 'batTeamDetails': {'batTeamId': 12, 'batTeamName': 'Zimbabwe', 'batTeamShortName': 'ZIM', 'batsmenData': {'bat_1': {'batId': 23616, 'batName': 'Brian Bennett', 'batShortName': 'Brian Bennett', 'isCaptain': False, 'isKeeper': False, 'runs': 7, 'balls': 13, 'dots': 7, 'fours': 0, 'sixes': 0, 'mins': 25, 'strikeRate': 53.85, 'outDesc': 'batting', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 5, 'twos': 1, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_2': {'batId': 15877, 'batName': 'Tadiwanashe Marumani', 'batShortName': 'T Marumani', 'isCaptain': False, 'isKeeper': True, 'runs': 17, 'balls': 12, 'dots': 6, 'fours': 3, 'sixes': 0, 'mins': 14, 'strikeRate': 141.67, 'outDesc': 'c Kusal Mendis b Chameera', 'bowlerId': 8393, 'fielderId1': 9494, 'fielderId2': 0, 'fielderId3': 0, 'ones': 2, 'twos': 0, 'threes': 1, 'fives': 0, 'boundaries': 3, 'sixers': 0, 'wicketCode': 'CAUGHT', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_3': {'batId': 441, 'batName': 'Sean Williams', 'batShortName': 'Sean Williams', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 2, 'dots': 2, 'fours': 0, 'sixes': 0, 'mins': 1, 'strikeRate': 0.0, 'outDesc': 'b Chameera', 'bowlerId': 8393, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'BOWLED', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_4': {'batId': 9354, 'batName': 'Sikandar Raza', 'batShortName': 'Raza', 'isCaptain': True, 'isKeeper': False, 'runs': 2, 'balls': 7, 'dots': 5, 'fours': 0, 'sixes': 0, 'mins': 8, 'strikeRate': 28.57, 'outDesc': 'b Chameera', 'bowlerId': 8393, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 2, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': 'BOWLED', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_5': {'batId': 8454, 'batName': 'Ryan Burl', 'batShortName': 'Ryan Burl', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_6': {'batId': 47129, 'batName': 'Tashinga Musekiwa', 'batShortName': 'Tashinga Musekiwa', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_7': {'batId': 14800, 'batName': 'Tony Munyonga', 'batShortName': 'Munyonga', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_8': {'batId': 19592, 'batName': 'Brad Evans', 'batShortName': 'Brad Evans', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_9': {'batId': 47311, 'batName': 'Tinotenda Maposa', 'batShortName': 'Tinotenda Maposa', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_10': {'batId': 11229, 'batName': 'Richard Ngarava', 'batShortName': 'Ngarava', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bat_11': {'batId': 13316, 'batName': 'Blessing Muzarabani', 'batShortName': 'Muzarabani', 'isCaptain': False, 'isKeeper': False, 'runs': 0, 'balls': 0, 'dots': 0, 'fours': 0, 'sixes': 0, 'mins': 0, 'strikeRate': 0.0, 'outDesc': '', 'bowlerId': 0, 'fielderId1': 0, 'fielderId2': 0, 'fielderId3': 0, 'ones': 0, 'twos': 0, 'threes': 0, 'fives': 0, 'boundaries': 0, 'sixers': 0, 'wicketCode': '', 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}}}, 'bowlTeamDetails': {'bowlTeamId': 5, 'bowlTeamName': 'Sri Lanka', 'bowlTeamShortName': 'SL', 'bowlersData': {'bowl_3': {'bowlerId': 8393, 'bowlName': 'Dushmantha Chameera', 'bowlShortName': 'Chameera', 'isCaptain': False, 'isKeeper': False, 'overs': 1.4, 'maidens': 0, 'runs': 3, 'wickets': 3, 'economy': 1.8, 'no_balls': 0, 'wides': 1, 'dots': 0, 'balls': 14, 'runsPerBall': 0.21, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_2': {'bowlerId': 18504, 'bowlName': 'Maheesh Theekshana', 'bowlShortName': 'M Theekshana', 'isCaptain': False, 'isKeeper': False, 'overs': 2.0, 'maidens': 0, 'runs': 16, 'wickets': 0, 'economy': 8.0, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 20, 'runsPerBall': 0.8, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': ''}, 'bowl_1': {'bowlerId': 9498, 'bowlName': 'Binura Fernando', 'bowlShortName': 'B Fernando', 'isCaptain': False, 'isKeeper': False, 'overs': 2.0, 'maidens': 0, 'runs': 8, 'wickets': 0, 'economy': 4.0, 'no_balls': 0, 'wides': 0, 'dots': 0, 'balls': 20, 'runsPerBall': 0.4, 'isOverseas': False, 'inMatchChange': '', 'playingXIChange': 'IN'}}}, 'scoreDetails': {'ballNbr': 34, 'isDeclared': False, 'isFollowOn': False, 'overs': 5.4, 'revisedOvers': 0.0, 'runRate': 4.76, 'runs': 27, 'wickets': 3, 'runsPerBall': 0.5}, 'extrasData': {'noBalls': 0, 'total': 1, 'byes': 0, 'penalty': 0, 'wides': 1, 'legByes': 0}, 'ppData': {}, 'wicketsData': {'wkt_1': {'batId': 15877, 'batName': 'Tadiwanashe Marumani', 'wktNbr': 1, 'wktOver': 3.2, 'wktRuns': 20, 'ballNbr': 32}, 'wkt_2': {'batId': 441, 'batName': 'Sean Williams', 'wktNbr': 2, 'wktOver': 3.4, 'wktRuns': 20, 'ballNbr': 34}, 'wkt_3': {'batId': 9354, 'batName': 'Sikandar Raza', 'wktNbr': 3, 'wktOver': 5.4, 'wktRuns': 27, 'ballNbr': 54}}, 'partnershipsData': {'pat_1': {'bat1Id': 23616, 'bat1Name': 'Brian Bennett', 'bat1Runs': 3, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 15877, 'bat2Name': 'Marumani', 'bat2Runs': 17, 'bat2fours': 3, 'bat2sixes': 0, 'totalRuns': 20, 'totalBalls': 20, 'bat1balls': 8, 'bat2balls': 12, 'bat1Ones': 3, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 2, 'bat2Twos': 0, 'bat2Threes': 1, 'bat2Fives': 0, 'bat2Boundaries': 3, 'bat2Sixers': 0}, 'pat_2': {'bat1Id': 23616, 'bat1Name': 'Brian Bennett', 'bat1Runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 441, 'bat2Name': 'Williams', 'bat2Runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 0, 'totalBalls': 2, 'bat1balls': 0, 'bat2balls': 2, 'bat1Ones': 0, 'bat1Twos': 0, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 0, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}, 'pat_3': {'bat1Id': 23616, 'bat1Name': 'Brian Bennett', 'bat1Runs': 4, 'bat1fours': 0, 'bat1sixes': 0, 'bat2Id': 9354, 'bat2Name': 'Raza', 'bat2Runs': 2, 'bat2fours': 0, 'bat2sixes': 0, 'totalRuns': 7, 'totalBalls': 12, 'bat1balls': 5, 'bat2balls': 7, 'bat1Ones': 2, 'bat1Twos': 1, 'bat1Threes': 0, 'bat1Fives': 0, 'bat1Boundaries': 0, 'bat1Sixers': 0, 'bat2Ones': 2, 'bat2Twos': 0, 'bat2Threes': 0, 'bat2Fives': 0, 'bat2Boundaries': 0, 'bat2Sixers': 0}}}], 'matchHeader': {'matchId': 122968, 'matchDescription': '2nd T20I', 'matchFormat': 'HUN', 'matchType': 'International', 'complete': False, 'domestic': False, 'matchStartTimestamp': 1757158200000, 'matchCompleteTimestamp': 1757169000000, 'dayNight': False, 'year': 2025, 'state': 'In Progress', 'status': 'Zimbabwe need 54 runs in 86 balls', 'tossResults': {'tossWinnerId': 12, 'tossWinnerName': 'Zimbabwe', 'decision': 'Bowling'}, 'result': {'winningTeam': '', 'winByRuns': False, 'winByInnings': False}, 'revisedTarget': {'reason': ''}, 'playersOfTheMatch': [], 'playersOfTheSeries': [], 'matchTeamInfo': [{'battingTeamId': 5, 'battingTeamShortName': 'SL', 'bowlingTeamId': 12, 'bowlingTeamShortName': 'ZIM'}, {'battingTeamId': 12, 'battingTeamShortName': 'ZIM', 'bowlingTeamId': 5, 'bowlingTeamShortName': 'SL'}], 'isMatchNotCovered': False, 'team1': {'id': 12, 'name': 'Zimbabwe', 'playerDetails': [], 'shortName': 'ZIM'}, 'team2': {'id': 5, 'name': 'Sri Lanka', 'playerDetails': [], 'shortName': 'SL'}, 'seriesDesc': 'Sri Lanka tour of Zimbabwe, 2025', 'seriesId': 10267, 'seriesName': 'Sri Lanka tour of Zimbabwe, 2025', 'alertType': 'auto', 'livestreamEnabled': False}, 'isMatchComplete': False, 'status': 'Zimbabwe need 54 runs in 86 balls', 'videos': [], 'responseLastUpdated': 1757165759}
        # data2 = response.json()
        #Showing Live Match Details
        st.header(options)
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div style="padding:15px; border-radius:10px; background-color:#f0faff;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom:10px;">
                    <p><b>🏷️ Match ID:</b> {match_id_list[index]}</p>
                    <p><b>🏏 Team 1:</b> {team1_list[index]}</p>
                    <p><b>🏏 Team 2:</b> {team2_list[index]}</p>
                    <p><b>📋 Format:</b> {match_format_list[index]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div style="padding:15px; border-radius:10px; background-color:#f0faff;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom:10px;">
                    <p><b>📌 Status:</b> {match_status_list[index]}</p>
                    <p><b>🛑 State:</b> {match_state_list[index]}</p>
                    <p><b>🏟️ Venue:</b> {match_venue_list[index]}</p>
                    <p><b>🔢 Team 1 Score:</b> {team1_scores_list[index]}</p>
                    <p><b>🔢 Team 2 Score:</b> {team2_scores_list[index]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        batting_details = []
        bowling_details = []

        for innings in data2['scoreCard']:
            # Batting Data
            bat_team = innings["batTeamDetails"]["batsmenData"]
            bat_df = pd.DataFrame(bat_team.values())
            bat_df = bat_df[['batName','runs','balls','fours','sixes','strikeRate','outDesc',]]
            bat_column = ['Batsmen','Runs','Balls','4s','6s','Strike Rate','Out / Not Out']
            bat_df.columns = bat_column
            batting_details.append(bat_df)
            #Bowling Data
            bowl_team = innings["bowlTeamDetails"]["bowlersData"]
            bowl_df = pd.DataFrame(bowl_team.values())
            bowl_df = bowl_df[['bowlName','overs','maidens','runs','wickets','economy']]
            bowl_column = ['Bowler','Overs','Maidens','Runs','Wickets','Economy']
            bowl_df.columns = bowl_column
            bowling_details.append(bowl_df)

        st.header("Scorecard")
        tabs = st.tabs([f"Innings {i+1}" for i in range(len(batting_details))])

        for i, tab in enumerate(tabs):
            with tab:
                st.subheader(f"🏏 Innings {i+1} - Batting")
                st.dataframe(batting_details[i], hide_index=True)

                st.subheader(f"🎯 Innings {i+1} - Bowling")
                st.dataframe(bowling_details[i], hide_index=True)

    
    except Exception as e:
        st.info("No Recent Matches Found. Both API calls failed.")


