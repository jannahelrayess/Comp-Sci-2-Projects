'''
paddle.py
Jannah El-Rayess
2021-02-15

A simple paddle class.
'''

class Paddle:
    def __init__(self, x, y, speed, l, w, player):
        self.__x = x
        self.__y = y
        self.__speed = speed
        self.__l = l
        self.__w = w
        self.__player = player

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
    
    # get_speed: -> int
    def get_speed(self):
        return self.__speed
    
    # get_l: -> int
    def get_l(self):
        return self.__l
    
    # get_w: -> int
    def get_w(self):
        return self.__w
    
    # ball_hit: obj ->
    # Respectively changes the balls velocity after collding with either paddle
    def ball_hit(self, ball_obj):
        # Obtain the ball object's attribute values
        ball_y = ball_obj.get_y()
        ball_x = ball_obj.get_x()
        ball_r = ball_obj.get_r()
        ball_x_vel = ball_obj.get_x_vel()

        if (ball_y + ball_r < (self.__y + 2 * ball_r)) and (ball_y - ball_r > (self.__y - self.__l) - 2 * ball_r):
            # Left paddle
            if (self.__player == 1) and (self.__x + self.__w > ball_x - ball_r) and (ball_x_vel < 0): 
                ball_x_vel *= -1
                ball_obj.set_x_vel(ball_x_vel)
            
            # Right paddle
            if (self.__player == 2) and (self.__x < ball_x + ball_r) and (ball_x_vel > 0): 
                ball_x_vel *= -1
                ball_obj.set_x_vel(ball_x_vel)