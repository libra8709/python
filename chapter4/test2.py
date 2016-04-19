man=[]
other=[]
try:
    data=open("..\chapter3\sketch.txt")
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
    data.close()
except IOError:
    print("The data file is missing!")
try:
    man_out=open("manspoken.txt","w")
    other_out=open("otherspoken.txt","w")
    print(man,file=man_out)
    print(other,file=other_out)
except IOError:
    print("file error!")
finally:
    man_out.close()
    other_out.close()