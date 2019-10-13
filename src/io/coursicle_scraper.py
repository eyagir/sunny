import requests
from bs4 import BeautifulSoup
import sys
import dryscrape


def get_courses(searchPattern, school):

    if 'linux' in sys.platform:
        # start xvfb in case no X is running. Make sure xvfb
        # is installed, otherwise this won't work!
        dryscrape.start_xvfb()

    url = "https://www.coursicle.com/" + school + "/#search=" + searchPattern

    session = dryscrape.Session()
    session.set_attribute('auto_load_images', False)
    session.visit(url)

    response = session.body()

    soup = BeautifulSoup(response, 'lxml')
    table = soup.find('div', attrs={'id': 'show_results'})

    instructors = []
    days = []
    times = []
    types = []

    for type in table.findAll('div', attrs={'class': 'courseNumber'}):
        type = type.text[-3:]
        if(int(type) >= 600):
            types.append("REC")
        else:
            types.append("LEC")

    for instructor in table.findAll('div', attrs={'class': 'instructor'}):
        instructors.append(instructor.text)

    for day in table.findAll('div', attrs={'class': 'days'}):
        days.append(day.text)

    for time in table.findAll('div', attrs={'class': 'time'}):
        times.append(time.text)

    output = []

    for i in range(len(instructors)):
        output.append("%s %s:\t%s on %s at %s" %
                    (types[i], i, instructors[i], days[i], times[i]))

    return output

def main():
    for i in get_courses('comp 411', 'unc'):
        print(i)

if(__name__ == '__main__'):
    main()