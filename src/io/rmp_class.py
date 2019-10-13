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
# <div class="content" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:LoadMore', linkType:'o' } );">Load More</div>
overlapping_element = session.at_xpath("//*[@id='myProfprogressbtnwrap']")
load_more = overlapping_element.exec_sript('node.parentElement.removeChild(node)')
for i in range(5):
    load_more.click()
    print("Fuck")

page = session.body()
#print(page)
parsed_html = BeautifulSoup(page, 'lxml')


#print(parsed_html)
list_of_profs = parsed_html.find('div', attrs = {'id':'body'})
list_of_profs = list_of_profs.find('div', attrs = {'id':'mainContent'})
list_of_profs = list_of_profs.find('div', attrs = {'class':'left-panel'})
list_of_profs = list_of_profs.find('div', attrs = {'class':'side-panel'})
list_of_profs = list_of_profs.find('div', attrs = {'class':'result-list'})
#print(list_of_profs)
list_of_profs = list_of_profs.find_all('li', attrs = {'id': re.compile('my-professor*')})
y = 0
for x in list_of_profs:
    name = x.find('span', attrs = {'class':'name'}).text
    rating = x.find('span', attrs = {'class':'rating'}).text
    print(str(name) , str(rating))
    y += 1
print(y)
