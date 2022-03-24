def myprint(l):
    for a in l:
        if a % 2 == 0 and a % 3 == 0 :
            print('Foo Bar', a)
        elif a % 2 == 0 :
            print('Foo', a)
        elif a % 3 == 0 :
            print('Bar', a)
    
myprint(range(1,100))
     