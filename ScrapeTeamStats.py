from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

teamcode = ["buf", "ram", "nor", "atl", "cle", "car", "sfo", "chi", "pit", "cin",
            "kan", "crd", "tam", "dal", "phi", "det", "clt", "htx", "nwe", "mia", "gnb", "min",
            "rav", "nyj", "nyg", "oti", "rai", "sdg", "jax", "was", "den", "sea"]

headers = ["Team", "3rdDwnConv", "4thDwnConv", "3rdDwnAll",
           "NY/A", "OPointsPerYard", "DPointsPerYard", "TotalPPY"]

with open('PowerRatings2022.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    # write headers
    writer.writerow(headers)

    for team in teamcode:
        l = "https://www.pro-football-reference.com/teams/{}/2022.htm".format(team)

        page = urlopen(l)
        page_html = page.read()
        page.close()
        soup = BeautifulSoup(page_html, 'html.parser')

        # get full team name
        Header = soup.find('div', id='meta')
        h = Header.find('h1')
        teamName = h.text.replace("2022", '')
        teamName = teamName.split("Rosters")
        tName = teamName[0].replace('\n', '')

        # get TeamStats Table
        TeamStats = soup.find('table', id='team_stats')
        TeamStatsData = TeamStats.find_all('td')

        # get conversion table
        ConversionTable = soup.find('table', id='team_conversions')
        ConversionData = ConversionTable.find_all('td')

        # calculate points per yard
        PointPerYard = round(float(TeamStatsData[1].text) / float(TeamStatsData[0].text), 2)

        # calculate points per yard allowed
        PointPerYardAll = round(float(TeamStatsData[31].text) / float(TeamStatsData[30].text), 2)

        # calculate net points per yard
        NetPPY = round(PointPerYardAll - PointPerYard, 2)

        # Remove % from conversion data
        thirdDownConv = ConversionData[2].text.replace('%', '')
        thirdDownConv = float(thirdDownConv)

        fourthDownConv = ConversionData[5].text.replace('%', '')
        fourthDownConv = float(fourthDownConv)

        thirdDownAll = ConversionData[11].text.replace('%', '')
        thirdDownAll = float(thirdDownAll)

        stats = [tName, thirdDownConv, fourthDownConv,
                 thirdDownAll, float(TeamStatsData[12].text), PointPerYard, PointPerYardAll, NetPPY]

        writer.writerow(stats)
