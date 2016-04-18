import os

the_file=open('sketch.txt')
for item in the_file:
    if not item.find(":")==-1:
        (role,line_spoken)=item.split(":",1)
        print(role,end='')
        print("said",end='')
        print(line_spoken,end='')
the_file.close()