def check_if_palindrome(s):
    return s == s[::-1]
    
s = "A Santa Lived As a Devil At NASA"
ans = check_if_palindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

    
def next_palindrome(value):
    while not check_if_palindrome(str(value)):
        value =int(value) +1
    return value
