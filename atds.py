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

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data = new_data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]" 

class UnorderedList(object):
    def __init__(self):
        self.head = None
    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def length(self):
        node_count = 0
        current = self.head
        while current != None:
            node_count += 1
            current = current.get_next()
        return node_count

    def is_empty(self):
        return self.head == None
    
    def remove(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            else:
                previous = current
                current = current.get_next()
        return # default





    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result     

def main():
    print("Testing the UnorderedList class")
    tests_passed = 0
    try:
        ul = UnorderedList()
        tests_passed += 1
        print("Test passed: UnorderedList object created")
    except:
        print("Test failed: couldn't create UnorderedList object")

    try:
        if ul.is_empty():
            tests_passed += 1
            print("Test passed: .is_empty() method detected empty list")
        else:
            print("Test failed: .is_empty() method didn't understand that list is empty")
    except:
        print("Test failed: .is_empty method unavailable")
    
    try:
        if ul.length() == 0:
            tests_passed += 1
            print("Test passed: .length() correctly identified a length of 0")
        else:
            print("Test failed: .length() didn't identify a length of 0")
    except:
        print("Test failed: .length() method unavailable")
        
    try:
        ul.add(4)
        ul.add(3)
        ul.add(2)
        ul.add(1)
        ul.add(0)
        tests_passed += 1
        print("Test passed: five items added")
    except:
        print("Test failed: couldn't add items")
    
    try:
        if not ul.is_empty():
            tests_passed += 1
            print("Test passed: .is_empty() method identified that list is no longer empty")
        else:
            print("Test failed: .is_empty() method thought list was empty, and it isn't")
    except:
        print("Test failed: .is_empty method unavailable")
    
    try:
        if ul.length() == 5:
            tests_passed += 1
            print("Test passed: .length() correctly identified a length of 5")
        else:
            print("Test failed: .length() didn't identify a length of 5")
    except:
        print("Test failed: .length() method unusable")
     
    try:
        result = str(ul)         # Try using __repr__
        if result == "UnorderedList[0,1,2,3,4,]":
            tests_passed += 1
            print("Test passed: __repr__ returning correct values:")
            print(result)
        else:
            print("Test failed: __repr__ returned " + result)
            print("Expected: UnorderedList[0,1,2,3,4,]")
        
    except:
        print("Test failed: couldn't reference __repr__ method")
    
    try:
        if not ul.search(5):
            tests_passed += 1
            print("Test passed: .search() method correctly identified that 5 isn't on list")
        else:
            print("Test failed: .search() method thought 5 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")
        
    try:
        if ul.search(3):
            tests_passed += 1
            print("Test passed: .search() method correctly identified that 3 is on list")
        else:
            print("Test failed: .search() method thought 3 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")
    
    try:
        ul.remove(0)
        if str(ul) == "UnorderedList[1,2,3,4,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from beginning of list")
        else:
            print("Test failed: .remove() didn't remove item from beginning of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")

    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(1)
        if str(ul) == "UnorderedList[0,2,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from middle of list")
        else:
            print("Test failed: .remove() didn't remove item from middle of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
        
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(2)
        if str(ul) == "UnorderedList[0,1,]":
            tests_passed += 1
            print("Test passed: .remove() successfully removed item from end of list")
        else:
            print("Test failed: .remove() didn't remove item from end of list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.remove(3)
        if str(ul) == "UnorderedList[0,1,2,]":
            tests_passed += 1
            print("Test passed: .remove() successfully didn't remove item from list")
        else:
            print("Test failed: .remove() failed in not removing a non-existent item from list")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(0)
        ul.add(1)
        ul.add(0)
        print("Attempting multiple remove")
        print("Before remove: " + str(ul))
        ul.remove(0)
        print("After remove: " + str(ul))
        result = ul.search(0)
        if not result:
            tests_passed += 1
            print("Test passed: .remove() successfully removed multiple items")
        else:
            print("Test failed: .remove() didn't remove multiple items")
    except:
        print("Test failed: .remove() method unavailable or not working?")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.append(3)
        if str(ul) == "UnorderedList[0,1,2,3,]":
            tests_passed += 1
            print("Test passed: .append() successfully appended item to list")
        else:
            print("Test failed: .append() didn't append item to list")
    except:
        print("Test failed: .append() method unavailable or not working?")
    
    try:
        result = ul.index(1)
        if result == 1:
            tests_passed += 1
            print("Test passed: .index() successfully found item on list")
        else:
            print("Test failed: .index() failed to find item on list")
    except:
        print("Test failed: .index() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.insert(0, -1)
        if str(ul) == "UnorderedList[-1,0,1,2,]":
            tests_passed += 1
            print("Test passed: .insert() successfully inserted value at beginning of list")
        else:
            print("Test failed: .insert() didn't correctly insert at beginning of list")
    except:
        print("Test failed: .insert() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.insert(2,3)
        if str(ul) == "UnorderedList[0,1,3,2,]":
            tests_passed += 1
            print("Test passed: .insert() successfully inserted values in middle of list")
        else:
            print("Test failed: .insert() didn't correctly insert values in middle of list")
    except:
        print("Test failed: .insert() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop()
        if str(ul) == "UnorderedList[0,1,]":
            tests_passed += 1
            print("Test passed: .pop() successfully removed last item from list")
        else:
            print("Test failed: .pop() didn't remove last item from list correctly")
    except:
        print("Test failed: .pop() method unavailable? (or __repr__ not working?)")
    
    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop(0)
        if str(ul) == "UnorderedList[1,2,]":
            tests_passed += 1
            print("Test passed: .pop(0) successfully removed first item from list")
        else:
            print("Test failed: .pop(0) didn't remove first item from list correctly")
    except:
        print("Test failed: .pop(0) method unavailable? (or __repr__ not working?)")

    try:
        ul = UnorderedList()
        ul.add(2)
        ul.add(1)
        ul.add(0)
        ul.pop(1)
        if str(ul) == "UnorderedList[0,2,]":
            tests_passed += 1
            print("Test passed: .pop(1) successfully removed item from middle of list")
        else:
            print("Test failed: .pop(1) didn't remove last item from middle of list correctly")
    except:
        print("Test failed: .pop(1) method unavailable? (or __repr__ not working?)")


        
    print(str(tests_passed) + "/21 tests passed on the UnorderedList class")

if __name__ == "__main__":
    main()


    
