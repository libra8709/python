movies=["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
print(movies)
for each_item in movies:
    if isinstance(each_item,list):
        for item in each_item:
            print(item)
    else:
        print(each_item)
    