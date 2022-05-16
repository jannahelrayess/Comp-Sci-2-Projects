'''
customer.py
Jannah El-Rayess & Samara Baksh
2021-05-05

A simple customer class that keeps track of the time each customer has spent in a line.
'''

class Customer:
    def __init__(self):
        self.__time = 0
    
    def get_time(self):
        return self.__time
    
    def set_time(self, time):
        self.__time = time
    
    # timer: ->
    # Increases the customer's time by 1 second 
    def timer(self):
        self.__time += 1
    
    def __str__(self):
        return str(self.__time)