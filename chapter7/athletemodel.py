# -*- coding:utf-8 -*-

import pickle
from AthleteList import AthleteList

def get_coach_data(filename):
    
    
def put_to_store(files_list):
    all_athletes={}
    for flist in files_list:
        try:
            with open(flist) as data:
                data_txt=data.readline()
                datalist=data_txt.strip.split(",")
                all_athletes=AthleteList(datalist.pop(0),datalist.pop(0),datalist)
        except: