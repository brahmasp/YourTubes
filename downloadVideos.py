#downloadVideos.py
#responsible for downloading the required links (linkList)

from bs4 import BeautifulSoup; #only for display the hrefs of links
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
import webbrowser;

def downloadVid(linkList):
    
    #site used to download the videos
    downloadSite1 = "http://en.savefrom.net/1-how-to-download-youtube-video/";
    downloadSite2 = "http://www.clipconverter.cc/";
    

    #setsup connection to ChromeBrowser
    browser = webdriver.Chrome(executable_path="Chrome_Driver/chromedriver");
    #browser = webdriver.Firefox();


    for video in linkList:
        browser.get(downloadSite1);
        inputBox = browser.find_element_by_xpath('//*[@id="sf_url"]');
        inputBox.send_keys(video["href"]);

        browser.find_element_by_xpath('//*[@id="sf_submit"]').click();
    
        downloadLink = browser.find_element_by_xpath('//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a').get_attribute("href");
        webbrowser.open_new(downloadLink);
        
    """for site 2
    for video in linkList:
        browser.get(downloadSite);
        inputBox = browser.find_element_by_xpath('//*[@id="mediaurl"]');
        inputBox.send_keys(video["href"]);

        browser.find_element_by_id("submiturl").click();
    
        downloadLink = browser.find_element_by_xpath('//*[@id="submitconvert"]/input').get_attribute("href");
        webbrowser.open_new(downloadLink);"""
    
