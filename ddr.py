from sense_hat import SenseHat
from random import choice
import time
import argparse

def arg_checker(arg):
    if str(arg) not in ['easy', 'medium', 'hard']:
        raise argparse.ArgumentTypeError('Invalid argument.')
    return str(arg)

parser = argparse.ArgumentParser(description = 'Game settings')
parser.add_argument('-d', '--difficulty', dest = 'difficulty', type = arg_checker, default = 'easy', help = 'Game difficulty - options are "easy", "medium", and "hard" (Default = "easy")')
args = parser.parse_args()

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

if args.difficulty == "easy":
    delay = 3
elif args.difficulty == "medium":
    delay = 2
else:
    delay = 1

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
        
    time.sleep(delay)
    
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
sense.show_message("Final Score: ", scroll_speed = 0.05)
sense.show_message(str(score), scroll_speed = 0.2)
            
