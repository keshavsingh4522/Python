def checkIfPalindrome(s):
    return s == s[::-1]
    
n=int(input())
s=input()
ans = checkIfPalindrome(s)
ans2 = checkIfPalindrome(str(n))
 
if ans:
    print("Yes the string is a palindrome")
else:
    print("No the string is a palindrome")
if ans2:
    print("Yes the number is a palindrome")
else:
    print("No the number is a palindrome")
