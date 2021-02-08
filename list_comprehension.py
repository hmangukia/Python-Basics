h = []
for l in "John":
	h.append(l)
print(h)


##########
h = [l for l in "John"]
print(h)

print("===================")
l = list(map(lambda x: x, "John"))
print(l)

print("=================")

#conditional
n_list = [x for x in range(20) if x % 2 == 0]
print(n_list)

#nested if
# check both divisible by 2 and 5
n = [y for y in range(100) if y%2 == 0 if y % 5 == 0]
print(n)

# if esle
n = ["even" if i%2 == 0 else "odd" for i in range(20)]
print(n)