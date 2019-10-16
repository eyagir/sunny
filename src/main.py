import coursicle_scraper as c_scrape
import course_block
from get_profs import get_profs
import pickle
import os.path
import itertools



def main():

    if (os.path.exists('prof_list.pkl')):
        prof_dict = pickle.load(open('prof_list.pkl', 'rb'))
        #print(prof_dict)
    else:
        prof_dict = get_profs()
        pickle.dump(prof_dict, open('prof_list.pkl', 'wb'))

    subjects = []
    course_possibilities = []
    max = 0
    while(1==1):
        uInput = input("Choose an option and type the number:\n1.\t Add another course.\n2.\t Print course blocks added so far.\n3.\t Print all permutations of courses.\n4.\t Exit program\n")

        if(uInput == '1'):
            search_pattern = input("Enter a course code:\t")
            school = 'unc'
            subjects.append(load_subject(search_pattern, school, prof_dict))

        elif (uInput == '2'):
            for subj in subjects:
                for cblock in subj:
                    print(cblock.content())
        elif(uInput == '3'):
           for cblock in get_optimal_cblocks(subjects):
               print(cblock.content())
        elif (uInput == '4'):
            break


def load_subject(search_pattern, school, prof_dict):
    courses = c_scrape.get_courses(search_pattern, school, prof_dict)

    return courses

def get_optimal_cblocks(subjects):
    max_points = 0

    schedule_temp = []
    
    cblock_temp = ''

    for subj in subjects:

        cblock_temp = ''
        highest = -1
        for cblock in subj:

            

            if(cblock.rating >= highest and not conflict(cblock, schedule_temp)):
                highest = cblock.rating
                cblock_temp = cblock
            
        schedule_temp.append(cblock_temp)
                    
    return schedule_temp       

def conflict(course_block, schedule):
    for block in schedule:
        if (len(set(course_block.get_day_list()).intersection(set(block.get_day_list()))) > 0):
            if (len((set(course_block.get_time_range()).intersection(set(block.get_time_range())))) > 0 ):
                return True
    return False


def get_permutations(course_blocks):
    all_permutations = itertools.permutations(course_blocks)


    return all_permutations
    



def add_prof(course_block):
    return 0

















if(__name__ == '__main__'):
    main()