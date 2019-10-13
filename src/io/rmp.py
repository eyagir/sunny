import requests
import json
from bs4 import BeautifulSoup
import sys

sys.path.append('/hackNC/sunny/src/')
from objects.professor import Professor

def create_professor(id):
    name = ""
    qual = 0.0
    diff = 0.0

    # Grab the html file from the website
    page = requests.get("https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1831912")
    html = page.content
    parsed_html = BeautifulSoup(html, 'html.parser')

    # Print name of the professor
    professor_name = parsed_html.find('html', attrs = {'class':'no-js'})
    professor_name = parsed_html.find('head')
    professor_name = parsed_html.find_all('script')
    name = str(professor_name[6])
    name1 = name.split('professor')
    name2 = name1[1].rstrip(',')
    name = name2

    # Print the Overall Quality of Professor
    overall_qual = parsed_html.find('div',attrs = {'class':'grade'})
    #overall_qual = overall_qual.find('span',attrs = {'class':'score good'})
    for span in overall_qual:
        span = str(span)
        span.strip()
        qual = float(span)

    # Print the Overall Difficulty of Professor
    overall_diff = parsed_html.find('div',attrs = {'class':'breakdown-section difficulty'})
    overall_diff = overall_diff.find('div',attrs = {'class':'grade'})
    for span in overall_diff:
        span = str(span)
        span.strip()
        diff = float(span)

    x = Professor(name,qual,diff)
    return x

create_professor(0)



