from DataParser import Database


class Commands:
    """
    A class to access data from database and create specific statistics based on the given year

    Attributes
    ----------
    year : int
        the year referring to a specific season dataset
    stats : dict
        dictionary dataset that contains player stats for the specific year with category and value pairs

    Methods
    -------
    get_player_stats(name)
        accesses stats to return a dictionary of all stats for given player name
    def get_all_category(categoryCode)
        accesses stats to get all players stats for a specific stat category e.g. points, assists and returns dictionary
    def get_top5_category(categoryCode)
        gets and returns dictionary of top 5 players of given category code
    """
    def __init__(self, year):
        """
        Parameters
        ----------
        year : int
            the year referring to a specific season dataset
        """
        self.year = year
        TOKEN = "E6cns5ucSZAxNEfe6gRusH"
        REST_KEY = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoiU0d4SHc2ZWZrdkxWdWhUakFzbzhVQyIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6IlZCUHdlaDdCV09yMlhJRTcxbkxsNWJrT1l6b05TdkN6Q1pUYjhIdzJrQ3psWjBST3BwOGJYd3pRdUJteFJBR3EiLCJpYXQiOjE2MTA5Mjc2NTcsImV4cCI6MTYxOTU2NzY1NywiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJvQ3NQODJqOTY2dTgyOXpxN0xoVU00In0.XJF-YbxpBrYQd67epG2LPFHgTn18N4rdmHZWBgwzIus"

        query = '?select=player,pts,dropbase_ts'
        default_query = "null"
        table_to_query = "nbastats2"
        year_2017_18 = "2021-01-18T01:51:29.180433"
        year_2018_19 = "2021-01-18T02:12:57.530854"
        year_2019_20 = "2021-01-18T02:19:10.541736"

        data = Database(TOKEN, REST_KEY)

        data_base = data.rest_api(table_to_query, default_query)

        _2017_18 = []
        _2018_19 = []
        _2019_20 = []

        if year == "2018":
            for x in data_base:
                if x["dropbase_ts"] == year_2017_18:
                    _2017_18.append(x)
            self.stats = _2017_18
        elif year == "2019":
            for x in data_base:
                if x["dropbase_ts"] == year_2018_19:
                    _2018_19.append(x)
            self.stats = _2018_19
        elif year == "2020":
            for x in data_base:
                if x["dropbase_ts"] == year_2019_20:
                    _2019_20.append(x)
            self.stats = _2019_20
        else:
            print("Year is not available")

    def get_player_stats(self, name):
        """
        accesses stats to return a dictionary of all stats for given player name

        Parameters
        ----------
        name : str
            The name of a specific player from current season

        Returns
        -------
        x : dict
            Dictionary of all stats for given player name
        """
        for x in self.stats:
            if x["player"] == name:
                return x

        return "Year or player not found"

    def get_all_category(self, categoryCode):
        """
        Accesses stats to get all players stats for a specific stat category e.g. points, assists and returns dictionary

        Parameters
        ----------
        categoryCode : string
            abbreviation of a statistic category e.g. points - 'pts'

        Returns
        -------
        Dictionary of all players stats for a given category
        """
        category = dict()
        for x in self.stats:
            if x[categoryCode] == 'NaN':
                category[x['player']] = 0
            else:
                category[x['player']] = x[categoryCode]
        return category

    def get_top5_category(self, categoryCode):
        """
        Gets and returns dictionary of top 5 players of given category code

        Parameters
        ----------
        categoryCode : str
            abbreviation of a statistic category e.g. points - 'pts'

        Returns
        -------
        first5pairs : dict
            Dictionary of the top 5 players and their stats for the given category
        """
        all_category = self.get_all_category(categoryCode)
        sorted_list = {k: v for k, v in sorted(all_category.items(), key=lambda item: item[1], reverse=True)}
        first5pairs = {k: sorted_list[k] for k in list(sorted_list)[:5]}
        return first5pairs
