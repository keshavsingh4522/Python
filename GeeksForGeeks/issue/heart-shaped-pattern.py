n = 8

m = n+1

for i in range(n//2-1):
	for j in range(m):
		
		if i == n//2-2 and (j == 0 or j == m-1):
			print("*", end=" ")
			
	
		elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
							or (j-i == m//2-n//2+3 and j > m//4)):
			print("*", end=" ")
			
		
		elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
						or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
			print("*", end=" ")
			
		
		else:
			print(" ", end=" ")
	print()

for i in range(n//2-1, n):
	for j in range(m):
		
		
		if (i-j == n//2-1) or (i+j == n-1+m//2):
			print('*', end=" ")
			
		else:
			print(' ', end=" ")
			
	print()
