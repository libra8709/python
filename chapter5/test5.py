# _*_ conding:utf-8 _*_

def inputlist(txtfile):
    try:
        with open(txtfile) as txt_data:
            txtitem=txt_data.readline()
            txt_out=txtitem.strip().split(",")
            return txt_out
    except IOError as ioerr:
        print("IO Error!"+str(ioerr))
        
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

james=inputlist("james.txt")
julie=inputlist("julie.txt")
mikey=inputlist("mikey.txt")
sarah=inputlist("sarah.txt")
james_item=sorted([sanitize(each_t) for each_t in james])
julie_item=sorted([sanitize(each_t) for each_t in julie])
mikey_item=sorted([sanitize(each_t) for each_t in mikey])
sarah_item=sorted([sanitize(each_t) for each_t in sarah])

UNjames=[]
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
print(UNsarah[0:3])