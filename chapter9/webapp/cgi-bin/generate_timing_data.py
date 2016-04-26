# -*- coding:utf-8 -*-
import cgi
import yate
import athletemodel
#import cgitb

#cgitb.enable()

ale=athletemodel.get_from_store()
form_data=cgi.FieldStorage()
atlete_name=form_data["which_athlete"].value
print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete:"+ale[atlete_name].name+",DOB:"+ale[atlete_name].dob+"."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(ale[atlete_name].top3))
print(yate.include_footer({"Home":"/index.html","Select another one":"generate_list.py"}))