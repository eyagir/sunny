class course_block:

    def __init__(self, course_code, course_name, days, time, is_lecture, professor, rating):
        self.course_code = course_code
        self.course_name = course_name
        self.days = days
        self.time = time
        self.is_lecture = is_lecture
        self.professor = professor
        self.rating = rating

    def content(self):
        return("%s %s %s\twith\t%s (%s)\ton\t%s at %s" % ( 'LEC' if self.is_lecture else 'REC' , self.course_code, self.course_name[:20], self.professor, round(self.rating)*'*',self.days, self.time))

    def get_time_range(self):
        timeRange = self.time.split('-')
        for i in range(2):
            x = 0
            if ('pm' in timeRange[i] and '12:' not in timeRange[i]):
                x = 1200
            
            timeRange[i] = timeRange[i].replace('am', '')
            timeRange[i] = timeRange[i].replace('pm', '')
            timeRange[i] = timeRange[i].replace(':', '')

            timeRange[i] = int(timeRange[i]) + x

        return range(timeRange[0], timeRange[1])

    def get_day_list(self):
        output = []
        for i in range(len(self.days)):
            output.append(self.days[i])
        return output
            