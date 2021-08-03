import requests


def speak(string):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(string)


def newsfetcher():
    query_params = {
        "sortby": "top",
        "apikey": "18a75b52ce224f09bf077b767e5b7f41"
    }
    newsurl = "https://newsapi.org/v2/top-headlines?country=in"

    resp = requests.get(url=newsurl, params=query_params)
    newss = resp.json()
    article = newss["articles"]
    print(type(article))
    print(article)
    results = []
    for items in article:
        results.append(items["title"])
    for i in range(len(results)):
        print(i + 1, results[i])
    return results


if __name__ == '__main__':
    speak(newsfetcher())

# how it works (●'◡'●)
# speak function was copied so i dont know its working uwu
# query params contains the parameters for query it can be also added in url
# resp stores the response from get request
# its turned into a json format which is like a dictionary
# all the values with 'articles' key are stored in a list 'newss' its like a dictionary
# (json lists can have key value pairs)
# empty list results is created
# each value with key 'title' is appended to the list
# returns results which is the list containing all the news
# speak functions does its work
print("pycharm is slow")
print("are you gay?")
