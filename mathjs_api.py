# @author anshu189
# By deafult 'requests' module is already installed with python if not found fire this command in cmd > pip install requests
import requests
chh=-1

while(int(chh)!=0):
    print("1. Try a problem\n2. Help\n0. Exit")
    helplst = ["bignumber", "boolean", "complex", "index", "number", "string", "unit", "sparse", "matrix"]
    chh = int(input("\nChoose any one: "))

    if chh == 1:
        print("\nNOTE: Don't use alphabets or invalid symbols & Algorithm Follows BODMAS Rule!")
        print("Example Input: 2+3*sqrt(10/2-1) => 8 || (2+3)*sqrt((10/2)-1) => 10\n")
        problem = input("Input your problem: ")
        api_call = f"http://api.mathjs.org/v4/?expr={problem}"
        response = requests.get(api_call)
        print(f"Your solution: {response.text}")

    elif chh == 2:
        print("\n<===== Help Desk =====>")
        print(*helplst, sep="\n")
        ch=input("Input the name of the category correctly: ")
        api_call = f"http://api.mathjs.org/v4/?expr=help({ch})"
        response = requests.get(api_call)
        print(response.text)
print("See Ya :)")
