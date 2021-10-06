#A simple code for Pronic Number

#Pronic Number - it is a number which is the product of two consecutive integers.

num=int(input(''))
root=int(num**(0.5))
if num==root*(root+1):
  print(num," is Pronic Number")
else:
  print(num," is not a Pronic Number")
