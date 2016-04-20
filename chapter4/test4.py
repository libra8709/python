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
            
man=[]
other=[]
try:
    with open("..\chapter3\sketch.txt") as data:
        for item in data:
            try:
                (role,line_spoken)=item.split(":",1)
                line_spoken=line_spoken.strip()
                if role=="Man":
                    man.append(line_spoken)
                elif role=="Other Man":
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError:
    print("The data file is missing!")
try:
    with open("manspoken.txt","w") as man_out:
        print_lol(man,False,0,man_out)
    with open("otherspoken.txt","w") as other_out:   
        print_lol(other,False,0,other_out)
except IOError as err:
    print("file error!"+str(err))