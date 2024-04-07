from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

week = []
game = []
home = []
away = []
x = 0
y= 272
z=0

l = "https://www.pro-football-reference.com/years/2022/games.htm"

page = urlopen(l)
page_html = page.read()
page.close()
soup = BeautifulSoup(page_html, 'html.parser')

Schedule = soup.find('table', id='games')

Week = Schedule.find_all("th")

for w in Week:
    if (len(w.text) <= 2 and len(w.text) > 0):
        if(int(w.text) > 9):
            week.append(w.text)
GameLinks = Schedule.find_all('a', href=True)

while(x < len(GameLinks)):
    if(GameLinks[x].text!= "boxscore" and GameLinks[x].text!= "preview" ):
        game.append(GameLinks[x].text)
    x+=1

while(y < len(game)):
    if y % 2 == 0:
        away.append(game[y])
    else:
        home.append(game[y])
    y +=1

with open('Schedule2022.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    while(z < len(week)):
        row = [week[z],  home[z], away[z]]
        writer.writerow(row)
        z += 1