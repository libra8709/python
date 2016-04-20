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
#james_item=[sanitize(each_t) for each_t in james]
julie=inputlist("julie.txt")
#julie_item=[sanitize(each_t) for each_t in julie]
mikey=inputlist("mikey.txt")
#mikey_item=[sanitize(each_t) for each_t in mikey]
sarah=inputlist("sarah.txt")
#sarah_item=[sanitize(each_t) for each_t in sarah]
print(james)
print(julie)
print(mikey)
print(sarah)
print()
#print(james_item)
#print(julie_item)
#print(mikey_item)
#print(sarah_item)
#print()
print(sorted([sanitize(each_t) for each_t in james]))
print(sorted([sanitize(each_t) for each_t in julie]))
print(sorted([sanitize(each_t) for each_t in mikey]))
print(sorted([sanitize(each_t) for each_t in sarah]))