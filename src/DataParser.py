import requests
import json
import os
import csv


class Database:

    def __init__(self, token, restKey):
        self.restKey = restKey
        self.token = token

    def upload_to_db_from_file(self, file_name):
        url = "https://api2.dropbase.io/v1/pipeline/generate_presigned_url"
        r = requests.post(url, data={'token': self.token})
        if r.status_code != 200:
            print(r.status_code)
            print(r.json())  # detaailed error message
        signed_url = r.json()["upload_url"]
        job_id = r.json()["job_id"]

        path = "/Users/toluadegbehingbe/Desktop/HTN2020/"
        file = file_name + ".csv"

        fh = open(path + file, 'r')
        print(fh.readline())

        r = requests.put(signed_url, data=open(path + file, 'rb'))
        if r.status_code != 200:
            print(r.status_code)
            print(r.json())  # detaailed error message

        return job_id

    def rest_api(self, table_to_query, query):
        if query == "null":
            query = ""
        database_rest_api = "https://query.dropbase.io/SGxHw6efkvLVuhTjAso8UC"
        r = requests.get(database_rest_api + '/' + table_to_query + query, headers={"Authorization": self.restKey})
        if r.status_code != 200:
            print(r.status_code)
            print(r.json())  # detaailed error message

        var1 = json.loads(r.text)
        color_names = []

        for i in range(len(var1)):
            x = var1[i]
            color_names.append(x["color"])

        print(color_names)









