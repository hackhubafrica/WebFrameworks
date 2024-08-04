import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/categories/list-live?sport=football", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/auto-complete?query=cris", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


#TEAMS


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/detail?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-logo?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-performance?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-transfers?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-squad?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-rankings?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-tournaments?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-near-events?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-statistics-seasons?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-statistics?teamId=38&tournamentId=7&seasonId=29267&type=overall", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-player-statistics-seasons?teamId=38", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-player-statistics?teamId=38&tournamentId=7&seasonId=29267&type=overall", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-last-matches?teamId=38&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-next-matches?teamId=38&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/get-matches?teamId=38&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/teams/search?name=Chelsea", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/detail?playerId=155997", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))






import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-image?playerId=155997", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-characteristics?playerId=155997", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-last-ratings?playerId=155997&tournamentId=7&seasonId=29267", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-attribute-overviews?playerId=155997", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-national-team-statistics?playerId=155997", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-transfer-history?playerId=155997", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-last-year-summary?playerId=155997", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-statistics-seasons?playerId=155997", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-statistics?playerId=155997&tournamentId=7&seasonId=29267&type=overall", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-last-matches?playerId=155997&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-next-matches?playerId=155997&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/get-matches?playerId=155997&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/players/search?name=Cristiano%20Ronaldo", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/managers/get-career-history?managerId=53418", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/managers/detail?managerId=53418", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/managers/get-image?managerId=53418", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/managers/get-last-matches?managerId=53418&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/managers/get-next-matches?managerId=53418&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/managers/get-matches?managerId=53418&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/managers/search?name=Jos%C3%A9%20Mourinho", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/list?categoryId=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/detail?tournamentId=17", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-logo?tournamentId=17", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-featured-events?categoryId=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-scheduled-events?categoryId=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-live-events?sport=football", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-seasons?tournamentId=17", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-top-players?tournamentId=17&seasonId=29415", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-top-teams?tournamentId=17&seasonId=29415&type=total", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-rounds?tournamentId=17&seasonId=29415", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-team-of-the-week-rounds?tournamentId=17&seasonId=29415", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-team-of-the-week?tournamentId=17&seasonId=29415&roundId=5642", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-player-statistics?tournamentId=17&seasonId=29415&limit=20&order=-rating&accumulation=total&group=summary", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-standings?tournamentId=17&seasonId=29415&type=total", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-media?tournamentId=17", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-cuptrees?tournamentId=17&seasonId=29415", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-last-matches?tournamentId=17&seasonId=29415&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-next-matches?tournamentId=17&seasonId=29415&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/get-matches?tournamentId=17&seasonId=29415&pageIndex=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/tournaments/search?name=Premier%20League", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/detail?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-lineups?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-incidents?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-managers?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-votes?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-graph?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-statistics?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-team-streaks?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-best-players?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-media?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", "/matches/get-tweets?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-esport-games?matchId=9744554", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-player-statistics?matchId=9644933&playerId=832208", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-player-heatmap?matchId=9644933&playerId=832208", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-all-odds?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-featured-odds?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-h2h-events", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-h2h-events", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/matches/get-head2head?matchId=8897222", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/esport-games/get-lineups?gameId=288315", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/esport-games/get-statistics?gameId=288315", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/esport-games/get-rounds?gameId=288315", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))








import http.client

conn = http.client.HTTPSConnection("sofascore.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

conn.request("GET", "/esport-games/get-bans?gameId=288315", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
































































