# -*- coding:utf-8 -*-

class Athlete:
    def __init__(self,a_name,a_dob=None,a_time=[]):
        self.name=a_name
        self.dob=a_dob
        self.time=a_time
    def top3(self):
        b_time=str(sorted(set([sanitize(t) for t in self.time]))[0:3])
        return (b_time)
    def add_time(self,n_time=None):
        self.time.append(n_time)
    def add_times(self,n_times):
        #列表插入要用extend
        self.time.extend(n_times)

def inputlist(txtfile):
    try:
        with open(txtfile) as txt_data:
            txtitem=txt_data.readline()
            txt_out=txtitem.strip().split(",")
            ae=Athlete(txt_out.pop(0),txt_out.pop(0),txt_out)
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
 
sarah=inputlist("sarah2.txt")
print(sarah.name+"'s fastest times are:"+sarah.top3())
julie=inputlist("julie2.txt")
print(julie.name+"'s fastest times are:"+julie.top3())
james=inputlist("james2.txt")
print(james.name+"'s fastest times are:"+james.top3())
mikey=inputlist("mikey2.txt")
print(mikey.name+"'s fastest times are:"+mikey.top3())
veravi=Athlete("veravi")
veravi.add_time("3.21")
print(veravi.top3())
veravi.add_times(["2.94","2.84"])
print(veravi.top3())