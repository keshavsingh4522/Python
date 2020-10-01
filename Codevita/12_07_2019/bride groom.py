leng = int(input())
bride = input()
groom = input()
left=0

while(True):
  if(bride[0] == groom[0]):
    bride = bride[1:]
    groom = groom[1:]
    left = 0
  else:
    groom = groom[1:] + groom[0]
    left += 1
  if(left == len(groom)):
    break
answer = len(groom)
print(answer)
