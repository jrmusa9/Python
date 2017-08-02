x=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,122]

if type(x)== int and x>=100:
    print 'Thats a big number'
elif type(x)== int and x<100:
    print 'Thats a small number'
elif type(x)==str and x.count('')>=50:
    print 'Long sentence'
elif type(x)==str and x.count('')<50:
    print 'Short sentence'
elif type(x)==list and len(x)>10:
    print 'Big List!'
elif type(x)==list and len(x)<10:
    print 'Small List!'




