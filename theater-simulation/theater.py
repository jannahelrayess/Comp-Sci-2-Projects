'''
theater.py
Jannah El-Rayess & Samara Baksh
2021-05-05

A theater class that updates the lines and windows by placing customers in the appropriate lines and windows. 
'''

from customer import Customer
from ticket_line import Ticket_line
from ticket_window import Ticket_window

class Theater:
    def __init__(self, sim_time, num_lines, num_windows, processing_times):
        self.__lines = []
        self.__windows = []
        self.__num_lines = num_lines
        self.__num_windows = num_windows
        self.__processing_times = processing_times
        self.__sim_time = sim_time
        self.make_lines()
        self.make_windows()
    
    # make_lines: ->
    # Creates a number of empty Ticket lines based on the number of lines inputted to the Theater class
    def make_lines(self):
        for i in range(self.__num_lines):
            self.__lines.append(Ticket_line())
            
    # make_windows: ->
    # Creates a number of Ticket windows with specific processing times from Theater class input
    def make_windows(self):
        for i in range(self.__num_windows):
            self.__windows.append(Ticket_window(int(self.__processing_times[i])))
        
    def get_lines(self):
        return self.__lines
    
    def set_lines(self, lines):
        self.__lines = lines
    
    def get_windows(self):
        return self.__windows
    
    def set_windows(self, windows):
        self.__windows = windows
    
    # arrivals: ->
    # Places a customer into the right line based on the lines' lengths
    def arrivals(self):
        length_of_lines = []
        all_same = True

        for line in self.__lines:
            length_of_lines.append(len(line))

        record_min = length_of_lines[0]

        for length in length_of_lines:
            if length_of_lines[0] != length:
                all_same = False
        
        line_num = 0
        if not all_same:
            for i in range(len(length_of_lines)):
                if length_of_lines[i] < record_min:
                    record_min = length_of_lines[i]
                    line_num = i
        self.__lines[line_num].enter_line()
        
        if self.__windows[line_num].get_idle() and len(self.__lines[line_num]) > 0:
            self.__lines[line_num].exit_line()
            self.__windows[line_num].enter_window()
        
    
    # update: ->
    # Updates the position of a customer by checking the windows and if said customer
    # Can be at a window or not
    def update(self):
        for w in range(len(self.__windows)):
            window = self.__windows[w]
            if window.get_time_elapsed() == window.get_processing_time():
                window.exit_window()
            if window.get_idle():
                if self.__num_lines == 1:
                    if len(self.__lines[0]) > 0:
                        self.__lines[0].exit_line()
                        window.enter_window()
                else:
                    if len(self.__lines[w]) > 0:
                        self.__lines[w].exit_line()
                        window.enter_window()
            window.update_time()
        for line in self.__lines:
            line.increase_wait_time()