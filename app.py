import requests
import json

#Cricbuzz Live Scores API
# url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

# headers = {
# 	"x-rapidapi-key": "4879a17e0cmsh37b379d4ab14552p161d4djsncf56613e28e8",
# 	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)
# data = response.json()
# print(data)

with open('json_files/live.json', 'r') as f:
    data = json.load(f)

#print(live.keys())

# Traverse through each matchType and its matches
for section in data["live_matches"]:
    print(f"\nMatch Type: {section['matchType']}")
    print("=" * 40)
    
    for match in section["matches"]:
        print(f"Series: {match['seriesName']}")
        print(f"Match: {match['matchDesc']}")
        print(f"Format: {match['matchFormat']}")
        print(f"Teams: {', '.join(match['teams'])}")
        print(f"Status: {match['status']}")
        print(f"Venue: {match['venue']}")
        
        # Some matches have scores
        if "scores" in match:
            print("Scores:")
            for team, score in match["scores"].items():
                print(f"  {team}: {score}")
        
        print("-" * 40)
    