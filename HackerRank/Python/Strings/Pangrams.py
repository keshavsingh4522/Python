#https://www.hackerrank.com/challenges/pangrams/problem
def pangrams(s):
    s=s.lower()
    if ' ' in s:
        for i in range(25):
            if chr(i+97) not in s:
                return('not pangram')
        return('pangram')
    return('not pangram')
pangrams(input())