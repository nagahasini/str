def max_1(matrixi):
    maxi=-1
    maxin=-1

    for i in range(len(matrixi)):
        total=sum(matrixi[i])
        if total>maxi:
            maxi=total
            maxin=i
    return maxin



rows=int(input("enter num of rows:  " ))
cols=int(input("no of cols : "))

matri=[list(map(int,input().split())) for _ in range(rows)]
a=max_1(matri)
print(a)



