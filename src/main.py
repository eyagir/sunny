import coursicle_scraper as c_scrape
import course_block
from get_profs import get_profs
import pickle
import os.path
from schedulebuilder import getOptimal





def main():

    if (os.path.exists('prof_list.pkl')):
        prof_dict = pickle.load(open('prof_list.pkl', 'rb'))
        #print(prof_dict)
    else:
        prof_dict = get_profs()
        pickle.dump(prof_dict, open('prof_list.pkl', 'wb'))

    all_blocks = []
    max = 0
    while(1==1):
        uInput = input("Choose an option and type the number:\n1.\t Add another course.\n2.\t Print course blocks added so far.\n3.\t Print ranked schedules.\n4.\t Exit program\n")

        if(uInput == '1'):
            search_pattern = input("Enter a course code:\t")
            school = 'unc'
            for block in load_subject(search_pattern, school, prof_dict):
                all_blocks.append(block)

        elif (uInput == '2'):
            for block in all_blocks:
                    print(block.content())
        elif(uInput == '3'):
           continue
        elif (uInput == '4'):
            break


def load_subject(search_pattern, school, prof_dict):
    courses = c_scrape.get_courses(search_pattern, school, prof_dict)
    return courses

def optimise_schedule(subjects):
    return(getOptimal(subjects))
    



if(__name__ == '__main__'):
    main()