#__author__ = "Badal"

def merge_sort(array):
	"""
		This function takes an array and returns a new sorted array.
	"""
	# find the mid point which takes into account even and odd length arrays
	mid = int(len(array) / 2)
	if len(array) == 1 :
		return array
	else: 
		# recursively call merge_sort on each half of the input array and returns the merged result 
		return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


	


def merge(arr1, arr2):
	"""
		This function takes two sorted functions and combines them into a new sorted array
	"""
	max1 = len(arr1)
	max2 = len(arr2)
	index1 = 0
	index2 = 0
	result = []
	#while loop iterates until either input array has been exhausted
	while index1 < max1 and index2 < max2:
		if arr1[index1] <= arr2[index2]:
			result.append(arr1[index1])
			index1 += 1
		else: 
			result.append(arr2[index2])
			index2 += 1

	# add the array that was not finished to the end of the result array
	if index1 == max1:
		result += arr2[index2:]
	else: 
		result += arr1[index1:]
	return result



test_array = [5, 4, 3, 8, 5, 8, 110, 23123, 32, 55, 4, 34, 4, 6, 53]

print(merge_sort(test_array))