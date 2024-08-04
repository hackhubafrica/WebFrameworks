import http.client

conn = http.client.HTTPSConnection("sportapi7.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699",
    'x-rapidapi-host': "sportapi7.p.rapidapi.com"
}

conn.request("GET", "/api/v1/event/xdbsZdb/h2h/events", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))