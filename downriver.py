import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.pinnacletiming.us/index.php?n=downriver_rail_run_10k_overall_2021'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

pre = soup.find_all('pre')
assert len(pre) == 1

pre = str(pre)

rows = pre.split("\n")[11:]
rows = [x.strip() for x in rows]
rows = [x.split() for x in rows]
rows = [x[5:] for x in rows]
rows.pop(-1)
for i,row in enumerate(rows):
    print(f"i={i}: {len(row)} : {row}")

first_names = []
last_names = []
net_times = []

for row in rows:
        first_names.append(row[0])
        last_names.append(row[1])
        net_times.append(row[-2])

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
