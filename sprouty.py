import csv
import requests
from bs4 import BeautifulSoup

url = 'http://802timing.com/results/21results/runresults/9.11.21sproutyoverall.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table')
assert len(tables) == 1
rows = tables[0].find_all('tr')

with open("sprouty.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        csv_row = []
        for cell in row.findAll(["td", "th"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)
