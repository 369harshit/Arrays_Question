# Python program to implement
# the above approach
# Returns true if the there is a subarray
# of arr[] with sum equal to 'sum' otherwise
# returns false. Also, prints the result
def subArraySum(arr, n, sum_):
	
	# Pick a starting point
	for i in range(n):
		curr_sum = arr[i]
	
		# Try all subarrays starting
		# with 'i'
		j = i + 1
		while j <= n:		
			if curr_sum == sum_:
				print ("Sum found between indexes %d and %d"%( i, j-1))				
				return 1
				
			if curr_sum > sum_ or j == n:
				break
			curr_sum = curr_sum + arr[j]
			j += 1
   
	print ("No subarray found")
	return 0

# Driver code
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23
subArraySum(arr, n, sum_)
