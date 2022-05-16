'''
pong.py
Jannah El-Rayess
2021-02-15

This program uses pyglet to run a game of ping pong where the first to get to 15
or have a lead of 2 beyond 15 wins. The game keeps track of the scores and rounds.
'''

import pyglet
import math
import random
import ball
import paddle
from pyglet.gl.gl import glColor3f

# Set an 800 x 600 window size
window = pyglet.window.Window(800, 600)

# Set scores to 0
p1_score = 0 
p2_score = 0

# Set rounds to 0
game_rounds = 0

# Initialize the ball and paddle objects
random_val = random.random()
theta = math.pi * random_val / 8.0 + math.pi / 16
ball_obj = ball.Ball(400, 300, 10, 8 * math.cos(theta), 8 * math.sin(theta))
p1_paddle = paddle.Paddle(20, 340, 5, 80, 20, 1)
p2_paddle = paddle.Paddle(760, 340, 5, 80, 20, 2)

# A list for storing the states of the four buttons
keys_pressed = [False, False, False, False] 

def update(dt):
	global p1_score, p2_score, game_rounds
	ball_obj.update()

	# Obtain paddle object attribute values
	p1_paddle_y = p1_paddle.get_y()
	p2_paddle_y = p2_paddle.get_y()
	p1_paddle_l = p1_paddle.get_l()
	p2_paddle_l = p2_paddle.get_l()
	p1_paddle_speed = p1_paddle.get_speed()
	p2_paddle_speed = p2_paddle.get_speed()

	# Obtain ball object attribute values
	ball_y = ball_obj.get_y()
	ball_x = ball_obj.get_x()
	ball_r = ball_obj.get_r()
	ball_x_vel = ball_obj.get_x_vel()
	ball_y_vel = ball_obj.get_y_vel()
	
	# Move left paddle 
	if keys_pressed[0] and p1_paddle_y < 600:
		p1_paddle_y += p1_paddle_speed
		p1_paddle.set_y(p1_paddle_y)
	
	if keys_pressed[1] and p1_paddle_y > p1_paddle_l:
		p1_paddle_y -= p1_paddle_speed
		p1_paddle.set_y(p1_paddle_y)
	
	# Move right paddle
	if keys_pressed[2] and p2_paddle_y < 600:
		p2_paddle_y += p2_paddle_speed
		p2_paddle.set_y(p2_paddle_y)
	
	if keys_pressed[3] and p2_paddle_y > p2_paddle_l:
		p2_paddle_y -= p2_paddle_speed
		p2_paddle.set_y(p2_paddle_y)
	
	# Collisions
	p1_paddle.ball_hit(ball_obj)
	p2_paddle.ball_hit(ball_obj)

	if ball_y < ball_r or ball_y > 600 - ball_r:
		ball_y_vel *= -1
		ball_obj.set_y_vel(ball_y_vel)

	# Update left side scores
	if ball_x < 400:
		if ball_x - ball_r < 0:
			ball_obj.set_x(400)
			ball_obj.set_y(300)
			ball_obj.set_x_vel(-8 * (math.cos(math.pi * random.random() / 8.0 + math.pi / 16)))
			ball_obj.set_y_vel(-8 * (math.sin(math.pi * random.random() / 8.0 + math.pi / 16)))
			p2_score += 1
	
	# Update right side scores
	if ball_x > 400:
		if ball_x + ball_r > 800:
			ball_obj.set_x(400)
			ball_obj.set_y(300)
			ball_obj.set_x_vel(8 * (math.cos(math.pi * random.random() / 8.0 + math.pi / 16)))
			ball_obj.set_y_vel(8 * (math.sin(math.pi * random.random() / 8.0 + math.pi / 16)))
			p1_score += 1
	
	# Player 1 winning requirement and update rounds
	if p1_score >= 15 and p1_score - p2_score >= 2:
		p1_score = 0
		p2_score = 0
		game_rounds += 1
	
	# Player 2 winning requirement and update rounds
	if p2_score >= 15 and p2_score - p1_score >= 2:
		p1_score = 0
		p2_score = 0
		game_rounds += 1

# Detection of a keyboard button press
@window.event
def on_key_press(symbol, modifiers):
	if symbol == ord('a'):
		keys_pressed[0] = True
			
	if symbol == ord('z'):
		keys_pressed[1] = True
	
	if symbol == ord('k'):
		keys_pressed[2] = True
			
	if symbol == ord('m'):
		keys_pressed[3] = True
	
# Detection of a keybaord button release	
@window.event
def on_key_release(symbol, modifiers):
	if symbol == ord('a'):
		keys_pressed[0] = False
    
	if symbol == ord('z'):
		keys_pressed[1] = False
    
	if symbol == ord('k'):
		keys_pressed[2] = False
    
	if symbol == ord('m'):
		keys_pressed[3] = False

# Draw to the window
@window.event
def on_draw():
	# Clear the screen	
	window.clear()
	
    # Display the score
	score_display = pyglet.text.Label(str(p1_score) + "\t\t\t" + str(p2_score),
                            font_name = 'Consolas',
                            font_size = 44,
							color = (215, 179, 228, 255),
                            x = window.width / 2, y = 550, 
                            anchor_x = 'center', anchor_y = 'center')
	score_display.draw()  

	# Display the number of rounds
	rounds_display = pyglet.text.Label("Rounds: " + str(game_rounds),
                            font_name = 'Consolas',
                            font_size = 20,
							color = (215, 179, 228, 255),
                            x = 473, y = 20, 
                            anchor_x = 'center', anchor_y = 'center')
	rounds_display.draw()  

    
    # Draw the net
	glColor3f(0.2, 0.3, 0.6)
	for i in range(20):
		pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                            ('v2f', [395, 30 * i, 405, 30 * i, 405, 30 * i + 20, 395, 30 * i + 20])) 
    
    # Draw the paddles
	glColor3f(0.9, 0.3, 0.5)
	pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, 
                        ('v2f', [p1_paddle.get_x(), p1_paddle.get_y(), p1_paddle.get_x() + p1_paddle.get_w(), p1_paddle.get_y(),
						p1_paddle.get_x() + p1_paddle.get_w(), p1_paddle.get_y() - p1_paddle.get_l(), p1_paddle.get_x(), p1_paddle.get_y() - p1_paddle.get_l()])) 
	pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, 
                        ('v2f', [p2_paddle.get_x(), p2_paddle.get_y(), p2_paddle.get_x() + p2_paddle.get_w(), p2_paddle.get_y(),
						p2_paddle.get_x() + p2_paddle.get_w(), p2_paddle.get_y() - p2_paddle.get_l(), p2_paddle.get_x(), p2_paddle.get_y() - p2_paddle.get_l()])) 
 
    
	# Draw the ball
	x = ball_obj.get_x()
	y = ball_obj.get_y()
	r = ball_obj.get_r()

	glColor3f(1.0, 0.9, 0.4)
	pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', [x - r, y + r, x + r, y + r, x + r, y - r, x - r, y - r]))

pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
