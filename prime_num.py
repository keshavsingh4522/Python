def primegen(maxn=float("inf"),count=float("inf")):
	#Sequentially output primes. Outputs all p<maxn or the first 'count' primes.
	for n in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47):
		if n>=maxn or count<=0: return
		yield n
		count-=1
	#Recursive generator for upcoming factors.
	r,sq,n=7,49,49
	it=iter(primegen())
	while next(it)<r: pass
	comp=dict()
	jump=(1,6,5,4,3,2,1,4,3,2,1,2,1,4,3,
	      2,1,2,1,4,3,2,1,6,5,4,3,2,1,2)
	while n<maxn and count>0:
		#See if we have a factor of n.
		f=comp.pop(n,0)
		if n==sq:
			#n=r*r is the next prime square we're waiting for.
			f,r=r,next(it)
			sq=r*r
		elif f==0:
			#n!=sq and isn't in comp, so it's prime.
			yield n
			count-=1
		if f:
			#We've found a factor of n. Add it to comp.
			q=n//f
			q+=jump[q%30]
			while q*f in comp: q+=jump[q%30]
			comp[q*f]=f
		n+=jump[n%30]

    
print("First 20 primes : "+str(list(primegen(count=20))))
print("Primes under 100: "+str(list(primegen(100))))
print("Loop iterator test:")
for p in primegen():
	if p>50: break
	print(p)
