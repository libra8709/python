# -*- coding:utf-8 -*-
import athletemodel

the_files=["../chapter6/james2.txt","../chapter6/julie2.txt","../chapter6/mikey2.txt","../chapter6/sarah2.txt"]
data=athletemodel.put_to_store(the_files)
data_copy=athletemodel.get_from_store()
for each_data in data_copy:
    print(data_copy[each_data].name+" "+data_copy[each_data].dob)