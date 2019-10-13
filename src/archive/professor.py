class Professor:
    # A class to represent a professor

    name: str = "None"
    qual: float = 0.0
    diff: float = 0.0
    course: str = ""
    school: str = "University of North Carolina at Chapel Hill"

    def __init__(self, name, qual, diff):
        self.name = name
        self.qual = qual
        self.diff = diff
        print( name + "\nOverall Quality: " + str(qual) + "\nDifficulty: " + str(diff))
    
    def get_name():
        return name

    def get_qual():
        return qual

    def get_diff():
        return diff

    def get_course():
        return course

    def get_school():
        return school

        