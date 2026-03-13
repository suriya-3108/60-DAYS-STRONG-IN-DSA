"""Queue Problem
Implement Queue using Stacks
Problem

Implement a Queue using two stacks.
Queue follows FIFO (First In First Out).
You must support these operations:

push(x)   → insert element
pop()     → remove front element
peek()    → return front element
empty()   → check if queue is empty"""

def queue_operations(operations):
    stack1 = []
    stack2 = []
    result = []

    for op, val in operations:

        if op == "push":
            stack1.append(val)

        elif op == "pop":
            if not stack2:
                while stack1:
                    stack2.append(stack1.pop())
            result.append(stack2.pop())

        elif op == "peek":
            if not stack2:
                while stack1:
                    stack2.append(stack1.pop())
            result.append(stack2[-1])

        elif op == "empty":
            result.append(len(stack1) == 0 and len(stack2) == 0)

    return result


ops = [
    ("push",1),
    ("push",2),
    ("peek",None),
    ("pop",None),
    ("empty",None)
]

print(queue_operations(ops))