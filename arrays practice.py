def largest_element(arr):
    maxi=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi=max(arr[i],maxi)
    return maxi

a=largest_element([2,3,1,5,6,0,5,10])
print(a)

def second_largest(arr):
    largest=arr[0]
    slargest=float('inf')

    for i in range(len(arr)):
        if arr[i]>largest:
            slargest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>slargest:
            slargest=arr[i]
    return slargest

b=second_largest([2,3,1,5,6,0])
print(b)

def is_sorted(arr):
    for i in range(len(arr)):
        if arr[i]<=arr[i+1]:
            return True
        else:
            return False
    return True

print(is_sorted([1,3]))

# [1,1,2,2,2,3,3]
def remove_dupli(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[j]==arr[i]:
                j+=1
            else:
                arr[i+1]=arr[j]






print(remove_dupli([1,1,2]))

def consecutive_ones(arr):
    c=0
    maxi=float('-inf')
    for i in range(len(arr)):
        if arr[i]==1:
            c+=1
            maxi=max(maxi,c)
        else:
            c=0

def sortb(arr1):
    for i in range(len(arr1)-1):
        for j in range(len(arr1)-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j] , arr1[j + 1]=arr1[j+1],arr1[j]

    return arr1

print(sortb([2,13,1]))



def bubble_sort(arr3):
    for i in range(1,len(arr3)):
        temp=arr3[i]
        j=i-1
        while j>=0 and arr3[j]>temp:
            arr3[j+1]=arr3[j]
            j-=1
        arr3[j+1]=temp
    return arr3

print(bubble_sort([4,1,8]))










