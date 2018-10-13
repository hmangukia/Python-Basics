l_primes = [ 2 ]
for i in range( 3, 1000, 2 ):
	for j in l_primes:
		if 0 == i%j:
			break
	else:
		l_primes.append( i )

print( "\n".join([ str(_) for _ in l_primes ]) )
