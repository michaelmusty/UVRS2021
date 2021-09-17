import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://802timing.com/results/21results/runresults/9.11.21sproutyoverall.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table')
assert len(tables) == 1
rows = tables[0].find_all('tr')

first_names = []
last_names = []
net_times = []

for row in rows:
    row_list = []
    for cell in row.findAll(["td", "th"]):
        row_list.append(cell.get_text())
    try:
        name = row_list[1]
        first_names.append(name.split(" ")[0])
        last_names.append(name.split(" ")[1])
        net_times.append(row_list[8].split(".")[0].strip())
    except:
        pass

def format_time_for_spreadsheet(s):
    """ we want 00:20:05 instead of 20:05
    """
    colon_count = s.count(":")
    assert colon_count in [1,2]
    if colon_count == 1:
        t = datetime.strptime(s,"%M:%S")
    else:
        t = datetime.strptime(s,"%H:%M:%S")
    return t.strftime("%H:%M:%S")

print("\nFIRST NAMES\n")
for x in first_names:
    print(x)
print("\nLAST NAMES\n")
for x in last_names:
    print(x)
print("\nNET TIMES\n")
for x in net_times:
    print(format_time_for_spreadsheet(x))

# tests
assert format_time_for_spreadsheet("20:05") == "00:20:05"
assert format_time_for_spreadsheet("1:23:05") == "01:23:05"
