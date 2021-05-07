#Python list all h1,h2,h3 tags from the page Kean.edu

import requests

from bs4 import BeautifulSoup

url = 'https://www.kean.edu/'

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("List of all the h1, h2, h3 :")

for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.name + ' ' + heading.text.strip())