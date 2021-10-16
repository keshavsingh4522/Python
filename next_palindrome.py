def next_palindrome(n):
    while(True):
        n += 1
        if(str(n) == str(n)[::-1]):
            return(n) 

n = int(input())
print(next_palindrome(n))
