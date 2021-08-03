import requests

r = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=6123d131eeb3ba54e756a99c07b4140c")
print(r.text)
print(r.status_code)

# url = "www.xnxx.tv"
#
# data = {
#     "p1" : 4 ,
#     "p2" : 5 ,
#     "p3" : 6 ,
#     "p4" : 7
# }
#
# r2 =  requests.post(url=url,data=data)
"""
example of post
 url = www.facebook.com
 info = {
  "username" = your_name,
  "password" = your_pass

post_data = r2 =  requests.post(url=www.facebook.com,data=info)
  
  # post requests are not cacheable but get requests are
  # so you'll send you username and password to the url but can't be cached or saved by that server
  }

"""