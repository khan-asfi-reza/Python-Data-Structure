# Basic Node For Linked List
class Node:

    # Constructor method takes data and next node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Returns data when the instance object is called
    def __repr__(self):
        return self.data


# Nodes for queue
class QueueNode:

    def __init__(self, value):
        self.value = value
        self.next = None


# Dynamic Node for doubly linked list
class DynamicNode:
    def __init__(self, previous, next, value):
        self.previous = previous
        self.next = next
        self.value = value
