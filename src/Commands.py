from src.DataParser import Database


class Commands:

    def get_player_stats(self, name, year):

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

        # print(self.data_base)

        _2017_18 = []
        _2018_19 = []
        _2019_20 = []

        for x in data_base:
            if x["dropbase_ts"] == year_2017_18:
                _2017_18.append(x)
            if x["dropbase_ts"] == year_2018_19:
                _2018_19.append(x)
            if x["dropbase_ts"] == year_2019_20:
                _2019_20.append(x)

        if year == "2017":
            data = _2017_18
            for x in data:
                if x["player"] == name:
                    return x
        if year == "2018":
            data = _2018_19
            for x in data:
                if x["player"] == name:
                    return x
        if year == "2019":
            data = _2019_20
            for x in data:
                if x["player"] == name:
                    return x

        return "Year or player not found"
