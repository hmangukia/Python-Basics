# GCD : Greates common divisor of two number

def gcd(m,n):

  # Initialized empty list for factors of m
  # Calculate factors and append in empty list
  fm = []
  for i in (1, m+1):
    if(m%i) == 0:
      fm.append(i)

  # Initialized empty list for factors of m    
  # Calculate factors and append in empty list
  fn = []
  for j in range(1, n+1):
    if (n%j) == 0:
      fn.append(j)

   # Initialized empty list for common factors and then append and return last element
  cf = []
  for f in fm:
    if f in fn:
      cf.append(f)
  return(cf[-1])

print(gcd(12,4))