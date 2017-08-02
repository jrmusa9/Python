words= "It's thanksgiving day. It's my birthday,too!"
print words.find('day')

x= [2, 54, -2, 7, 12, 98]
print min(x), max(x)

x= ["hello",2,54,-2,7,12,98,"world"]
print x[len(x)-1],x[0]

y= [] 
y.append(x[len(x)-1])
y.append(x[0])
print y


print 'new'
x=[19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
first=x[0:len(x)/2]
second=x[(len(x)/2)+1:len(x)]
second.insert(0,first)

print second



