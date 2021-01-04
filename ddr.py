#!/usr/bin/env python3

from sense_hat import SenseHat
from random import choice
import time
import argparse

# Error checking for argument parsing
def arg_checker(arg):
    if str(arg) not in ['easy', 'medium', 'hard']:
        raise argparse.ArgumentTypeError('Invalid argument.')
    return str(arg)

# Setup argument parser and arguments
parser = argparse.ArgumentParser(description = 'Game settings')
parser.add_argument('-d', '--difficulty', dest = 'difficulty', type = arg_checker, default = 'easy', help = 'Game difficulty - options are "easy", "medium", and "hard" (Default = "easy")')
args = parser.parse_args()

# Initialize sense hat and clear LED array
sense = SenseHat()
sense.clear()

# Create color tuples
a = (0, 255, 255)
b = (0, 0, 0)
pink = (255, 153, 255)

# Create arrow lists for LED array
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

# Create a list of possible directions
directions = ['left', 'right', 'up', 'down']

# Create leaderboard list to hold scores
leaderboard = []

# While loop to run game in
while True:
    # Reset end_game flag
    end_game = False
    
    # Print chosen difficulty
    print("Difficulty: " + args.difficulty)
    
    # Set game delay based on selected difficulty
    if args.difficulty == "easy":
        delay = 3
    elif args.difficulty == "medium":
        delay = 2
    else:
        delay = 1

    # Set score to 0
    score = 0
    
    # Countdown timer for start of game
    sense.show_letter('3', pink)
    time.sleep(1)
    sense.show_letter('2', pink)
    time.sleep(1)
    sense.show_letter('1', pink)
    time.sleep(1)

    # Each game round runs inside of this loop
    for i in range(20):
        # Clear the LED array
        sense.clear()
        
        # Randomly choose arrow direction
        arrow = choice(directions)
        
        # Set LED array to display chosen arrow
        if arrow == 'left':
            sense.set_pixels(left_arrow)
        elif arrow == 'right':
            sense.set_pixels(right_arrow)
        elif arrow == 'up':
            sense.set_pixels(up_arrow)
        elif arrow == 'down':
            sense.set_pixels(down_arrow)
            
        # Delay for amount of time determined by difficulty
        time.sleep(delay)
        
        # Reset user_event storage
        user_event = 'none'
        
        # Get joystick events
        for event in sense.stick.get_events():
            # Break out of loop if an event has been stored
            if user_event != 'none':
                break
            # Check if event is pressed and not middle direction, then save it
            if event.action == 'pressed':
                if event.direction in ['left', 'right', 'down', 'up']:
                    user_event = event.direction
            
        # If user joystick direction matches chosen arrow, give a point
        if arrow == user_event:
            score = score + 1
        
        # Print score
        print(score)
        
    # Print final score in terminal and on LED array
    print("Final Score: " + str(score))
    sense.show_message("Final Score: ", scroll_speed = 0.05)
    sense.show_message(str(score), scroll_speed = 0.2)
    
    # Add score to leaderboard
    leaderboard.append(score)
    
    # Clear diff_menu and restart flags
    diff_menu = False
    restart = False
    
    # While loop to contain end of game menu
    while True:
        # Break out of loop if restart or end_game flags are true
        if restart == True or end_game == True:
            break
        # Allow user to select end of game options based on menu in README file
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction in ['left', 'right', 'down', 'up']:
                    if diff_menu == False:
                        if event.direction == 'up':
                            restart = True
                        if event.direction == 'left':
                            end_game = True
                        if event.direction == 'down':
                            diff_menu = True
                    else:
                        if event.direction == 'up':
                            args.difficulty = 'easy'
                        elif event.direction == 'right':
                            args.difficulty = 'medium'
                        elif event.direction == 'left':
                            args.difficulty = 'hard'
                        restart = True
                
    # Break out of full game while loop if end_game flag is true
    if end_game == True:
        break

# Print highest score from game on LED array
sense.show_message("High Score: ", scroll_speed = 0.05)
sense.show_message(str(max(leaderboard)), scroll_speed = 0.2)