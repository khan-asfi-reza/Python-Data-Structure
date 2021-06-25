# Stack implementation using a linked list.
# Node class
from Nodes.nodes import QueueNode as Node


class Stack:
    class EmptyStackError(Exception):
        def __init__(self, message="Peeking from an empty stack"):
            self.message = message
            super().__init__(self.message)

    # Initialize Stack using multiple data
    def __create(self, args):
        current = None
        for each in args:
            node = Node(each)
            self.size += 1
            if each == args[0]:
                self.head = node
            else:
                current.next = node
            current = node

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self, *args):
        self.head = None
        self.size = 0
        self.__create(list(args))

    # String representation of the stack
    def __str__(self):
        cur = self.head
        out = ""
        while cur:
            if cur.next is not None:
                out += str(cur.value) + ", "
            else:
                out += str(cur.value)
            cur = cur.next
        return out

        # Get the current size of the stack

    def getSize(self):
        return self.size

    # Returns size of the queue
    def __len__(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise self.EmptyStackError()
        return self.head.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise self.EmptyStackError()
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        self.head = remove
        return remove.value

    # Make stack an array
    def toList(self):
        if self.isEmpty():
            return []
        else:
            lst = []
            current = self.head
            while current:
                lst.append(current.value)
                current = current.next
            return lst
