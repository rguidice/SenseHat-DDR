# DDR-Style Game on Raspberry Pi Sense Hat

This game is a Dance Dance Revolution-style game that uses the input and output capabilities of the Raspberry Pi Sense Hat.

usage: `ddr.py [-h] [-d DIFFICULTY]`  
Optional Arguments:  
  `-h, --help` Show this help message and exit  
  `-d DIFFICULTY, --difficulty DIFFICULTY` Game difficulty - options are "easy", "medium", and "hard" (Default = "easy")  

End of game menu:
- Up - Restart game
- Left - End game
- Down - Go into difficulty menu (game will restart after selection):
    - Up - Change to easy
    - Right - Change to medium
    - Left - Change to hard