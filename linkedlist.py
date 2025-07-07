# 1st sum is
from logging import currentframe


class Node:
    def __init__(self,k):
        self.key=k
        self.next=None



def arr_to_linkedlist(arr):
    if not arr:
        return None

    head=Node(arr[0])
    current=head
    for value in arr[1:]:
        current.next=Node(value)
        current=current.next

    return head

def print_linked_list(head):
    current=head
    while current is not None:
        print(current.key,end='->')
        current=current.next
    print('None')

def count_length_linkedlist(head):
    current=head
    count=0
    while current is not None:
        count+=1
        current=current.next
    return count

def search_in_linkedlist(head,element):
    pos=1
    current=head
    while current is not None:
        if current.key==element:
            return pos
        pos+=1
        current=current.next
    return -1


a=arr_to_linkedlist([1,2,3,9])
print_linked_list(a)
c=count_length_linkedlist(a)
print(c)
s=search_in_linkedlist(a,9)
print(s)

# insert at beginning



