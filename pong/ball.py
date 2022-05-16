'''
ball.py
Jannah El-Rayess
2021-01-25

A simple ball class.
'''

import pyglet
import random

class Ball:
    def __init__(self, x, y, r, x_vel, y_vel):
        self.__x = x
        self.__y = y
        self.__x_vel = x_vel
        self.__y_vel = y_vel
        self.__r = r

    # get_x: -> int
    def get_x(self):
        return self.__x
    
    # set_x: int -> 
    def set_x(self, x):
        self.__x = x
    
    # get_y: -> int
    def get_y(self):
        return self.__y
    
    # set_y: int -> 
    def set_y(self, y):
        self.__y = y
    
    # get_x_vel: -> int
    def get_x_vel(self):
        return self.__x_vel
    
    # set_x_vel: int -> 
    def set_x_vel(self, x_vel):
        self.__x_vel = x_vel
    
    # get_y_vel: -> int
    def get_y_vel(self):
        return self.__y_vel
    
    # set_y_vel: int -> 
    def set_y_vel(self, y_vel):
        self.__y_vel = y_vel
    
    # get_r: -> int
    def get_r(self):
        return self.__r
    
    # set_r: int -> 
    def set_r(self, r):
        self.__r = r

    # update: ->
    # Updates the position of the ball based on its velocity
    def update(self):
        self.__x += self.__x_vel
        self.__y += self.__y_vel
    '''
        if self.__x < self.__r or self.__x > 800 - self.__r:
            self.__x_vel *= -1

        if self.__y < self.__r or self.__y > 600 - self.__r:
            self.__y_vel *= -1
    '''

    # collide: obj ->
    # Takes another ball object and changes the velocities of the two
    # Balls so that way they react to colliding with each other
    def collide(self, other):
        x_dist = abs(self.__x - other.__x)
        y_dist = abs(self.__y - other.__y)
        r_sum = self.__r + other.__r

        if x_dist <= r_sum and y_dist <= r_sum:
            # Vertical
            if x_dist < y_dist: 
               temp_y_vel = self.__y_vel
               self.__y_vel = other.__y_vel 
               other.__y_vel = temp_y_vel

            # Horizontal
            elif y_dist <= x_dist:
                temp_x_vel = self.__x_vel
                self.__x_vel = other.__x_vel 
                other.__x_vel = temp_x_vel