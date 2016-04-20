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

james=inputlist("james.txt")
julie=inputlist("julie.txt")
mikey=inputlist("mikey.txt")
sarah=inputlist("sarah.txt")
james_item=sorted(set([sanitize(each_t) for each_t in james]))[0:3]
julie_item=sorted(set([sanitize(each_t) for each_t in julie]))[0:3]
mikey_item=sorted(set([sanitize(each_t) for each_t in mikey]))[0:3]
sarah_item=sorted(set([sanitize(each_t) for each_t in sarah]))[0:3]
print(james_item)
print(julie_item)
print(mikey_item)
print(sarah_item)
"""UNjames=[]
UNjulie=[]
UNmikey=[]
UNsarah=[]
for item in james_item:
    if item not in UNjames:
        UNjames.append(item)
for item in julie_item:
    if item not in UNjames:
        UNjulie.append(item)
for item in mikey_item:
    if item not in UNjames:
        UNmikey.append(item)
for item in sarah_item:
    if item not in UNjames:
        UNsarah.append(item)
print(UNjames[0:3])
print(UNjulie[0:3])
print(UNmikey[0:3])
print(UNsarah[0:3])"""