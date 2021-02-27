from Commands import Commands
import matplotlib.pyplot as plt
import numpy as np
import os

year_18 = 2018
year_19 = 2019
year_20 = 2020
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

categorycode = [points, assists, rebounds, blocks, steals, turnovers, free_throw_percentage, fieldgoal_percentage, threept_percentage]
category_name = ['Points', 'Assists', 'Rebounds', 'Blocks', 'Steals', 'Turnovers', 'Free Throw Percentage', 'Field Goal Percentage', '3 Point Percentage']
seasons = ['2017-2018', '2018-2019', '2019-2020']
sts18 = Commands(str(year_18))
sts19 = Commands(str(year_19))
sts20 = Commands(str(year_20))

top5all_18 = []
top5all_19 = []
top5all_20 = []

for x in categorycode:
    top5all_18.append(sts18.get_top5_category(x))
    top5all_19.append(sts19.get_top5_category(x))
    top5all_20.append(sts20.get_top5_category(x))

#plotting top 5 for each category
"""fig = plt.figure(figsize=(10, 6))
ax = fig.add_axes([0, 0, 1, 1])
eighteenpts = top5all_18[0]
labels = eighteenpts.keys()
x = np.arange(len(labels))


ax.set_ylabel("points")
ax.set_title('Top 5 scorers in 2017-18 Season')
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.bar(labels, eighteenpts.values())
plt.show()
"""
all_stats = [top5all_18, top5all_19, top5all_20]
my_path = os.path.abspath('/Users/gaurabacharya/PycharmProjects/HTN-NBA-Stat-Visualizer/')
for i in range(len(categorycode)):
    for j in range(len(all_stats)):
        fig = plt.figure(figsize=(10,6))
        ax = fig.add_axes([0, 0, 1, 1])
        current_data = all_stats[j][i]
        labels = current_data.keys()
        x = np.arange(len(labels))
        
        ax.set_ylabel(category_name[i])
        ax.set_title('Top 5 Players in the {} Season in {}'.format(seasons[j], category_name[i]))
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        
        ax.bar(labels, current_data.values())
        plt.savefig('top5-{}-{}.png'.format(category_name[i], seasons[j]), dpi=300, bbox_inches='tight')
        plt.show()
        
        
    





