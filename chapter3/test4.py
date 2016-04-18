import os

if os.path.exists('sketch.txt'):
    the_file=open('sketch.txt')
    try:
        for item in the_file:
            (role,line_spoken)=item.split(":",1)
            print(role,end='')
            print("said",end='')
            print(line_spoken,end='')
    except:
        pass
    the_file.close()
else:
    print("Sorry,The data file is missing!")