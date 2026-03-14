"""Problem 2 — Insert Node at Beginning
Example:

Before:
10 → 20 → 30 → 40
Insert 5 at beginning

After:
5 → 10 → 20 → 30 → 40"""

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
    
    new_node.next = head
    head = new_node
    
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