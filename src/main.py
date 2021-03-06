from StatPackager import StatPackager 
from Commands import Commands
import matplotlib.pyplot as plt


#URL's for the website we are scraping
url_17_18 = "https://www.basketball-reference.com/leagues/NBA_2018_per_game.html"
url_18_19 = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
url_19_20 = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html"

#Year for each season
year_18 = 2018
year_19 = 2019
year_20 = 2020

#Creating StatPackager object using url
stats_18 = StatPackager(url_17_18, year_18)
stats_19 = StatPackager(url_18_19, year_19)
stats_20 = StatPackager(url_19_20, year_20)

#Categories for each table
header_18 = stats_18.get_header()
header_19 = stats_19.get_header()
header_20 = stats_20.get_header()

#List of all the rows of data for each season
data_18 = stats_18.get_rows()
data_19 = stats_19.get_rows()
data_20 = stats_20.get_rows()

#Saving into csv file
stats_18.to_csv('datasets/stats-17-18.csv', header_18, data_18)
stats_19.to_csv('datasets/stats-18-19.csv', header_19, data_19)
stats_20.to_csv('datasets/stats-19-20.csv', header_20, data_20)









