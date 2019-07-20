class positive(Exception):
 pass
class negative(Exception):
 pass
class zero(Exception):
 pass
def whatsign(n):
 if n==0:
  raise zero('number is zero')
 if n>0:
  raise positive('number is +ve')
 if n<0:
  raise negative('number is -ve')
if __name__=='__main__':
 n=int(input('enter a number: '))
 try:
  whatsign(n)
 except Exception as e:
  print('!',e)
 else:
  print('no error')
'''
output:
enter a number: 5
! number is +ve
enter a number: -7
! number is -ve
enter a number: 0
! number is zero
'''
