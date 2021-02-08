def transpose(m):
	trans = [[row[i] for row in m] for i in range(len(m[0]))]
	return trans
m = [[1,2,3]]
print(transpose(m))