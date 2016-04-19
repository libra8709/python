import pickle
import sys

def print_lol(the_list,the_switch=False,the_no=0,out=sys.stdout):
    for item in the_list:
        if isinstance(item,list):
            print_lol(item,the_switch,the_no+1,out)
        else:
            if the_switch:
                for item2 in range(the_no):
                    print("\t",end='',file=out)
            print(item,file=out)

try:
    with open("manspoken.txt","rb") as man:
        mans=pickle.load(man)
        print_lol(mans)
    with open("otherspoken.txt","rb") as other:
        others=pickle.load(other)
        print_lol(other)
except pickle.PickleError as pierr:
    print("pickle error!"+str(pierr))
except IOError as ioerr:
    print("IO error!"+str(ioerr))