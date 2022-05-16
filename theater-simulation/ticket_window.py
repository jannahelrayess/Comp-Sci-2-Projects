'''
ticket_window.py
Jannah El-Rayess & Samara Baksh
2021-05-05

A simple ticket window class that keeps track of the total idle time at a window and the total tickets sold.
'''

from customer import Customer

class Ticket_window:
    def __init__(self, processing_time):
        self.__time_idle = 0
        self.__idle = True
        self.__tickets_sold = 0
        self.__time_elapsed = 0
        self.__processing_time = processing_time

    def get_tickets_sold(self):
        return self.__tickets_sold
    
    def set_tickets_sold(self, tickets_sold):
        self.__tickets_sold = tickets_sold
    
    def get_time_idle(self):
        return self.__time_idle
    
    def set_time_idle(self, time_idle):
        self.__time_idle = time_idle
    
    def get_processing_time(self):
        return self.__processing_time
    
    def set_processing_time(self, processing_time):
        self.__processing_time = processing_time
    
    def get_time_elapsed(self):
        return self.__time_elapsed
    
    def set_time_elapsed(self, time_elapsed):
        self.__time_elapsed = time_elapsed
    
    def get_idle(self):
        return self.__idle

    # enter_window: ->
    # Sets if the window is empty to false as a customer entered the window
    def enter_window(self):
        self.__idle = False
    
    # update_time: ->
    # Updates the time that a window is empty by 1 second 
    def update_time(self):
        if self.__idle == True:
            self.__time_idle += 1
        else:
            self.__time_elapsed += 1
    
    # exit_window: ->
    # Registers that a customer left the window by resetting the elapsed time to 0, making note that the 
    # window is empty, and increasing the amount of total tickets sold by 1 ticket
    def exit_window(self):
        self.__time_elapsed = 0
        self.__idle = True
        self.__tickets_sold += 1
    
    def __str__(self):
        return "Total idle time: " + str(self.__time_idle) + "\nTotal tickets sold: " + str(self.__tickets_sold)