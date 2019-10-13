import requests
import json
from bs4 import BeautifulSoup
import sys
import re
import dryscrape


if 'linux' in sys.platform:
    dryscrape.start_xvfb()


# Read the HTML File
url = "https://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=University+of+North+Carolina+at+Chapel+Hill&schoolID=1232&queryoption=TEACHER"

session = dryscrape.Session()
session.set_attribute('auto_load_images', False)
session.visit(url)

page = session.body()
parsed_html = BeautifulSoup(page, 'lxml')

print(parsed_html)
list_of_profs = parsed_html.find('class', attrs = {'class':'result-list'})
print(list_of_profs)
list_of_profs = parsed_html.find_all("li", attrs = {id: re.compile('my-professor*')})
print(list_of_profs)
