import requests
import json

response = requests.get('https://api.collegefootballdata.com/games?year=2020&seasonType=regular&team=Michigan')
if response.status_code == 400:
    print('error')
    quit()

games = json.loads(response.text)
for game in games:
    if game['home_points'] is not None:
        print('{} {} - {} {}'.format(game['home_team'], game['home_points'], game['away_points'], game['away_team']))
