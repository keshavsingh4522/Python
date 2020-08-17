'''
Imagine you are a martial arts fighter fighting with fellow martial artists to win prize money. However unlike traditional competitions, here you have the opportunity to pick and choose your opponent to maximize your prize kitty. The rules of maximization of prize kitty are as follows

► You have a superpower bestowed upon you, that you will win against anyone you challenge

► You have to choose the right order because unfortunately the superpower does not ensure that your prize money is always the highest

► Every victory against an opponent that you challenge and win against, will translate into a certain winning sum

► Here begins the technical part that you need to know in order to maximize your winning prize money

o All your opponents are standing inone line next to each other i.e. the order of opponents is fixed

o Your first task is to choose a suitable opponent from this line

o When you choose one opponent from that line, he steps out of the line and fights you.

o After you beat him, you get to decide how your prize money for winning against him will be calculated

o Essentially, if the opponent you have beaten has two neighbours, then you have the option to multiply theopponent numberwith any one of the two neighbours and add the otheropponent number.That value becomes your prize money for that match

o If  your  opponent  has  only  one  neighbor  then  your  prize  money  for  that  match  is  product  of currentopponent numberwith neighbours'opponent number

o When  dealing  with  last  opponent  in  the  tournament,  your  prize  money  is  equal  to  the  value  of  the lastopponent number

o As the tournament proceeds, the opponent that you have beaten has to leave the tournament

Example: 2 5 6 7

This depicts that you have four opponents with numbers 2 5 6 and 7 respectively

1. Suppose you choose to fight opponent number 5, then after winning, the max prize kitty you can win for that match is = 5*6+2 = 32
  
   Now opponent number 5 is out of the game. So opponent number 2 6 7 remain

2. Suppose you now choose to fight opponent number 2, then after winning, the max prize kitty you can win for that match is = 2*6+0 = 12. Your overall prize kitty is now 32 + 12 = 44
 
   Now opponent number 2 is out of the game. So opponent number 6 7 remain

3. Suppose you now choose to fight opponent number 6, then after winning, the max prize kitty you can win for that match is = 7*6+0 = 42. Your overall prize kitty is now 44 + 42 = 86
   Now opponent number 6 is out of the game. So opponent number 7 remains

4. After beating opponent number 7, the max prize kitty you can win for that match is 7

So overall prize kitty in this case is 93.


Other orders of choosing opponents will yield the following overall prize kitty

 Order 7->2->6->5 will yield overall prize kitty as 87

Order 2->5->6->7 will yield overall prize kitty as 88

Order 5->6->2->7 will yield overall prize kitty as 95

Order 6->7->2->5 will yield overall prize kitty as 97

But by following the order 6->5->2->7 will yield overall prize kitty as 105, which is maximum.

Yourtask is to maximize your prize kitty by taking the right decisions

Input

First line contains an integer N which denotes the number of opponents in the tournament

Second line contains N space separated integers, which are theopponent numbers of other opponents

Output

Print the maximum number of coins you can win

Constraints

1 <= N <= 500

0 <= individual coin count < 100

Time Limit

1

Examples
Example 1
Input
4
2 5 6 7
Output
105
Explanation:Refer the explanation in problem description.

Example 2
Input
3
7 8 9
Output
151
Explanation:
1. You choose to fight opponent number 8, then after winning, the max prize kitty you can win for that match is = 8*9+7 = 79
   Now opponent number 8 is out of the game. So opponent number 7 9 remain

2. Suppose you now choose to fight opponent number 7, then after winning, the max prize kitty you can win for that match is = 7*9+0 = 63. Your overall prize kitty is now 79 + 63 = 142
   Now opponent number 7 is out of the game. So opponent number 9 remains
   
3. After beating opponent number 9, the max prize kitty you can win for that match is 9

So overall prize kitty in this case is 142 + 9 = 151.
'''

def max_sum(a,n):
    sum_=0
    if n==0:
        return 0
    elif n<3:
        if n==1:
            return a[0]
        else:
            return a[0]*a[1]+max(a)
    else:
        MAX=max(a)
        i=a.index(MAX)
        
        # partition of array from max element
        if MAX==a[0]:
            b=[]
        else:
            b=a[:i+1]
        if MAX==a[-1]:
            c=[]
        else:
            c=a[i:]
            
        if len(b)!=0:
            while i-1>0:
                sum_+=b[i]*b[i-1]+b[i-2]
                b[i-1]=b[i]
                b[i]='\0'
                i-=1
            sum_+=b[0]*b[1]
        if len(c)==0:
            b[0]=b[1]
            sum_+=b[0]
            b[1]='\0'
        else:
            c=c[::-1]
            max1=c[-1]
            k=c.index(max1)
            while k-1>0:
                sum_+=c[k]*c[k-1]+c[k-2]
                c[k-1]=c[k]
                c[k]='\0'
                k-=1
            sum_+=c[0]*c[1]
            c[0]=c[1]
            c[1]='\0'
            sum_+=max1
    return sum_
n=int(input())
a=list(map(int,input().split()))
print(max_sum(a,n))