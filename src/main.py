import coursicle_scraper as c_scrape
import course_block





def main():

    course_blocks = []

    while(1==1):
        uInput = input("Choose an option and type the number:\n1.\t Add another course.\n2.\tPrint course blocks added so far.\n3.\t Exit program\n")

        if(uInput == '1'):
            search_pattern = input("Enter a course code:\t")
            school = input("enter a school:\t")
            course_blocks = course_blocks + (load_subject(search_pattern, school))
        elif (uInput == '2'):
            for course in course_blocks:
                print(course.content())
        elif (uInput == '3'):
            break


def load_subject(search_pattern, school):
    courses = c_scrape.get_courses(searchPattern=search_pattern, school=school)
    return courses
    





















if(__name__ == '__main__'):
    main()