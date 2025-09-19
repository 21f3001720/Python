'''
Consider the following image of a chess-board: 
    A   B   C   D   E   F   G   H
8   ♜  ♞  ♝  ♛  ♚  ♝  ♞  ♜
7   ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟
6   .   .   .   .   .   .   .   .
5   .   .   .   .   .   .   .   .
4   .   .   .   .   .   .   .   .
3   .   .   .   .   .   .   .   .
2   ♙  ♙  ♙  ♙  ♙  ♙  ♙  ♙
1   ♖  ♘  ♗  ♕  ♔  ♗  ♘  ♖

Accept two positions as input: start and end. Print YES if a bishop at start can move to end in exactly one move. Print NO otherwise. Note that a bishop can only move along diagonals.
'''
start = str(input("Enter start position for bishop : "))
end = str(input("Enter end position for bishop : "))
posAH = "ABCDEFGH"
pos18 = "1234567"
x1 = posAH.find(start[0])
y1 = pos18.find(start[-1])
x2 = posAH.find(end[0])
y2 = pos18.find(end[-1])
if x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2 :
    print("YES")
else :
    print("NO")
