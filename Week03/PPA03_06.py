"""
Accept a sequence of words as input and print the shortest word in the sequence.

Input:
- The input consists of n+1 lines, where n is the number of words in the sequence.
- Each of the first n lines contains a word in the sequence (1 ≤ i ≤ n).
- The last line is always the string 'abcdefghijklmnopqrstuvwxyz', which is not part of the sequence and serves as a sentinel to end input.

Output:
- Print the shortest word from the sequence.
- If multiple words have the same minimum length, print the first such occurrence.

Assumption:
- Each test case corresponds to a non-empty sequence of words.
"""
word = ''
shortest = 'abcdefghijklmnopqrstuvwxyz'
while word != 'abcdefghijklmnopqrstuvwxyz' :
    word = str(input())
    if len(word)<len(shortest):
        shortest = word
print(shortest)