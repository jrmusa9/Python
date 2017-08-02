print 'x ',
for i in range(1,13):
    print '%3s' %i,
print '\r'

for y in range(1,13):
    print '%-2s' %y,'\b',
    for x in range(1,13):
        x= x*y
        print '%3s' %x,
    print '\r'


