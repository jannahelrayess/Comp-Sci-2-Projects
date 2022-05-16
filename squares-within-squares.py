'''
squares-within-squares.py
Jannah El-Rayess
2020-10-2

A program that uses recursion to draw multiple shapes such as squares and polygons.
It uses specific math functions such as sin, cos, and radians in order to perfectly
calculate the ratios for the sizing of the shapes when recursivly shrinking them.
'''

import turtle
import math

#1
#recursive_square: int turtle -> 
#takes the side length for the square that will be drawn recursively
def recursive_square_helper(side_length, sides, t):
    if sides >= 1:
        t.forward(side_length)
        t.left(90)
        recursive_square_helper(side_length, sides - 1, t)

def recursive_square(side_length, t):
    recursive_square_helper(side_length, 4, t)

#2
#recursive_polygon: int int turtle -> 
#takes the side length and number of sides for a polygon that
#will be drawn recursively
def recursive_polygon_helper(side_length, sides, x, t):
    if sides >= 1:
        t.forward(side_length)
        t.left(360/x)
        recursive_polygon_helper(side_length, sides - 1, x, t)

def recursive_polygon(side_length, sides, t):
    recursive_polygon_helper(side_length, sides, sides, t)
    
#3
#concentric_squares: int int turtle -> 
#recursively draws a set of n concentric squares centered about the origin
def loop_draw(side_length, sides, t):
    if sides >= 1:
        t.forward(side_length)
        t.right(90)
        loop_draw(side_length, sides - 1, t)
        
def concentric_squares(side_length, n, t):
    if n >= 1:
        t.penup()
        t.left(90)
        t.forward(side_length/2)
        t.right(90)
        t.pendown()
        t.forward(side_length/2)
        t.right(90)
        loop_draw(side_length, 3, t)
        t.forward(side_length/2)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        concentric_squares(side_length * 0.75, n - 1, t)

#4
#rotating_squares: int int int turtle -> 
#recursively draws a set of n concentric squares rotating
#about the origin by "angles" degrees
def rotating_squares(side_length, n, angle, t):
    if n >= 1:
        t.penup()
        t.left(90)
        t.forward(side_length/2)
        t.right(90)
        t.pendown()
        t.forward(side_length/2)
        t.right(90)
        loop_draw(side_length, 3, t)
        t.forward(side_length/2)
        t.penup()
        t.goto(0, 0)
        t.left(angle)
        t.pendown()
        rotating_squares(side_length * 0.75, n - 1, angle, t)

#5
'''
In order to find the ratios between the original side length, the new one,
and the angle of rotation, trig is needed. If the angle of roation is x
and the new side length is S, the 2 parts of the original side length
are S*sin(x) and S*cos(x). Depending on the size of x will affect which
part is smaller or larger. The sin part is alaways apposite the angle of
rotation, and the cos part is always adjacent. 
side_length = (S * sin(angle) + S * cos(angle))
side_length = S(sin(angle) + cos(angle))
side_length/(sin(angle) + cos(angle)) = S
'''

#6
#rotating_squares_modified: int int int turtle -> 
#recursively draws a set of n concentric squares rotating
#about the origin by "angles" degrees
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def rotating_squares_modified(side_length, n, angle, t):
    if n >= 1:
        t.penup()
        t.left(90)
        t.forward(side_length/2)
        t.right(90)
        t.pendown()
        t.forward(side_length/2)
        t.right(90)
        loop_draw(side_length, 3, t)
        t.forward(side_length/2)
        t.penup()
        t.goto(0, 0)
        t.left(angle)
        t.pendown()
        rotating_squares_modified((side_length/(sin(angle) + cos(angle))), n - 1, angle, t)

#7
#inscribed_polygons: int int int int turtle ->
#recursively draws a set of n polygons with a number of sides "sides"
#rotating about the origin by "angles" degrees
def loop_draw_poly_help(side_length, sides, x, t):
    if sides >= 1:
        t.forward(side_length)
        t.right(360/x)
        loop_draw_poly_help(side_length, sides - 1, x, t)

def loop_draw_poly(side_length, sides, t):
    loop_draw_poly_help(side_length, sides - 1, sides, t)

def tan(x):
    return math.tan(math.radians(x))
        
def inscribed_polygons(side_length, sides, n, angle, t):
    C = ((180 * (sides - 2)) / sides)
    B = 180 - C - angle
    x = (side_length * sin(B)) / (sin(angle) + sin(B))
    z = (x * sin(C)) / sin(B)
    if n >= 1:
        t.penup()
        t.left(90)
        t.forward((side_length/2) / tan(360/(2*sides)))
        t.right(90)
        t.pendown()
        t.forward(side_length/2)
        t.right(360/sides)
        loop_draw_poly(side_length, sides, t)
        t.forward(x)
        t.penup()
        t.goto(0, 0)
        t.left(angle)
        t.pendown()
        inscribed_polygons(z, sides, n - 1, angle, t)

def main():
    side_length = 200
    angle = 10
    n = 10
    sides = 6
    t = turtle.Pen()
    '''
    recursive_square(side_length, t)
    recursive_polygon(side_length, sides, t)
    concentric_squares(side_length, n, t)
    rotating_squares(side_length, n, angle, t)
    rotating_squares_modified(side_length, n, angle, t)
    inscribed_polygons(side_length, sides, n, angle, t)
    '''
    turtle.mainloop()

main()







