import urllib.request, json, time, datetime,config


while True:

    currentMinute = datetime.datetime.now().minute;

    if(currentMinute % 15 == 0):

        url="https://newsapi.org/v2/top-headlines?country=us&apiKey=" + config.newsapi_key

        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            print(data)
        
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

        time.sleep(900);

    else:
        
        secondsToSleep = (15 - (currentMinute % 15)) * 60;
        
        print(currentMinute)
        print("Sleeping %s" % (secondsToSleep))
        
        time.sleep(secondsToSleep);
