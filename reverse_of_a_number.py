def reverse(n):
	reverse = 0
	while n > 0:
		rem = n % 10
		reverse = reverse*10 + rem
		n = n // 10
	return reverse
# test cases

print(reverse(3151))
print(reverse(4))
print(reverse(15135324234235))