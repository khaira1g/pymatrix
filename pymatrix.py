import os
import random
import time
import sys

# Configs
rows, cols = 30, 50  # Number of rows and columns in the matrix
delay = 0.05  
symbols = ["た", "て", "い", "す", "か", "ん", "な", "に", "ら", "せ", "ち", "と", "し", "は", "き", "く", "ま", "の", "り", "つ", "さ", "そ", "ひ", "こ", "み", "も", "よ", "ろ", "わ", "え", "お", "あ", "う", "い", "え", "お", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def sleep(secs):
    time.sleep(secs)

columns = [
    {
        "position": random.randint(0, rows - 1),
        "length": random.randint(5, 15),
        "speed": random.randint(1, 3),
    }
    for _ in range(cols)
]

def clear_screen():
    # clear the prompt screen
    os.system("cls" if os.name == "nt" else "clear")

def hide_cursor():
    # hide the terminal cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    # show the terminal cursor
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def move_cursor_to_top():
    # move cursor to the top left corner
    sys.stdout.write("\033[H")
    sys.stdout.flush()

# hide the cursor at start
hide_cursor()

try:
    while True:
        # move the cursor
        move_cursor_to_top()

        # update and print the screen
        for row in range(rows):
            for col in range(cols):
                column = columns[col]
                if row == column["position"]:
                    # p[rint the head of the stream in bright white
                    sys.stdout.write(f"\033[97m{random.choice(symbols)} ")
                elif column["position"] - column["length"] < row < column["position"]:
                    # print the body of the stream in green
                    sys.stdout.write(f"\033[32m{random.choice(symbols)} ")
                else:
                    # make a blank
                    sys.stdout.write("  ")
            sys.stdout.write("\n")

        # Update cols positions
        for column in columns:
            column["position"] += column["speed"]
            if column["position"] - column["length"] > rows:
                # reset when the column goes out off screen
                column["position"] = 0
                column["length"] = random.randint(5, 15)
                column["speed"] = random.randint(1, 3)

        # delays the strean
        sleep(delay)

except KeyboardInterrupt:
    show_cursor() # the cursor shows when interrupted and script ends exec