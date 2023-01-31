'''
Edward participated in one maths competition. He was asked to find the number of ways to choose a pair of an even number 
and an odd number from the positive integers between 1 and N (inclusive). The order does not matter.

The input line contains only one input N.

Print the number of ways to choose a pair of an even number and an odd number from the positive integers between 1 and N (inclusive).

Sample Input 1
3
Sample Output 1
2

Sample Input 2
6
Sample Output 2
9
'''

n=int(input())
if n%2==0:
    even=odd=int(n/2)
else:
    even=int(n/2)
    odd=even+1
print(odd*even)
