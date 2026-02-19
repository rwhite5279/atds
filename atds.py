#!/usr/bin/env python3
"""
atds.py
A collection of data types for the Advanced Topics class.
Currently includes the Stack, Queue, and Deque classes.
"""
__author__ = "Richard White"
__version__ = "2026-02-12"

class Stack():
    def __init__(self):
        """Create an empty stack (as a list)"""
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def peek(self):
        """Returns the result if one available, otherwise None"""
        if len(self.stack) > 0:
            return self.stack[-1]
    def pop(self):
        """Returns the result if one available, otherwise None"""
        if len(self.stack) > 0:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0
    def __repr__(self):
        return str(self.stack)
    
class Queue(object):
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return len(self.queue) == 0
    def __repr__(self):
        return str(self.queue)

class Deque(object):
    """Defines a deque with the head (front) at 0
    and the tail (rear) at -1.
    """
    def __init__(self):
        self.deque = []
    def add_front(self, item):
        self.deque.insert(0, item)
    def add_rear(self, item):
        self.deque.append(item)
    def peek_front(self):
        if len(self.deque) > 0:
            return self.deque[0]
    def peek_rear(self):
        if len(self.deque) > 0:
            return self.deque[-1]
    def remove_front(self):
        if len(self.deque) > 0:
            return self.deque.pop(0)
    def remove_rear(self):
        if len(self.deque) > 0:
            return self.deque.pop(-1)
    def size(self):
        return len(self.deque)
    def is_empty(self):
        return len(self.deque) == 0

def main():
    pass

if __name__ == "__main__":
    main()


    
