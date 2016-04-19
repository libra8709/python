import pickle

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
    with open("manspoken.txt","wb") as man_out:
        pickle.dump(man,man_out)
    with open("otherspoken.txt","wb") as other_out:   
        pickle.dump(other,other_out)
except IOError as err:
    print("file error!"+str(err))
except pickle.PickleError as pierr:
    print("pickle error!"+str(pierr))