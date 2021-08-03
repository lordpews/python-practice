import requests

query_params = {
    "source": "bbc-news",
    "sortBy": "top",
    "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
}
main_url = " https://newsapi.org/v1/articles"

# fetching data in json format
res = requests.get(main_url, params=query_params)
open_bbc_page = res.json()

print(res)
print(open_bbc_page)