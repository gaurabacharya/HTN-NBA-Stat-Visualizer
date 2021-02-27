from Commands import Commands
import matplotlib.pyplot as plt
import numpy as np
import os

#Years for the 3 seasons
year_18 = 2018
year_19 = 2019
year_20 = 2020
#Main Categories for analysis
categorycode = ['pts', 'ast', 'trb', 'blk', 'stl', 'tov', 'ft_', 'fg_', '_3p_']
category_name = ['Points', 'Assists', 'Rebounds', 'Blocks', 'Steals', 'Turnovers', 'Free Throw Percentage', 'Field Goal Percentage', '3 Point Percentage']
seasons = ['2017-2018', '2018-2019', '2019-2020']
#Creating Commands Objects
sts18 = Commands(str(year_18))
sts19 = Commands(str(year_19))
sts20 = Commands(str(year_20))

top5all_18 = []
top5all_19 = []
top5all_20 = []

#Getting top 5 from each category for each season
for x in categorycode:
    top5all_18.append(sts18.get_top5_category(x))
    top5all_19.append(sts19.get_top5_category(x))
    top5all_20.append(sts20.get_top5_category(x))

#plotting top 5 for each category
all_stats = [top5all_18, top5all_19, top5all_20]
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
        
        
    





