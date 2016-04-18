import os

print(os.getcwd())
the_file=open('sketch.txt')
#print(the_file.readline(),end='')
#print(the_file.readline(),end='')
#the_file.seek(0)
for item in the_file:
    print(item,end='')
the_file.close()