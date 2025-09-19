"""
A bot starts at the origin (0, 0) and can move in four directions: UP, DOWN, LEFT, and RIGHT, each by 1 unit.
The program accepts a sequence of moves as input, where the first entry is always 'START' and the last entry is always 'STOP'.
For example:
START
UP
RIGHT
LEFT
LEFT
DOWN
UP
STOP

The task is to compute and print the Manhattan distance of the bot from the origin after executing all moves.
The Manhattan distance for a position (x, y) is calculated as: D = |x| + |y|
"""
pos_x, pos_y = 0,0
action = str(input())
while action != "STOP" :
    action = str(input())
    if action == "UP" :
        pos_y = pos_y + 1
    if action == "DOWN" :
        pos_y = pos_y - 1
    if action == "LEFT" :
        pos_x = pos_x - 1
    if action == "RIGHT" :
        pos_x = pos_x + 1
print(abs(pos_x)+abs(pos_y))