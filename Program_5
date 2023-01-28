'''
Alexa Loves to play with 0's and 2's. Among the positive integers that consist of 0's and 2's when written in base 10, he wanted to find the Kth smallest integer. 
Help him find that.

Sample Input 1
3
Sample Output 1
22

Sample Input 2
11
Sample Output 2
2022

Sample Input 3
923423423420220108
Sample Output 3
220022020000202020002022022000002020002222002200002022002200

'''
# code time taken greater than 2sec 

k=int(input())
c=0
m=1
cnt=1
a=[0,2]
while(c!=k):
    value=m=cnt
    m=list(set(list(map(int,list(str(m))))))
    if len(m)==1:
        if m[0]==0 or m[0]==2:
            c=c+1
    elif len(m)==2:
        m.sort()
        if m==a:
            c=c+1
    cnt=cnt+1
    
print(value)

# code time taken less than 2sec 
K = int(input())
print(str(format(K, 'b')).replace('1', '2'))

