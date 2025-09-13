import streamlit as st
import pandas as pd
from utils.db_connection import api_key, api_key2

import requests

st.set_page_config(page_title="CricBuzz App", page_icon="🏏", layout="wide")

st.title("📊Detailed Player Statistics")
st.write("Displaying player statistics from CricBuzz.")

st.write("🔍Enter the player's name to fetch their stats.")
player_name = st.text_input("Player Name:", placeholder="e.g., Virat Kohli")
submit = st.button("Fetch Stats")

#Player search using Name - players/search
url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search"

#name = "Sachin"
querystring = {"plrN":player_name}
headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

#Remove comment line below for live execution--------------------------------------
response = requests.get(url, headers=headers, params=querystring)
searched_data = response.json()

#Comment the below line for live execution--------------------------------------
# searched_data = {'player': [{'id': '13376', 'name': 'Sachin Bhudia', 'teamName': 'Kenya', 'faceImageId': '153979', 'dob': '1998-09-24'}, {'id': '14905', 'name': 'Sachin Mevada ', 'teamName': 'India', 'faceImageId': '169688', 'dob': '1999-04-23'}, {'id': '25', 'name': 'Sachin Tendulkar', 'teamName': 'India', 'faceImageId': '171004', 'dob': '1973-04-24'}, {'id': '1891', 'name': 'Sachin Rana', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1984-09-18'}, {'id': '8709', 'name': 'Sachin Baby', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1988-12-18'}, {'id': '8882', 'name': 'Sachin Chaudhari', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1986-03-27'}, {'id': '9296', 'name': 'Sachin Hooda', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1988-08-27'}, {'id': '9692', 'name': 'Sachin Mohan', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1990-04-10'}, {'id': '10308', 'name': 'Sachin Omprakash Katariya', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1995-04-14'}, {'id': '10602', 'name': 'Sachin Joshi', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1984-08-07'}, {'id': '11409', 'name': 'Audhi Sachin', 'teamName': 'India', 'faceImageId': '182026', 'dob': 'N/A'}, {'id': '11724', 'name': 'Sachin Gankal', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1995-03-28'}, {'id': '11760', 'name': 'Sachin Shinde', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1987-09-29'}, {'id': '11840', 'name': 'Sachin Solanki', 'teamName': 'United Arab Emirates', 'faceImageId': '182026', 'dob': 'N/A'}, {'id': '12378', 'name': 'Sachin Rathi', 'teamName': 'India', 'faceImageId': '182026', 'dob': '2003-11-03'}, {'id': '12917', 'name': 'Sachin Sharma', 'teamName': 'India', 'faceImageId': '182026', 'dob': 'N/A'}, {'id': '13076', 'name': 'Lal Sachin', 'teamName': 'India', 'faceImageId': '182026', 'dob': 'N/A'}, {'id': '13691', 'name': 'Sachintha Peiris', 'teamName': 'Sri Lanka', 'faceImageId': '182026', 'dob': '1995-11-16'}, {'id': '14966', 'name': 'Sachin Madhuker Yadav', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1994-04-07'}, {'id': '15012', 'name': 'Sachin Wagh', 'teamName': 'India', 'faceImageId': '182026', 'dob': 'N/A'}, {'id': '15490', 'name': 'Sachin Kumar', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1997-12-25'}, {'id': '15667', 'name': 'Sachindu Colombage', 'teamName': 'Sri Lanka', 'faceImageId': '182026', 'dob': '1998-02-21'}, {'id': '21793', 'name': 'Sachini Nisansala', 'teamName': 'Sri Lanka', 'faceImageId': '182026', 'dob': '2001-11-10'}, {'id': '26346', 'name': 'Sachin Mandy Gangareddy', 'teamName': 'Germany', 'faceImageId': '182026', 'dob': '1991-06-07'}, {'id': '27039', 'name': 'Sachini Jayasinghe', 'teamName': 'Bahrain', 'faceImageId': '182026', 'dob': '1996-08-22'}, {'id': '28199', 'name': 'Sachin Ganpat Shinde', 'teamName': 'Serbia', 'faceImageId': '182026', 'dob': '1983-11-15'}, {'id': '29480', 'name': 'Sachin Kumar', 'teamName': 'Bahrain', 'faceImageId': '182026', 'dob': '1989-04-03'}, {'id': '34144', 'name': 'Suresh Sachin', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1998-01-02'}, {'id': '46317', 'name': 'Sachin Singh Rathi', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1987-04-30'}, {'id': '46559', 'name': 'Balasubramaniam Sachin', 'teamName': 'India', 'faceImageId': '182026', 'dob': '2003-08-30'}, {'id': '48599', 'name': 'Sachin Parmar', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1999-04-23'}, {'id': '49396', 'name': 'Sachin Kakodia', 'teamName': 'India', 'faceImageId': '182026', 'dob': 'N/A'}, {'id': '49443', 'name': 'Sachin Malav', 'teamName': 'India', 'faceImageId': '182026', 'dob': 'N/A'}, {'id': '49499', 'name': 'Sachin Yadav', 'teamName': 'India', 'faceImageId': '182026', 'dob': '2003-12-29'}, {'id': '51798', 'name': 'Sachin Dhas', 'teamName': 'India', 'faceImageId': '182026', 'dob': '2005-02-03'}, {'id': '52222', 'name': 'Sachin Bhosale', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1998-01-02'}, {'id': '52379', 'name': 'Sachin Sharma', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1993-09-21'}, {'id': '55312', 'name': 'Sachin Banamali', 'teamName': 'Singapore', 'faceImageId': '182026', 'dob': '1989-08-17'}, {'id': '1424248', 'name': 'Sachin Ravikumar', 'teamName': 'Costa Rica', 'faceImageId': '182026', 'dob': '1988-05-27'}, {'id': '1431361', 'name': 'Sachin Gill', 'teamName': 'Kenya', 'faceImageId': '182026', 'dob': '1996-12-04'}, {'id': '1454129', 'name': 'Sachin Pawar', 'teamName': 'India', 'faceImageId': '182026', 'dob': '2007-06-06'}, {'id': '1456754', 'name': 'Sachin B', 'teamName': 'India', 'faceImageId': '182026', 'dob': '2006-08-14'}, {'id': '1460509', 'name': 'Sachin PS', 'teamName': 'India', 'faceImageId': '182026', 'dob': '1998-01-15'}, {'id': '1461506', 'name': 'Sachin Singh', 'teamName': 'India', 'faceImageId': '182026', 'dob': '2002-11-19'}], 'category': 'Sachin'}

players_searched = []
players_id = []
try:
    if searched_data['player']:
        for player in searched_data['player']:
            players_searched.append(player.get('name'))
            players_id.append(player.get('id'))

        # Data fetching from player search API
        selected_player = st.selectbox("Select the Player", players_searched, index=None, placeholder="Select a player to view details" )

        if selected_player:
            #st.write("Selected Player:", selected_player)
            id_index = players_searched.index(selected_player)
            #st.write("Player ID:", players_id[id_index])

            #Showing data in tabs
            tab1, tab2, tab3 = st.tabs(["ℹ️ Info", "🏏 Batting Stats", "⚾ Bowling Stats"])

            with tab1:
                #Player Info players/get-info
                url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{players_id[id_index]}"
                headers = {
                    "x-rapidapi-key": api_key,
                    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
                }
                #Remove comment line below for live execution--------------------------------------
                response = requests.get(url, headers=headers)
                searched_player_info = response.json()
                
                #Comment the below line for live execution--------------------------------------
                # searched_player_info = {'id': '6635', 'bat': 'Left Handed Bat', 'bowl': 'Right-arm offbreak', 'name': 'Usman Khawaja', 'nickName': 'Khawaja', 'height': '1.75 m ', 'role': 'Batsman', 'birthPlace': 'Islamabad, Pakistan ', 'intlTeam': 'Australia', 'teams': 'Australia, New South Wales, Derbyshire, Cricket Australia Chairmans XI, Sydney Thunder, Queensland, Australians, Australia A, Lancashire, Rising Pune Supergiant, Glamorgan, Islamabad United, Brisbane Heat', 'DoB': 'December 18, 1986 (38 years)', 'image': 'http://i.cricketcb.com/stats/img/faceImages/6635.jpg', 'bio': "Ricky Ponting's injury at Sydney in 2011, opened the doors for the first Muslim cricketer to represent Australia at the highest level. A qualified pilot, the highs of this achievement were unparalleled. Having moved to Australia as a kid, Usman Khawaja with the bat in his hands was identified pretty early as the boy wonder.  <br/>  <br/> Honing his skills at the Valley District Cricket Club, Usman made it to the Australian under-19 squad for the 2006 World Cup. He featured in 4 games and hunted down 140 runs making an impression with his poise at the crease and crafty technique. A backlift which comes down on the ball like butter on bread, Khawaja loves to cut and pull.  <br/>  <br/> Following his debut series,  Usman travelled to Sri Lanka and South Africa without much of a success. The year of 2011 ended with a home series against the Kiwis and that also remained a low key affair for the then New batsman.  <br/>  <br/> He was dropped post that and his next tryst with the baggy green happened during the Ashes in England in 2013 after a layoff of almost 18 months. In 3 Tests, he managed only fifty and another exile from Test cricket was handed out.  <br/>  <br/> In the meanwhile, Usman had made his ODI debut at the beginning of 2013 and met a similar fate as he was dropped after three unsuccessful outings in colored clothing. Another big move that Usman had made was the move from NSW to Queensland in 2012. <br/>  <br/> His debut season at Queensland yielded 438 runs from 6 games and it got better in the succeeding season as he riled up 551 runs at an average of 50.09 in 8 games. But then occurred a career-threatening injury. He tore his ACL (Anterior Cruciate Ligament) on his left knee and was out of cricket for the next 9 months.  <br/>  <br/> Khawaja who was now aware and accustomed to the waiting game built on his patience on the sidelines. He returned to the 2015-16 season with a bang. A ton on his return game for Sydney Thunder in December 2015 made the world aware of the destruction that he can be. The T20I debut was just a mere formal announcement when the touring Indians whitewashed Australia 0-3. <br/>  <br/> All this was just before his Test comeback. Usman went onto become a permanent member of the Test team post that barring the tour to India for which he was dropped unceremoniously. But he returned for the Ashes 2017-18 and scored vital knocks over the course of the series. His couple of tons in BBL 05 ensured Sydney Thunder,  the constant wooden Spooner shocked the cricketing fraternity and ended up winning the title.  <br/>  <br/> With the bans of Steve Smith and David Warner in 2018, Khawaja was thrust with the responsibility of being Australia's premier batsman in Tests and he rose to the responsibility with elan. A marathon match-saving knock in UAE was the start of a dream run for the stylish left-hander who also stamped his class during the limited-overs tour of India in 2019. <br/>  <br/> His prolific run in that ODI series and the succeeding one against Pakistan in the UAE helped Khawaja book his maiden World Cup call-up in 2019. A hamstring injury early in the tournament, however, cut his campaign short. He recovered in time for the following Ashes series but a poor run of form saw him dropped from the side and it wouldn't be until 2022 that he'd make a comeback to the international setup.  <br/>  <br/> After a 3-year hiatus, Khawaja returned to the Test side for the 4th Ashes Test in 2021/22 and he made a strong statement after scoring twin-centuries. He followed that up with another excellent performance in Pakistan and ended as the leading run-scorer. Khawaja proved his worth once again as he finished the highly-anticipated 2023 Ashes in England as the leading run-scorer. His contributions at the top of the order were vital in helping Australia retain the Ashes after drawing the series 2-2.  <br/>  <br/> In T20s, Khawaja had a brief stint in the IPL in 2016 with the now defunct Rising Pune Supergiants. He also played a few games for the Islamabad United in the PSL and represented the Sydney Thunder in the BBL until 2022. For the 2023 season, he was signed by the Brisbane Heat and named their captain despite his slim availability due to international duties.  <br/>  <br/> <b>Interesting facts:</b> Apart from being a professional cricketer, Khawaja is also a qualified pilot. <br/>  <br/> Usman is an ex-student of Westfields Sports School, which has also produced sportsmen of the calibre of Michael Clarke (former Australia captain), soccer player Harry Kewell and world champion discus thrower Dani Samuels. <br/>  <br/> <b>By Cricbuzz Staff</b>", 'rankings': {'bat': {'testRank': '18', 'testBestRank': '4', 'odiBestRank': '15', 't20BestRank': '54'}, 'bowl': {}, 'all': {}}, 'appIndex': {'seoTitle': 'Usman Khawaja Profile - Cricbuzz | Cricbuzz.com', 'webURL': 'http://www.cricbuzz.com/profiles/6635/usman-khawaja'}, 'DoBFormat': 'December 18, 1986', 'faceImageId': 332905, 'teamNameIds': [{'teamId': '4', 'teamName': 'Australia'}, {'teamId': '104', 'teamName': 'New South Wales'}, {'teamId': '144', 'teamName': 'Derbyshire'}, {'teamId': '191', 'teamName': 'Cricket Australia Chairmans XI'}, {'teamId': '192', 'teamName': 'Sydney Thunder'}, {'teamId': '164', 'teamName': 'Queensland'}, {'teamId': '266', 'teamName': 'Australians'}, {'teamId': '79', 'teamName': 'Australia A'}, {'teamId': '143', 'teamName': 'Lancashire'}, {'teamId': '346', 'teamName': 'Rising Pune Supergiant'}, {'teamId': '149', 'teamName': 'Glamorgan'}, {'teamId': '330', 'teamName': 'Islamabad United'}, {'teamId': '193', 'teamName': 'Brisbane Heat'}], 'playerTeamIds': '4, 104, 144, 191, 192, 164, 266, 79, 143, 346, 149, 330, 193'}

                st.subheader(f"ℹ️ {searched_player_info.get('name','Unknown')} ({searched_player_info.get('nickName', '-')})")
                # st.write(f"**Role:** {searched_player_info.get('role', 'N/A')}")
                # st.write(f"**Batting:** {searched_player_info.get('bat', 'N/A')}")
                # st.write(f"**Bowling:** {searched_player_info.get('bowl', 'N/A')}")

                # Player Details
                st.markdown(f"""
                **🎭 Role:** {searched_player_info.get('role', 'N/A')}    
                **🏏 Batting:** {searched_player_info.get('bat', 'N/A')}    
                **⚾ Bowling:** {searched_player_info.get('bowl', 'N/A')}   
                **🆔 ID:** {searched_player_info.get('id', 'N/A')}  
                **🌍 International Team:** {searched_player_info.get('intlTeam', 'N/A')}  
                **🎂 Date of Birth:** {searched_player_info.get('DoB', 'N/A')}  
                **🏟️ Birthplace:** {searched_player_info.get('birthPlace', 'N/A')}  
                """)

                st.markdown("### 🏆 Teams Played For")
                st.write(searched_player_info.get('teams', 'N/A'))

            with tab2:
                st.subheader("🏏Batting Statistics")
                # Player Batting Stats players/get-batting
                url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{players_id[id_index]}/batting"

                headers = {
                    "x-rapidapi-key": api_key,
                    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
                }
                #Remove comment line below for live execution--------------------------------------
                response = requests.get(url, headers=headers)
                batting_stats = response.json()
                #Comment the below line for live execution--------------------------------------
                # batting_stats = {'headers': ['ROWHEADER', 'Test', 'ODI', 'T20', 'IPL'], 'values': [{'values': ['Matches', '84', '40', '9', '6']}, {'values': ['Innings', '152', '39', '9', '6']}, {'values': ['Runs', '6053', '1554', '241', '127']}, {'values': ['Balls', '12464', '1848', '182', '100']}, {'values': ['Highest', '232', '104', '58', '30']}, {'values': ['Average', '43.55', '42', '26.78', '21.17']}, {'values': ['SR', '48.57', '84.10', '132.42', '127.00']}, {'values': ['Not Out', '13', '2', '0', '0']}, {'values': ['Fours', '645', '150', '31', '14']}, {'values': ['Sixes', '28', '13', '5', '3']}, {'values': ['Ducks', '9', '2', '0', '0']}, {'values': ['50s', '27', '12', '1', '0']}, {'values': ['100s', '16', '2', '0', '0']}, {'values': ['200s', '1', '0', '0', '0']}, {'values': ['300s', '0', '0', '0', '0']}, {'values': ['400s', '0', '0', '0', '0']}], 'appIndex': {'seoTitle': 'Usman Khawaja Profile - Cricbuzz | Cricbuzz.com', 'webURL': 'http://www.cricbuzz.com/profiles/6635/usman-khawaja'}, 'seriesSpinner': [{'seriesName': 'Career'}]}

                headers = batting_stats['headers']
                rows = [item["values"] for item in batting_stats["values"]]

                df = pd.DataFrame(rows, columns=headers)
                df = df.rename(columns={"ROWHEADER": "Stats"})
                st.dataframe(df, hide_index=True)


            with tab3:
                st.subheader("⚾Bowling Statistics")
                # Player Batting Stats players/get-bowling
                url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{players_id[id_index]}/bowling"

                headers = {
                    "x-rapidapi-key": api_key,
                    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
                }
                #Remove comment line below for live execution--------------------------------------
                response = requests.get(url, headers=headers)
                bowling_stats = response.json()
                #Comment the below line for live execution--------------------------------------
                # bowling_stats = {'headers': ['ROWHEADER', 'Test', 'ODI', 'T20', 'IPL'], 'values': [{'values': ['Matches', '84', '40', '9', '6']}, {'values': ['Innings', '3', '0', '0', '0']}, {'values': ['Balls', '18', '0', '0', '0']}, {'values': ['Runs', '8', '0', '0', '0']}, {'values': ['Maidens', '0', '0', '0', '0']}, {'values': ['Wickets', '0', '0', '0', '0']}, {'values': ['Avg', '0.0', '0.0', '0.0', '0.0']}, {'values': ['Eco', '2.67', '0', '0', '0']}, {'values': ['SR', '0.0', '0.0', '0.0', '0.0']}, {'values': ['BBI', '0/1', '-/-', '-/-', '-/-']}, {'values': ['BBM', '0/1', '-/-', '-/-', '-/-']}, {'values': ['4w', '0', '0', '0', '0']}, {'values': ['5w', '0', '0', '0', '0']}, {'values': ['10w', '0', '0', '0', '0']}], 'appIndex': {'seoTitle': 'Usman Khawaja Profile - Cricbuzz | Cricbuzz.com', 'webURL': 'http://www.cricbuzz.com/profiles/6635/usman-khawaja'}, 'seriesSpinner': [{'seriesName': 'Career'}]}

                headers = bowling_stats['headers']
                row = [item['values'] for item in bowling_stats["values"]]

                df = pd.DataFrame(row, columns=headers)
                df = df.rename(columns={"ROWHEADER": "Stats"})
                st.dataframe(df, hide_index=True)
        
except KeyError:
    st.warning("No players found with that name. Please try again with a different name.")






    


    

    

