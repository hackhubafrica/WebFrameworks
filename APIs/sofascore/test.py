    import requests

url = "https://sofascore.p.rapidapi.com/matches/get-votes"

querystring = {"matchId":"8897222"}

headers = {
    "x-rapidapi-key": "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    "x-rapidapi-host": "sofascore.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


import requests

url = "https://sofascore.p.rapidapi.com/matches/get-tweets"

querystring = {"matchId":"8897222"}

headers = {
    "x-rapidapi-key": "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    "x-rapidapi-host": "sofascore.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

import requests

url = "https://sofascore.p.rapidapi.com/matches/get-incidents"

querystring = {"matchId":"8897222"}

headers = {
    "x-rapidapi-key": "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    "x-rapidapi-host": "sofascore.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())