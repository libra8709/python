# -*- coding:utf-8 -*-

import pickle
from AthleteList import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as filedata:
            file=filedata.readline()
            filelist=file.strip().split(",")
            ath=AthleteList(filelist.pop(0),filelist.pop(0),filelist)
    except IOError as ioe:
        print("IO Error!"+ioe)
    return(ath)
    
def put_to_store(files_list):
    all_athletes={}
    for flist in files_list:
        ath=get_coach_data(flist)
        all_athletes[ath.name]=ath
    try:
        with open("athletes.pickle","wb") as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioe:
        print("IO Error!"+ioe)
    return (all_athletes)
    
def get_from_store():
    all_athletes={}
    try:
        with open("athletes.pickle","rb") as athf:
            all_athletes=pickle.load(athf)
    except IOError as ioe:
        print("IO Error!"+ioe)
    return(all_athletes)