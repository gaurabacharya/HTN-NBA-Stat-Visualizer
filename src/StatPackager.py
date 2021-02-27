from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


class StatPackager:
    """
    This class uses beautiful soup to web scrape an NBA statistics table from
    https://www.basketball-reference.com

    Attributes
    ----------
    url : str
        a string regarding the url of basketball-reference page for a specific season
    year : int
        the year representing a specific season
    soup : html data
        nested data structure with html code from webpage from given url

    Methods
    -------
    get_header(url, year)
        Returns the table categories from webpage as a list from the table header after removing html tags
    get_rows()
        Returns each row of data in table from webpage after removing html tags
    to_csv(filename, header, data)
        Creates a csv file imitating webpage format using data from header and rows
    """
    def __init__(self, url, year):
        """
        Parameters
        ----------
        url : str
            a string regarding the url of basketball-reference page for a specific season
        year : int
            the year representing a specific season
        """
        self.url = url.format(year)
        self.year = year
        html = urlopen(url)
        self.soup = bs(html, 'html.parser')

    def get_header(self):
        """
        Returns the categories from webpage as a list from the table header after removing html tags
        Returns
        -------
        headers : list
            the categories from webpage as a list from the table header
        """
        headers = [th.getText() for th in self.soup.findAll('tr', limit=2)[0].findAll('th')]
        headers = headers[1:]
        return headers

    def get_rows(self):
        """
        Returns each row of data in table from webpage after removing html tags

        Returns
        -------
        data : list
            each row of data in table from webpage
        """
        all_rows = self.soup.findAll('tr')[1:]
        data = [[td.getText() for td in all_rows[i].findAll('td')] for i in range(len(all_rows))]
        return data

    def to_csv(self, filename, header, data):
        """
        Creates a csv file imitating webpage format using data from header and rows

        Parameters
        ----------
        filename : str
            filepath needed to save csv file
        header : list
             table categories from webpage as a list
        data : list
            each row of data in table from webpage
        """
        f = open(filename, 'w')
        header_string = ''
        for title in header:
            header_string += title + ','

        # header_string = header_string[:-1]
        header_string += '\n'
        f.write(header_string)

        for row in data:
            row_string = ''
            for column in row:
                row_string += column + ','
            row_string += '\n'
            f.write(row_string)

        f.close()
