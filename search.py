


def sea(matrix,f):
    for i in matrix:
            if f in i:
                return True

    return False

m=[[1,2,3],
   [4,5,6]]

print(sea(m,1))
