from sense_hat import SenseHat
from random import choice
import time

sense = SenseHat()
sense.clear()

a = (0, 255, 255)
b = (0, 0, 0)

up_arrow = [
    b, b, b, a, b, b, b, b,
    b, b, a, a, a, b, b, b,
    b, a, b, a, b, a, b, b,
    a, b, b, a, b, b, a, b,
    b, b, b, a, b, b, b, b,
    b, b, b, a, b, b, b, b,
    b, b, b, a, b, b, b, b,
    b, b, b, a, b, b, b, b
]

down_arrow = [
    b, b, b, a, b, b, b, b,
    b, b, b, a, b, b, b, b,
    b, b, b, a, b, b, b, b,
    b, b, b, a, b, b, b, b,
    a, b, b, a, b, b, a, b,
    b, a, b, a, b, a, b, b,
    b, b, a, a, a, b, b, b,
    b, b, b, a, b, b, b, b
]

left_arrow = [
    b, b, b, b, b, b, b, b,
    b, b, b, a, b, b, b, b,
    b, b, a, b, b, b, b, b,
    b, a, b, b, b, b, b, b,
    a, a, a, a, a, a, a, a,
    b, a, b, b, b, b, b, b,
    b, b, a, b, b, b, b, b,
    b, b, b, a, b, b, b, b
]

right_arrow = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, a, b, b, b,
    b, b, b, b, b, a, b, b,
    b, b, b, b, b, b, a, b,
    a, a, a, a, a, a, a, a,
    b, b, b, b, b, b, a, b,
    b, b, b, b, b, a, b, b,
    b, b, b, b, a, b, b, b
]

directions = ['left', 'right', 'up', 'down']

score = 0

for i in range(20):
    sense.clear()
    arrow = choice(directions)
    
    if arrow == 'left':
        sense.set_pixels(left_arrow)
    elif arrow == 'right':
        sense.set_pixels(right_arrow)
    elif arrow == 'up':
        sense.set_pixels(up_arrow)
    elif arrow == 'down':
        sense.set_pixels(down_arrow)
        
    time.sleep(1)
    
    user_event = 'none'

    
    for event in sense.stick.get_events():
        if user_event != 'none':
            break
        if event.direction == 'left' or 'right' or 'down' or 'up':
            user_event = event.direction
        
    if arrow == user_event:
        score = score + 1
    
    print(score)
    
    
print("Final Score: " + str(score))
            
