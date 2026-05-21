import sys
sys.path.insert(0, "../src")

import display

def test_game_over() -> bool:

    print("Hello! Since I can't really test whether or not you can see something without user input, I'll be asking you a question directly. Please wait for the screen to open, then exit the program and answer the question.")

    display.GAME_OVER()

    game_over_works = input("Did you see a red screen displaying the words \"GAME OVER\" on your screen? (y/n) ") == "y"

    return game_over_works

if test_game_over():
    print("Test passed! display.py works!")
else:
    print("h o w . (You might want to try reinstalling pygame, or using Python 3.14.5)")