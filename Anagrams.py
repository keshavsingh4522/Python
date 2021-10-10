str1 = str(input("Enter first string: "))
str2 = str(input("Enter second string: "))
str1 = str1.lower()
str2 = str2.lower()
print(str1)
print(str2)
if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagrams")
    else:
        print(str1 + " and " + str2 + " are not anagrams")

else:
    print(str1 + " and " + str2 + " are not anagrams")