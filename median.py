def median(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    t=n+m
    l=sorted(arr1+arr2)
    m=0
    for i in range(len(l)):
        if t%2==0:
            m=l[t//2]+l[t//2+1]//2
        else:
            m=l[t//2]
    return m

r=median([2,3,4],[1,3])
print(r)

