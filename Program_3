'''
You are given a float array of length L with values in the array and you start at the 0th index and you can jump a max of k indices at once. 
Find the least score possible to reach the end of the array. (First you're given the value of k then size of array and then array elements)

Sample Input 0

3
10
1
2
3
4
5
6
7
8
9
10

Output Format
22

'''
k=int(input())
length=int(input())
lst=[]
j=0
sum=0
for i in range(length):
    lst.append(int(input()))
while(j<length):
    sum=sum+lst[j]
    j=j+3
print(sum)
