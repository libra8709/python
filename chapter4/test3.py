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
        print(man,file=man_out)
    with open("otherspoken.txt","w") as other_out:   
        print(other,file=other_out)
except IOError as err:
    print("file error!"+str(err))