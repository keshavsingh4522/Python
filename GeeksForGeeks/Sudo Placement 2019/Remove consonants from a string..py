# Remove consonants from a string
# Difficulty: Basic   Marks: 1
'''
Given a string s, remove all consonants and prints the string s that contains vowels only.
Input: The first line of input contains integer T denoting the number of test cases. For each test case, we input a string.
Output: For each test case, we get a string containing only vowels. If the string doesn't contain any vowels, then print "No Vowel"

Constraints:

1<=T<=100

The string should consist of only alphabets.

Examples:

Input: geEks
Output: eE
Input: what are you doing
Output: a ae ou oi
'''
for _ in range(int(input())):
    s=input().split(' ')
    c=0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] in 'aeiouAEIOU':
                print(s[i][j],end='')
                c+=1
        if c>0:
            print(end=' ')
    if c==0:
        print("No Vowel")
    else:
        print()
