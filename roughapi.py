import http.client

conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

headers = {
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "2061d3ec6bmsh23bfa29a516ce56p14570ajsna84ba056c8d5",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

conn.request("GET", "/language/translate/v2/languages", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))