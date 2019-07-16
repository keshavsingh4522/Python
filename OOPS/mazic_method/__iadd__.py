class Indexer:
 def __index__(self):
  return int(input('enter a number: '))
obj=Indexer()
print(bin(obj))
print(oct(obj))
print(hex(obj))
'''
output:
enter a number: 22
0b10110
enter a number: 44
0o54
enter a number: 94
0x5e
'''
