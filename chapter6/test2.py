# -*- coding:utf-8 -*-

def inputlist(txtfile):
    try:
        with open(txtfile) as txt_data:
            txtitem=txt_data.readline()
            txt_out=txtitem.strip().split(",")
            return(txt_out)
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
sarah_data={}
sarah_data["name"]=sarah.pop(0)
sarah_data['Bday']=sarah.pop(0)
sarah_data['time']=sarah
print(sarah_data['name']+"'s fastest times are:"+str(sorted(set([sanitize(t) for t in sarah_data['time']]))[0:3]))