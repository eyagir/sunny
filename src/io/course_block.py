class course_block:

    def __init__(self, course_code, days, time, is_lecture, professor):
        self.course_code = course_code
        self.days = days
        self.time = time
        self.is_lecture = is_lecture
        self.professor = professor

    def content(self):
        return("%s %s\twith\t%s\ton\t%s at %s" % ( 'LEC' if self.is_lecture else 'REC' , self.course_code, self.professor, self.days, self.time))