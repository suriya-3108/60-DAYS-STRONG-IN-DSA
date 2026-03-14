"""Problem (Very Common)

Find the Middle of a Linked List using the Fast & Slow pointer technique.
Example:
10 → 20 → 30 → 40 → 50

Output:
30"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse(head):
    
    current = head
    
    while current is not None:
        print(current.data, end=' ')
        current = current.next
        
    print()


def find_middle(head):
    
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    return slow.data


# Create Linked List
head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth


print("Linked List:")
traverse(head)

middle = find_middle(head)

print("Middle element:", middle)