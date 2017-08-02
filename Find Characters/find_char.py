arr= ['hello','world','my','name','is','Anna','otro']
char= 's'
newArr=[]

for i in range(0,len(arr)):
    if arr[i].find(char) > -1:
        newArr.append(arr[i])
print newArr