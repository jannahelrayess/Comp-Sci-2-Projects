'''
simulation.py
Jannah El-Rayess & Samara Baksh
2021-05-05

A simulation class that runs the entire program by setting up the simulation and loops every second. It also 
prints out all the final statistics once the simulation is over. 
'''

from theater import Theater
from ticket_window import Ticket_window
from ticket_line import Ticket_line
from customer import Customer

class Simulation:
    def __init__(self, input_file):
        self.__input_file = input_file
        self.__input = []
        self.__time = 0
        self.__simlength = 0
        self.__theater = None
        self.__line_type = 'S'
    
    # read_file: ->
    # Reads and takes in the info from the input file
    def read_file(self):
        file_obj = open(self.__input_file, 'r')
        file_lst = []
        for line in file_obj:
            file_lst.append(line.strip())
        file_obj.close()
        self.__input = file_lst
    
    # setup: ->
    # Sets up all the info from the input file so it corresponds with the right attributes 
    def setup(self):
        self.read_file()
        self.__simlength = (int(self.__input[1]) * 60)
        num_windows = int(self.__input[2])
        processing_times = self.__input[4:4+num_windows]
        self.__line_type = self.__input[3]
        if self.__line_type == 'S':
            num_lines = 1
        else:
            num_lines = num_windows
        self.__theater = Theater(self.__simlength, num_lines, num_windows, processing_times)

    # loop: ->
    # Loops everything that needs to be checked every second of the simulation
    def loop(self):
        customer_arrivals = self.__input[4+int(self.__input[2]):-1]
        customer_num = 0

        for j in range(len(customer_arrivals)):
            customer_arrivals[j] = customer_arrivals[j].split()

        for i in range(self.__simlength):
            if customer_num < len(customer_arrivals):
                if self.__time == int(customer_arrivals[customer_num][1]):
                    for k in range(int(customer_arrivals[customer_num][0])):
                        self.__theater.arrivals()
                    customer_num += 1
            self.__theater.update()
            self.__time += 1
    
    # window_statistics: ->
    # Prints out the window statistics from the simulation
    def window_statistics(self):
        num = 0
        
        for window in self.__theater.get_windows():
            num += 1
            total_tickets_sold = window.get_tickets_sold()
            total_time_idle = window.get_time_idle()
            percent_time_idle = (total_time_idle/self.__simlength) * 100
        
            print("\nWindow #" + str(num) + \
                "\n" +  str(total_tickets_sold) + " tickets sold\n" + \
                str(round(percent_time_idle, 2)) + "%" + " of the time was idle (" + str(total_time_idle) + " seconds out of " + str(self.__simlength) + ")\n")

    # line_statistics: ->
    # Prints out the line statistics from the simulation
    def line_statistics(self):
        num = 0
        total_customer_wait_time = 0
        
        for line in self.__theater.get_lines():
            num += 1
            customers_waiting = len(line)
            max_len = line.get_max_length()
            max_wait = line.get_max_customer_wait_time()
            customers_served = line.get_total_customers_served()
            if customers_served == 0:
                avg_wait_served = 0
            else:
                avg_wait_served = line.get_total_wait_time() / customers_served

            print("Line #" + str(num) + \
                "\n" +  str(customers_waiting) + " customer(s) waiting at the end of the simulation\n" + \
                "Maximum length was " + str(max_len) + " customers\n" + \
                "Average wait time: " + str(round(avg_wait_served, 2)) + " seconds\n" + \
                "Maximum wait time: " + str(max_wait) + " seconds\n")

    # overall_statistics: ->
    # Prints out the overall statistics from the simulation
    def overall_statistics(self):
        total_tickets_sold = 0
        total_customer_wait_time = 0
        total_processing_time = 0
        total_customers_served = 0

        for window in self.__theater.get_windows():
            tickets_sold = window.get_tickets_sold()
            total_tickets_sold += tickets_sold
            processing_time = window.get_processing_time()

            total_window_processing_time = tickets_sold * processing_time
            total_processing_time += total_window_processing_time
        
        if total_tickets_sold == 0:
                average_time_at_window = 0
        else:
            average_time_at_window = total_processing_time / total_tickets_sold
        
        for line in self.__theater.get_lines():
            total_customer_wait_time += line.get_total_wait_time()
            total_customers_served += line.get_total_customers_served()
        
        if total_customers_served == 0:
                average_wait_time = 0
        else:
            average_wait_time = total_customer_wait_time / total_customers_served

        print("Overall" + \
            "\n" +  str(total_tickets_sold) + " tickets sold\n" + \
            "Average wait time: " + str(round(average_wait_time, 2)) + " seconds\n" + \
            "Average time spent at a window: " + str(round(average_time_at_window, 2)) + " seconds\n")

# main: ->
# Calls for the simulation to run and print out the resulting statistics
def main():
    s = Simulation('notes.txt')
    s.setup()
    s.loop()
    s.window_statistics()
    s.line_statistics()
    s.overall_statistics()

main()