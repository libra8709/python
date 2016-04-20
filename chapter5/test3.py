# _*_ coding:utf-8 _*_

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

james_item=[]
julie_item=[]
mikey_item=[]
james=inputlist("james.txt")
for each_t in james:
    james_item.append(sanitize(each_t))
julie=inputlist("julie.txt")
for each_t in julie:
    julie_item.append(sanitize(each_t))
mikey=inputlist("mikey.txt")
for each_t in mikey:
    mikey_item.append(sanitize(each_t))
print(james_item)
print(julie_item)
print(mikey_item)
print()
print(sorted(james_item))
print(sorted(julie_item))
print(sorted(mikey_item))