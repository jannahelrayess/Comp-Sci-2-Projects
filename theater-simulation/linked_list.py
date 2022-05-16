'''
linked_list.py
Jannah El-Rayess
2021-05-05

A linked list class that includes a head and tail pointer.
'''

from node import Node

class Linked_list:
    def __init__(self):
        self.__head = None # Initially, there is no head node.
        self.__tail = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def __str__(self):
        lst = '['
        node = self.__head

        if self.__head == None:
            return '[]'
        else:
            for i in range(self.__length - 1):
                lst += str(node.item)
                node = node.link
                lst += ', '
            
            lst += str(node.item)
            lst += ']'
        
            return lst
    
   # __getitem__: int -> item
    # Returns the node item located at the given index in the linked list
    def __getitem__(self, index):
        return self.__find(index).item
    
    # __setitem__: int item ->
    # Sets the given index with the given item
    def __setitem__(self, index, item):
        edited_node = self.__find(index)
        edited_node.item = item

    # __find: int -> Node
    # Consumes a non-negative integer index (0 <= index < self.__length)
    # and produces the Node located at this position in the list.
    def __find(self, index):
        if index == 0:
            return self.__head
        elif (index == self.__length - 1) or (index == -1):
            return self.__tail
        else: # index > 0
            node = self.__head
            for i in range(index):
                node = node.link
            return node

    # append: object ->
    # Consumes an object and adds it to the end of the list.
    def append(self, item):
        old_tail = self.__tail
        self.__tail = Node(item) # The new last node in the list
        
        # If the the list is empty, make new_last_node the head.
        # Else, find the last node in the list and make it point
        # to new_last_node.
        if self.__length == 0:
            self.__head = self.__tail
        else:
            old_tail.link = self.__tail
        
        self.__length += 1 # Increase the length of the list by 1
    
    # insert: int object -> 
    # Consumes an object and index value to insert the object into said index value
    def insert(self, index, item):
        new_node = Node(item)

        if index == 0: 
            old_head = self.__head
            self.__head = new_node
            new_node.link = old_head
        elif index >= self.__length:
            return self.append(new_node.item)
        elif (index == -1) or (index == self.__length - 1):
            prev_node = self.__find(self.__length - 2)
            old_node = self.__find(index)
            prev_node.link = new_node
            new_node.link = old_node
        else:
            node = self.__find(index - 1)  
            node_after = self.__find(index)
            node.link = new_node
            new_node.link = node_after
        
        self.__length += 1
    
    # pop: int ->
    # Consumes an index value (but if there is not one given it will assume the index value is -1)
    # And removes as well as prints out the item in the list at that index
    def pop(self, index = -1):
        if index == 0:
            removed = self.__head.item
            node_after_head = self.__head.link
            self.__head = node_after_head
            self.__length -= 1
            if self.__length == 0:
                self.__tail = None
            else:
                pass
            return removed
        elif (index == -1) or (index == self.__length - 1):
            removed = self.__tail.item
            self.__tail = self.__find(self.__length - 2)
            self.__tail.link = None
            self.__length -= 1
            return removed
        else:
            removed = self.__find(index).item
            node = self.__find(index + 1)
            node_before = self.__find(index - 1)
            node_before.link = node
            self.__length -= 1
            return removed