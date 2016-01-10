#linkScraper.py
#responsible for scraping the web page (of specified playlist link)
#and getting video links

import urllib.request
import urllib.parse;
from bs4 import BeautifulSoup;

def getLinks(playlistLink, lowerRange, upperRange, menuChoice):
    
    #sites we want to visit
    #used for testing purposes/debugging
    sample_urls = ["https://www.youtube.com/playlist?list=LL3IcEolPgWzJzKl38XMP99w", 
    "https://www.youtube.com/playlist?list=PLykzf464sU9_RYk_ex-SEl2WXeB0D0wTB",
                   "https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDgp7nGSUnnXihbTLFZJ79B"];

    #base used for standarizing the links
    baseURL = "http://" + str(urllib.parse.urlparse(playlistLink).hostname);
    
    #make request to server for the required page to playlist
    htmlText = urllib.request.urlopen(playlistLink).read();

    soup = BeautifulSoup(htmlText, "html.parser");

    return getList(htmlText, soup, baseURL, lowerRange, upperRange, menuChoice);


def getList(htmlText, soup, baseURL, lowerRange, upperRange, menuChoice):
    
    #getting all the links to the videos in playlist
    linkList = soup.find_all("a", "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link ");
    
    if (menuChoice == "2" and int(upperRange) < len(linkList)):
        linkList = linkList[int(lowerRange) - 1 : int(upperRange)];           
       
    #standardizing the links
    for link in linkList:
            link["href"] = urllib.parse.urljoin(baseURL, link["href"]);
            #print (link["href"]);
    print (linkList);
        
    return linkList;


