# -*- coding: utf-8 -*-

import datetime
import feedparser
import pandas as pd

df = pd.DataFrame


def get_Trends_Rss():
    NewsFeed = feedparser.parse("https://trends.google.com/trends/trendingsearches/daily/rss?geo=US")
    #This is for testing, to make sure you can print an entry out
    entry = NewsFeed.entries[1]
    #print(entry.keymap) #this will print out all of the optinoal feilds from the RSS feed
    
    # This is also for testing, it shows all of the optional feilds in the RSS feed
    # for i in entry:
    #     print(i) 
    count =0
    count = len(NewsFeed.entries)
    print("\nNumber of items: " + str(count))
    trendsDict = {}
    countTracker =0
    #This is the area that will collect all of the entry data into a df.
    for i in NewsFeed.entries:
        title = i.title
        traffic= i.ht_approx_traffic
        if len(i.summary_detail["value"]) >0: #grabs the items that have extra details information
            description = i.summary_detail["value"]
        else:
            description = "None"
        pubDate = i.published
        url = i.link
        trendsDict[countTracker] = {"Title":title,"Traffic":traffic,"Description":description,"Published":pubDate,"Link":url}
        """ Below here is the terminal representation of things
        """
        countTracker+=1
    for i in trendsDict:
        print(trendsDict[i])
    return trendsDict

df = get_Trends_Rss()