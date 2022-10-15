import datetime
from operator import itemgetter
class Time:  
    def __init__(self):
        #start time is 8:00 Am
        self.time = datetime.datetime(2022, 9, 2, 8, 0, 0)
        self.time_before_nine = []
        self.time_before_ten = []
        self.time_before_one = []
    #calculate miles per minute and add it to time
    def delivered_at(self, start_time, distance):

        mpm = 18 / 60 / 60
        mps = distance / mpm

        start_time += datetime.timedelta(seconds=mps)
        return start_time
