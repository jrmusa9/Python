for count in range(1, 1001):
    if count%2==1:
        print count

for count in range(5,1000001):
    if count%5==0:
        print count


a = [1, 2, 5, 10, 255, 3]
count=0
for el in range(0,len(a)):
    count+=a[el]
    print count




a = [1, 2, 5, 10, 255, 3]
count=0
for el in range(0,len(a)):
    count+=a[el]

print count/len(a)

