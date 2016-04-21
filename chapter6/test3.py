# -*- coding:utf-8 -*-

def inputlist(txtfile):
    try:
        with open(txtfile) as txt_data:
            txtitem=txt_data.readline()
            txt_out=txtitem.strip().split(",")
            txt_DT={}
            txt_DT["name"]=txt_out.pop(0)
            txt_DT['Bday']=txt_out.pop(0)
            txt_DT['time']=sorted(set([sanitize(t) for t in txt_out]))[0:3]
            return(txt_DT)
    except IOError as ioerr:
        print("IO Error!"+str(ioerr))
        return(None)
 
def sanitize(time_string):
    try:
        if "-" in time_string:
            splitter="-"
        elif ":" in time_string:
            splitter=":"
        else:
            return(time_string)
        (mins,secs)=time_string.split(splitter)
        return(mins+"."+secs)
    except TypeError as tyerr:
        print("Type Error!"+str(tyerr))
        return(None)
 
sarah=inputlist("sarah2.txt")
print(sarah['name']+"'s fastest times are:"+str(sarah['time']))
james=inputlist("james2.txt")
print(james['name']+"'s fastest times are:"+str(james['time']))
julie=inputlist("julie2.txt")
print(julie['name']+"'s fastest times are:"+str(julie['time']))
mikey=inputlist("mikey2.txt")
print(mikey['name']+"'s fastest times are:"+str(mikey['time']))
