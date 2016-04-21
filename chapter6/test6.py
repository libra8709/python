# -*- coding:utf-8 -*-

class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_time=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_time)
    def top3(self):
        b_time=str(sorted(set([sanitize(t) for t in self]))[0:3])
        return (b_time)

def inputlist(txtfile):
    try:
        with open(txtfile) as txt_data:
            txtitem=txt_data.readline()
            txt_out=txtitem.strip().split(",")
            ae=AthleteList(txt_out.pop(0),txt_out.pop(0),txt_out)
            return(ae)
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

veravi=AthleteList("veravi")
veravi.append("3.21")
print(veravi.top3())
veravi.extend(["2.94","2.84"])
print(veravi.top3())
sarah=inputlist("sarah2.txt")
print(sarah.name+"'s fastest times are:"+sarah.top3())