"""Problem 1 — Traverse a Linked List
Problem
Given the head of a linked list, print all elements.

Example:
Input:
10 → 20 → 30 → 40

Output:
10 20 30 40"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
def linked_list(head):
    current = head
    
    while current is not None:
        print(current.data,end=' ')
        current = current.next
        

head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

head.next = second
second.next = third
third.next = fourth

print("The linked list elements are: ")
linked_list(head)