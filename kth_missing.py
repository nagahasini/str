def miss(arr,k):
    l={}
    l1=[]
    for i in range(1,max(arr)+k+1):
        if i in arr:
            l[i]=0
        else:
            l[i]=1
            l1.append(i)
            if len(l1) == k:
                break


    return l1[k-1]

a=miss([2,3,4,7,11],5)
print(a)