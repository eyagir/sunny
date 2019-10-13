import requests
import json
from bs4 import BeautifulSoup
import sys
import re
import dryscrape
import time


def get_profs():
    if 'linux' in sys.platform:
        dryscrape.start_xvfb()

    prof_dict = {}

    # Read the HTML File
    url = "https://www.ratemyprofessors.com"
    session = dryscrape.Session()
    session.set_attribute('auto_load_images', False)
    session.visit(url)
    url = "https://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=University+of+North+Carolina+at+Chapel+Hill&schoolID=1232&queryoption=TEACHER"
    session.visit(url)
    # <div class="content" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:LoadMore', linkType:'o' } );">Load More</div>
    load_more = session.at_xpath("//*[@id='mainContent']/div[1]/div/div[5]/div/div[1]")
    for i in range(292):
        load_more.click()

    page = session.body()
    parsed_html = BeautifulSoup(page, 'lxml')


    #print(parsed_html)
    list_of_profs = parsed_html.find('div', attrs = {'id':'body'})
    list_of_profs = list_of_profs.find('div', attrs = {'id':'mainContent'})
    list_of_profs = list_of_profs.find('div', attrs = {'class':'left-panel'})
    list_of_profs = list_of_profs.find('div', attrs = {'class':'side-panel'})
    list_of_profs = list_of_profs.find('div', attrs = {'class':'result-list'})
    #print(list_of_profs)
    list_of_profs = list_of_profs.find_all('li', attrs = {'id': re.compile('my-professor*')})

    for x in list_of_profs:
        name = x.find('span', attrs = {'class':'name'}).text
        name = name.split(" ")
        name[1] = re.sub('\s+', '', name[1])
        name = name[0] + " " + name[1][:len(name[1])-2]
        name = re.sub(r'\d+', '', name)
        rating = x.find('span', attrs = {'class':'rating'}).text
        prof_dict[str(name)] = float(str(rating))
    return prof_dict
