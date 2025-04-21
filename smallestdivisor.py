import math
def sums(arr,v):
    s=0
    for i in range(len(arr)):
        s+=math.ceil(float(arr[i]/v))
    return s

def smallest_divisor(arr,t):
    l=1
    h=max(arr)
    while l<=h:
        mid=(l+h)//2
        if sums(arr,mid)<=t:
            h=mid-1
        else:
            l=mid+1
    return l


s=smallest_divisor([1,2,5,9],7)
print(s)



