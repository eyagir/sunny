

import requests
from bs4 import BeautifulSoup
import sys
import dryscrape
from course_block import course_block



def get_courses(searchPattern, school, prof_dict):

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
    names = []
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

    for name in table.findAll('div', attrs={'class': 'courseName'}):
        #print(name.text)
        names.append(name.text)

    for instructor in table.findAll('div', attrs={'class': 'instructor'}):
        #print(instructor.text)
        instructors.append(instructor.text)

    for day in table.findAll('div', attrs={'class': 'days'}):
        #print(day.text)
        days.append(day.text)

    for time in table.findAll('div', attrs={'class': 'time'}):
        #print(time.text)
        times.append(time.text)

    output = []

    for i in range(len(instructors)):
        if (is_lecture[i]):
            rating = get_rating(instructors[i], prof_dict)
            cBlock = course_block(codes[i], names[i], days[i], times[i], is_lecture[i], instructors[i], rating)
            output.append(cBlock)

    return output

def main():

    search_pattern = input("Enter a course:\t")
    for i in get_courses(search_pattern, 'unc'):
        print(i.content())

def get_rating(name, prof_dict):
    name = name.split(' ')
    name = name[1] + ", " + name[0]
    if (name in prof_dict):
        return(prof_dict[name])
    else :
        return(-1) 


if(__name__ == '__main__'):
    main()


