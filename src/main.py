from StatPackager import StatPackager 
from Commands import Commands
import matplotlib.pyplot as plt


#StatPackager Commands
url_17_18 = "https://www.basketball-reference.com/leagues/NBA_2018_per_game.html"
url_18_19 = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
url_19_20 = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html"

year_18 = 2018
year_19 = 2019
year_20 = 2020

stats_18 = StatPackager(url_17_18, year_18)
stats_19 = StatPackager(url_18_19, year_19)
stats_20 = StatPackager(url_19_20, year_20)

header_18 = stats_18.get_header()
header_19 = stats_19.get_header()
header_20 = stats_20.get_header()

data_18 = stats_18.get_rows()
data_19 = stats_19.get_rows()
data_20 = stats_20.get_rows()

stats_18.to_csv('datasets/stats-17-18.csv', header_18, data_18)
stats_19.to_csv('datasets/stats-18-19.csv', header_19, data_19)
stats_20.to_csv('datasets/stats-19-20.csv', header_20, data_20)

#Data Manipulating Commands from class Commands
points = 'pts'
assists = 'ast'
rebounds = 'trb'
blocks = 'blk'
steals = 'stl'
turnovers = 'tov'
free_throw_percentage = 'ft_'
fieldgoal_percentage = 'fg_'
threept_percentage = '_3p_'

categories = [points, assists, rebounds, blocks, steals, turnovers, free_throw_percentage, fieldgoal_percentage, threept_percentage]

sts18 = Commands(str(year_18))
sts19 = Commands(str(year_19))
sts20 = Commands(str(year_20))

top5all_18 = []
top5all_19 = []
top5all_20 = []

for x in categories:
    top5all_18.append(sts18.get_top5_category(x))
    top5all_19.append(sts19.get_top5_category(x))
    top5all_20.append(sts20.get_top5_category(x))

#plotting top 5 for each category
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(top5all_18[0].keys()[0], top5all_18[0].values()[0])
plt.show()







