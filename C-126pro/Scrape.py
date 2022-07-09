#from pydoc import plainpager
from selenium import webdriver 
from bs4 import BeautifulSoup 
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=["Proper_name","Distance","Mass","Radius"]
    star_data = []
    for i in range(0,1):
        soup=BeautifulSoup (browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr"):
            td_tags=tr_tag.find_all("td")
            temp_list=[]
            for index, td_tag in enumerate(td_tags):
              if index ==0:
                temp_list.append(td_tag.find_all("a")[0].contents[0])
              else:
                try:
                    temp_list.append(td_tag.contents[0])
                except:
                    temp_list.append("")
            
            star_data.append(temp_list)
        
scrape()

with open("final.csv","w")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

#C:\Users\SHIVEN\OneDrive\Desktop\code\C-126pro


