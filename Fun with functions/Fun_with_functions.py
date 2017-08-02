# def odd_even():
#     for i in range(1, 2001):
#         if i%2==0:
#             print 'Number is',i,'and  its even'
#         else:
#             print 'Number is',i,'and its odd'
#     return

# odd_even()


def multiply(arr,b):
    for i in range(0,len(arr)):
        arr[i]*=b
    # print arr
    return arr

# multiply([1,2,3,4],3)


def layered_multiples(arr):
    arr2=[]
    for i in range(0,len(arr)):
        arr2.append([1]*arr[i])
    return arr2

x=layered_multiples(multiply([1,2,3,4],3))

print x

