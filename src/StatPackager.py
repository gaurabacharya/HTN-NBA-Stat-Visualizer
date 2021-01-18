from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 

class StatPackager:
    def __init__(self, url, year):
        self.url = url.format(year)
        self.year = year
        self.html = urlopen(url)
        self.soup = bs(self.html, 'html.parser')

    def get_header(self):
        headers = [th.getText() for th in self.soup.findAll('tr', limit=2)[0].findAll('th')]
        headers = headers[1:]
        return headers
    
    def get_rows(self):
        all_rows = self.soup.findAll('tr')[1:]
        data = [[td.getText() for td in all_rows[i].findAll('td')] for i in range(len(all_rows))]
        return data
    
    def to_csv(self, filename, header, data):
        f = open(filename, 'w')
        header_string = ''
        for title in header:
            header_string += title + ','

        header_string = header_string[:-1]
        header_string += '\n'
        f.write(header_string)

        for row in data:
            row_string = ''
            for column in row:
                row_string += column + ','
            row_string += '\n'
            f.write(row_string)
            
        f.close()






