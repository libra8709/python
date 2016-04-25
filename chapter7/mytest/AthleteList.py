# -*- coding:utf-8 -*-
from sanitize import sanitize

class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_time=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_time)
    def top3(self):
        b_time=str(sorted(set([sanitize(t) for t in self]))[0:3])
        return (b_time)