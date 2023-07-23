from bs4 import BeautifulSoup
import requests

with open('proj_scraping\example.html') as inFile:
    soup = BeautifulSoup(inFile, 'lxml')
    
print(f"The links with the ids' are: {soup.body.header.find_all('a', href=True)}")
