#purpose: Download >1 videos with a single link
#main.py
#Libraries/APIs used:
#1. BeautifulSoup
#2. Selenium
#3. urllib
#4. webbrowser
#5. mysql.connector
#responsible for controlling overall functionality
#of "YourTubes"

import linkScraper;
import downloadVideos;

def main():
    #asks users playlist link
    playlistLink, lowerRange, upperRange, menuChoice = whichURL();
    print (playlistLink);
    print (str(lowerRange) + " " + str(upperRange));

    #gets an array of all the videos in a specified playlist
    linkList = linkScraper.getLinks(playlistLink, lowerRange, upperRange, menuChoice);

    #stores linkList data in MySQL database
    #databaseManager.writeToDB(linkList);
    
    #calls method to download the required videos
    downloadVideos.downloadVid(linkList);

def whichURL():
    menuChoice = input("Select from menu:\n1. Entire Playlist\n2. Multiple Videos in order\n");

    if (menuChoice == "1"):
        return (input("Enter link of playlist to download: "), 0, 0, menuChoice);
    elif (menuChoice == "2"):
        lowerRange = input("Enter lower range (>=1): ");
        upperRange = input("Enter upper range (>lowerRange) (if more than number if videos then downloads till end): ");
        return (input("Enter link of playlist to download: "), lowerRange, upperRange, menuChoice);

main();


#possible updates:
#1. multithreading??
#2. include database. so only specific video can be downloaded in case
# that video is lost
#3. use flask and make it have a front end



       
