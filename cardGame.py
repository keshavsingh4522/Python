'''
number card game
A game in which one card with the highest number is drawn from among several number cards. 

'''

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
