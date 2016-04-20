# -*- coding:utf-8 -*-

def inputlist(txtfile):
    try:
        with open(txtfile) as txt_data:
            txtitem=txt_data.readline()
            txt_out=txtitem.strip().split(",")
            return txt_out
    except IOError as ioerr:
        print("IO Error!"+str(ioerr))

james=inputlist("james.txt")
james2=sorted(james)
print(james2)
julie=inputlist("julie.txt")
julie2=sorted(julie)
print(julie2)
mikey=inputlist("mikey.txt")
mikey2=sorted(mikey)
print(mikey2)

