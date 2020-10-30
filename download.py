import requests
import json, re
from bs4 import BeautifulSoup

filePattern = re.compile(r'(https:\/\/[\w\.\/\-]+)')
datePattern = re.compile(r'-(\d+)-')

coronaPage = 'https://www.ssi.dk/sygdomme-beredskab-og-forskning/sygdomsovervaagning/c/covid19-overvaagning/arkiv-med-overvaagningsdata-for-covid19'

req = requests.get(coronaPage)
soup = BeautifulSoup(req.text, 'html.parser')

rte_result = soup.find_all('section', attrs={'class': 'rte'})

rte = BeautifulSoup(str(rte_result), 'html.parser')

acc_result = rte.find_all('accordions')

accordions = BeautifulSoup(str(acc_result), 'html.parser')

link_result = accordions.find('p')
links = BeautifulSoup(str(link_result), 'html.parser')

results = []
a = links.find_all('a')

for link in a:
    link = str(link)
    filelink = str(filePattern.search(link).group(1))
    results.append(filelink)

print(json.dumps(results, sort_keys=True, indent=2))

for link in results:
    file = requests.get(link)
    date = str(datePattern.search(link).group(1))
    open(f'./data/{date}.zip', 'wb').write(file.content)
    
