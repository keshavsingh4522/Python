'''
Constellation

Problem Description

Three characters { #, *, . } represents a constellation of stars and galaxies in space. Each galaxy is demarcated by # characters. There can be one or many stars in a given galaxy. Stars can only be in shape of vowels { A, E, I, O, U } . A collection of * in the shape of the vowels is a star. A star is contained in a 3x3 block. Stars cannot be overlapping. The dot(.) character denotes empty space.

Given 3xN matrix comprising of { #, *, . } character, find the galaxy and stars within them.

Note: Please pay attention to how vowel A is denoted in a 3x3 block in the examples section below.

Constraints

3 <= N <= 10^5

Input

Input consists of single integer N denoting number of columns.

Output

Output contains vowels (stars) in order of their occurrence within the given galaxy. Galaxy itself is represented by # character.

Time Limit

1

Examples

Example 1

Input

18

* . * # * * * # * * * # * * * . * .

* . * # * . * # . * . # * * * * * *

* * * # * * * # * * * # * * * * . *

Output

U#O#I#EA

Explanation

As it can be seen that the stars make the image of the alphabets U, O, I, E and A respectively.



 
                                                                                                                                                                                                                                                                                                                                            

Example 2

Input

12

* . * # . * * * # . * .

* . * # . . * . # * * *

* * * # . * * * # * . *

Output

U#I#A

Explanation

As it can be seen that the stars make the image of the alphabet U, I and A.

'''

n=int(input())
a = [[0 for i in range(n)] for j in range(3)]
for i in range(3):
    a[i][:]=input().split()
s=''
j=0
while j<n:
    if a[i][j]=='#':
        s+='#'
        j+=1
        continue
    elif a[0][j]=='.' and a[1][j]=='.' and a[2][j]=='.':
        j+=1
        continue
    elif a[1][j]=='.':
        s+='I'
        j+=3
        continue
    elif a[1][j+1]=='.':
        if a[0][j+1]=='.':
            s+='U'
        else:
            s+='O'
        j+=3
        continue
    elif a[0][j]=='.':
        s+='A'
        j+=3
        continue
    else:
        s+='E'
        j+=3
        continue
print(s)