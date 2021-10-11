def isPalindrome(s):
    if(s[:] == s[::-1]):
        return True
    return False
  
  
# Driver code 
s = str(input("Enter a string \n"))
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 
