"""for item in range(10):
    print(item)
"""    
def print_lol(the_list,the_switch=False,the_no=0):
    for item in the_list:
        if isinstance(item,list):
            print_lol(item,the_switch,the_no+1)
        else:
            if the_switch:
                for item2 in range(the_no):
                    print("\t",end='')
            print(item)
            
movies=["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
print_lol(movies)
print_lol(movies,True)
print_lol(movies,True,4)