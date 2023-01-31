'''
We are interested in integers without the digit 7 in both decimal and octal. 
How many such integers are there between 1 and N (inclusive)?

Sample Input 1
20
Sample Output 1
17
Sample Input 2
100000
Sample Output 2
30555
'''

a=[0,1,2,3,4,5,6,7]
n=int(input())
c=0

for i in range(1,n+1):
    octal_num=''
    oi=i
    k=''
    while(i//8 not in a):
        k=k+str(i%8)
        i=i//8
        octal_num=octal_num+str(k)
    if(i//8 in a):
        k=i%8
        i=i//8
        octal_num=str(i)+str(k)+octal_num
    if ('7' not in str(oi)):
        if ('7' not in octal_num):
            c=c+1
print(c)
