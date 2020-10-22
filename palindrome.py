def checkIfPalindrome(s):
    return s == s[::-1]
    
s = "A Santa Lived As a Devil At NASA"
ans = checkIfPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
