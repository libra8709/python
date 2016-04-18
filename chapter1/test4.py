def print_lol(the_list):
    for item in the_list:
        if isinstance(item,list):
            print_lol(item)
        else:
            print(item)

movies=["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
print_lol(movies)