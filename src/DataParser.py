import requests
import json


class Database:
    """
    This class handles the input and output to the database, we used the Dropbase API to handle database interactions:
    https://www.dropbase.io/

    ...

    Attributes
    ----------

    token: str
        The Dropbase API token
    restKey: str
        The Dropbase API key

    Methods
    -------
    upload_to_db_from_file(file_name)
        uploads a file from the a local machine to the database
    """

    def __init__(self, token, restKey):
        """
        Parameters
        ----------
        token: str
            The Dropbase API token
        restKey: str
            The Dropbase API key
        """
        self.restKey = restKey
        self.token = token

    def upload_to_db_from_file(self, file_name, path):
        """uploads a file from the a local machine to the database.

        Parameters
        ----------
        file_name : str
            name of the file to be uploaded
        path: str
            the path of the file to be uploaded

        Returns
        -------
        job_id
            job id, used to check the status of the job. (Only relavent for early testing)

        Raises
        -------
        ConnectionError
            If there is a problem connecting to the database
        """

        url = "https://api2.dropbase.io/v1/pipeline/generate_presigned_url"
        r = requests.post(url, data={'token': self.token})
        if r.status_code != 200:
            raise ConnectionError(r.json())

        signed_url = r.json()["upload_url"]
        job_id = r.json()["job_id"]

        file = file_name + ".csv"

        fh = open(path + file, 'r')
        print(fh.readline())

        r = requests.put(signed_url, data=open(path + file, 'rb'))
        if r.status_code != 200:
            raise ConnectionError(r.json())

        return job_id

    def rest_api(self, table_to_query, query):
        """Query Dropbase managed database using PostgREST API

        Parameters
        ----------
        table_to_query : str
            The name of the table in the database to query, in this case: nbastats2
        query : str
            Arguments for the query, pass null to get the entire table

        Returns
        -------
        json.loads(r.text)
            a dictionary containing the query data

        Raises
        -------
        ConnectionError
            If there is a problem connecting to the database
        """
        if query == "null":
            query = ""
        database_rest_api = "https://query.dropbase.io/SGxHw6efkvLVuhTjAso8UC"  # our database URL
        r = requests.get(database_rest_api + '/' + table_to_query + query, headers={"Authorization": self.restKey})
        if r.status_code != 200:
            raise ConnectionError(r.json())

        return json.loads(r.text)
