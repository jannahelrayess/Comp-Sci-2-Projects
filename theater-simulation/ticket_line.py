'''
ticket_line.py
Jannah El-Rayess & Samara Baksh
2021-05-05

A ticket line class that keeps track of customers withtin the line and if they are exiting or entering it.
'''

from customer import Customer
from myqueue import myQueue

class Ticket_line:
    def __init__(self):
        self.__customers = myQueue()
        self.__total_customers_served = 0
        self.__max_length = 0
        self.__max_customer_wait_time = 0
        self.__total_wait_time = 0
    
    def get_max_length(self):
        return self.__max_length
    
    def set_max_length(self, max_length):
        self.__max_length = max_length
    
    def get_total_customers_served(self):
        return self.__total_customers_served
    
    def set_total_customers_served(self, total_customers_served):
        self.__total_customers_served = total_customers_served

    def get_max_customer_wait_time(self):
        return self.__max_customer_wait_time
    
    def set_max_customer_wait_time(self, max_customer_wait_time):
        self.__max_customer_wait_time = max_customer_wait_time
    
    def get_total_wait_time(self):
        return self.__total_wait_time
    
    def set_total_wait_time(self, total_wait_time):
        self.__total_wait_time = total_wait_time
    
    # enter_line: ->
    # Adds a customer object to the line and resets the max length of the line if the current length is greater
    # Than the record max length 
    def enter_line(self):
        customer = Customer()
        self.__customers.enqueue(customer)

        if len(self.__customers) > self.__max_length:
            self.__max_length += 1
    
    # exit_line: ->
    # Removes a customer from a line and increases the total customers served
    def exit_line(self):
        removed = self.__customers.dequeue()
        self.__total_wait_time += removed.get_time()
        self.__total_customers_served += 1

    
    # increase_wait_time: ->
    # Increases the wait time of each customer in the line and resets the max wait time of a customer if the 
    # Current customer wait time is greater than the record
    def increase_wait_time(self):
        for i in range(len(self.__customers)):
            removed = self.__customers.dequeue()
            removed.timer()
            if removed.get_time() > self.__max_customer_wait_time:
                self.__max_customer_wait_time = removed.get_time()
            self.__customers.enqueue(removed)

    def __str__(self):
        return "Customer line: " + str(self.__customers) + "\nTotal customers served: " + str(self.__total_customers_served) + \
            "\nMax length: " + str(self.__max_length) + "\nMax customer wait time: " + str(self.__max_customer_wait_time)
    
    def __len__(self):
        return len(self.__customers)