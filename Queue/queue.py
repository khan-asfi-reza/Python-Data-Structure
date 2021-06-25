# Queue
import random
import string
import sys
import time


class Queue:
    # Create Queue
    def __init__(self):
        self.__queue = []

    # Modifies the whole new Queue
    def modify_queue(self, q):
        self.__queue = q

    # Returns the queue
    def get_queue(self):
        return self.__queue

    # Checks if queue is empty
    def isEmpty(self):
        return len(self.__queue) == 0

    # Inserts into Queue
    def enqueue(self, val):
        self.__queue.insert(0, val)

    # Removes from queue
    def dequeue(self):
        return self.__queue.pop()

    # Returns size
    def size(self):
        return len(self.__queue)

    # Prints queue
    def print_queue(self):
        print(self.__queue.__repr__())

    def dequeue_item(self):
        return self.__queue[-1]



