import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

target_url = "https://rainbow-connection.co.uk/collections/new-in"
head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

response = requests.get(target_url, headers=head)
print(response)

soup = BeautifulSoup(response.text, 'html.parser')

resultList = soup.find_all("div", {"class":"one-third"})

print(resultList)

for results in resultList:
    title_element = results.find("span", {"class":"title"})
    price_element = results.find("span", {"class":"money"})
    print(title_element)
    print(price_element)