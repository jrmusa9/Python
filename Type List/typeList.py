x=['Hi',5,'Anna',10]
sum=0
txt=''
for i in range(0,len(x)):
    if type(x[i])==int:
        sum+=x[i]
    elif type(x[i])==str:
        txt+=x[i]+' '
if sum and txt:
    print 'Thi is a mixed list'
    print 'String is:',txt
    print 'Sum is:',sum
elif sum:
    print 'Thi is a list of numbers'
    print 'Sum is:',sum
elif txt:
    print 'Thi is a list of strings'
    print 'String is:',txt
        




