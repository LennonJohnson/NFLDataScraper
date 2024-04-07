import csv

Home = []
Away = []
headers = ["Team", "3rdDwnConv", "4thDwnConv", "3rdDwnAll",
           "NY/A", "OPointsPerYard", "DPointsPerYard", "TotalPPY", "PPY Difference"]

x: int = 0
# input week you want to get matchups for
week = int(input('Enter Week: '))

# make sure it is a valid week
while week < 1 or week > 18:
    week = input('Invalid Input ReEnter Week: ')

week = str(week)

# read csv, and split on "," the line
csv_Schedule = csv.reader(open('Schedule2022.csv', "r"), delimiter=",")

# loop through the schedule and save the home teams and away teams
for row in csv_Schedule:
    # if current rows 2nd value is equal to input, print that row
    if week == row[0]:
        Home.append(str(row[1]))
        Away.append(str(row[2]))

# get the stats for each game
filename = 'Week{}Matchups.txt'.format(week)

file_handle = open('PowerRatings2022.csv', "r")
csv_PowerRatings = csv.reader(file_handle)

with open(filename, 'w') as f:
    headLine = "{:^25} {:<15} {:<15} {:<15} {:<10} {:<20} {:<20} {:<20}".format(headers[0], headers[1], headers[2], headers[3],
                                                                               headers[4], headers[5], headers[6], headers[7])
    f.write(headLine)
    f.write('\n')
    f.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    while x < len(Home):
        for row in csv_PowerRatings:
            if Home[x] == row[0]:
                home = row
                print(row)
            elif Away[x] == row[0]:
                away = row
                print(row)
        print("--------------------------------------------------------------------------------------------")

        CombinedPPy = round(float(home[len(home) - 1]) - float(away[len(home) - 1]), 2)

        line1 = "{:<25} {:<15} {:<15} {:<15} {:<10} {:^20} {:^20} {:<20}".format(str(home[0]), str(home[1]), str(home[2]),
                                                                           str(home[3]), str(home[4]),
                                                                           str(home[5]), str(home[6]), str(home[7]))

        line2 = "{:<25} {:<15} {:<15} {:<15} {:<10} {:^20} {:^20} {:<20}".format(str(away[0]), str(away[1]),
                                                                                 str(away[2]),
                                                                                 str(away[3]), str(away[4]),
                                                                                 str(away[5]), str(away[6]),
                                                                                 str(away[7]))
        f.write(line1)
        f.write('\n')
        f.write(line2)

        f.write("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

        file_handle.seek(0)
        x += 1
