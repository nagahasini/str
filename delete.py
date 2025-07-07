from multiprocessing.dummy import current_process


class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def delete_node_atposition(node):
    node.key=node.next.key
    node.next=node.next.next

def print_list(head):
    current=head
    while current is not None:
        print(current.key,end=' -> ')
        current=current.next
    print("None")


def length_of_list(head):
    count=0
    current=head
    while current is not None:
        count+=1
        current=current.next
    return count




# find middle of linked list
def middle_of_list(head):
    current=head
    count=length_of_list(head)
    for i in range(count//2):
        current=current.next
    return current.key

# nth node from end of linkedlist
def find_nth_from_last(head,x):
    if head == None:
        return
    count=length_of_list(head)
    current=head
    for i in range(count-x):
        current=current.next
    print(current.key)

# optimal approach
def nth_from_last(head,x):
    if head==None:
        return
    first=head
    for i in range(x):
        first= first.next
    second=head
    while first!=None:
        first=first.next
        second=second.next
    print(second.key)





head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
print_list(head)
print(find_nth_from_last(head,1))















