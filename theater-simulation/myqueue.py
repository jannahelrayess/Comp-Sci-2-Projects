'''
myqueue.py
Jannah El-Rayess
2021-05-05

A simple queue class.
'''

from linked_list import Linked_list

class myQueue:
    def __init__(self):
        self.__items = Linked_list()
    
    # enqueue: object ->
    # Appends the given object to the queue  
    def enqueue(self, item):
        self.__items.append(item)

    # dequeue: ->
    # Pops first item in the queue  
    def dequeue(self):
        return self.__items.pop(0)
    
    # front: ->
    # Returns the first item in the queue 
    def front(self):
        return self.__items[0]
    
    # is_empty: ->
    # Returns a boolean based off of if the queue is empty or not
    def is_empty(self):
        return len(self.__items) == 0
    
    # queue_in_order: ->
    # Returns a boolean based off of if the queue is in order or not
    def queue_in_order(self):
        for i in range(len(self.__items) - 1):
            if self.__items[i] < self.__items[i + 1]:
                pass

            else:
                return False
        
        return True 
    
    def __len__(self):
        return len(self.__items)
    
    def __str__(self):
        return str(self.__items)