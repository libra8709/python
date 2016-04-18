#import os

man=[]
other=[]
try:
#    print(os.getcwd())
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
print(man)
print(other)