"""Insert at End
Example:
10 → 20 → 30 → 40

Insert 50
10 → 20 → 30 → 40 → 50"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse(head):
    current = head
    
    while current is not None:
        print(current.data, end = ' ')
        current = current.next
        
    print()

def add_new_to_linkedlist(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next 
    
    current.next = new_node
    
    return head

head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)


head.next = second
second.next = third
third.next = fourth

print("before inserting")
traverse(head)

head = add_new_to_linkedlist(head, 9)

print("After inserting")
traverse(head)