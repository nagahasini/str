# insert at beginning
class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def insert_at_beginning(head,key):
    temp=Node(key)
    temp.next=head
    return temp

def print_ll(head):
    current=head
    while current is not None:
        print(current.key,end=' -> ')
        current=current.next
    print('None')


head=None
head=insert_at_beginning(head,10)
head=insert_at_beginning(head,20)

print_ll(head)