import requests
import bs4
import time
from bs4 import BeautifulSoup
import pandas as pd

target_url = "https://rainbow-connection.co.uk/collections/new-in"
head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

response = requests.get(target_url, headers=head)
soup = BeautifulSoup(response.text, 'html.parser')

web_data = []

resultList = soup.find_all("div", {"class":"one-third"})

def generateResults():
    for results in resultList:
        title_element = results.find("span", {"class":"title"})
        price_element = results.find("span", {"class":"money"})
        thumbnail_element = results.find("img", {"class":"primary"})
        
        web_data.append({"Title": title_element.text.strip(), "Price": price_element.text.strip(), "Image": thumbnail_element["data-original"]})
        
if response.ok is False:
    print(f"Get request failed - Error Code:", {response.status_code})
else:
    generateResults()
    
print(web_data)



