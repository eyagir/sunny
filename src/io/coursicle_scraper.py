

import requests
from bs4 import BeautifulSoup
import sys
import dryscrape
from course_block import course_block



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

    codes = []
    instructors = []
    days = []
    times = []
    is_lecture = []

    for courseNumber in table.findAll('div', attrs={'class': 'courseNumber'}):
        codes.append(courseNumber.text)
        cNum = courseNumber.text[-3:]
        if(int(cNum) < 600):
            is_lecture.append(True)
        else:
            is_lecture.append(False)

    for instructor in table.findAll('div', attrs={'class': 'instructor'}):
        instructors.append(instructor.text)

    for day in table.findAll('div', attrs={'class': 'days'}):
        days.append(day.text)

    for time in table.findAll('div', attrs={'class': 'time'}):
        times.append(time.text)

    output = []

    for i in range(len(instructors)):
        cBlock = course_block(codes[i], days[i], times[i], is_lecture[i], instructors[i])
        output.append(cBlock)

    return output

def main():
    search_pattern = input("Enter a course:\t")
    for i in get_courses(search_pattern, 'unc'):
        print(i.content())

if(__name__ == '__main__'):
    main()