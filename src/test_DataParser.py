from unittest import TestCase

from src.Commands import Commands
from src.DataParser import Database


class TestDatabase(TestCase):
    TOKEN = "hjiAYex3PbXKy2SBwPKkSV"
    REST_KEY = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoiU0d4SHc2ZWZrdkxWdWhUakFzbzhVQyIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6Ik5QUjRRZXY0bGIyTWY1STdEdlFsbUVScGNwTURkT2tuMWlJV21ORTVLbjdHUjJoRTN6ZkFSSmNMekJnb093N2EiLCJpYXQiOjE2MTQzMjY0MzMsImV4cCI6MTYxNDMyNjczMywiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJvQ3NQODJqOTY2dTgyOXpxN0xoVU00In0.v38NpmttsxHCfiMfiuZz2MHaLOcVeSnVB-JEf7g6AJc"
    query = '?select=player,pts,dropbase_ts'
    default_query = "null"
    table_to_query = "nbastats2"

    def test_rest_api(self):
        data = Database(self.TOKEN, self.REST_KEY)

        data_base = data.rest_api(self.table_to_query, self.default_query)

        print(data_base)

        year_2017_18 = "2021-01-18T01:51:29.180433"
        year_2018_19 = "2021-01-18T02:12:57.530854"
        year_2019_20 = "2021-01-18T02:19:10.541736"

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

    def tests2(self):

        stats = Commands.get_player_stats(self, "Kyle Korver", "2017")
        print(stats)
