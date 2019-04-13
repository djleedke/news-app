from application import config
import urllib.request, json, time, datetime

print("We are catching the news!")

def catch_news():
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=" + config.newsapi_key

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        print(data)
                    
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)



def say_hello():
    print("WOOP")
