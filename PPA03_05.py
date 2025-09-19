""" Accept a sequence of positive integers as input and print the maximum number in the sequence.

Input:

The input consists of n+1 lines, where n denotes the number of terms in the sequence.
The i-th line (for 1 ≤ i ≤ n) contains the i-th term in the sequence.
The last line of the input will always be the number 0, which serves as a sentinel value and is not part of the sequence.
Each test case will have at least one term in the sequence.
Output:

Print the maximum number among the input sequence (excluding the terminating 0). """
num = int(input())
max_num = -1
while num != 0:
    if max_num <= num:
        max_num = num
    num = int(input())
    
print(max_num) 