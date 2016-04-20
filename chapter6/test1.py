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
(s_name,s_Bday)=sarah.pop(0),sarah.pop(0)
print(s_name+"'s fastest times are:"+str(sorted(set([sanitize(each_t) for each_t in sarah]))[0:3]))