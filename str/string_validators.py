if __name__ == '__main__':
    s = raw_input()
if len(s)>0 and len(s)<1000:
    an=0
    al=0
    d=0
    l=0
    u=0
    for i in s:
        if i.isalnum():
            an+=1
        if i.isalpha():
            al+=1
        if i.isdigit():
            d+=1
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
    if an!=0:
        print(True)
    else:
        print(False)
    if al!=0:
        print(True)
    else:
        print(False)
    if d!=0:
        print(True)
    else:
        print(False)
    if l!=0:
        print(True)
    else:
        print(False)
    if u!=0:
        print(True)
    else:
        print(False)
 '''
 Task

You are given a string . 
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
 '''
