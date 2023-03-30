# Python program that returns true if there is
# a Pythagorean Triplet in a given array.

# Returns true if there is Pythagorean
# triplet in ar[0..n-1]
def isTriplet(ar, n):
	# Square all the elements
	for i in range(n):
		ar[i] = ar[i] * ar[i]

	# sort array elements
	ar.sort()

	# fix one element
	# and find other two
	# i goes from n - 1 to 2
	for i in range(n-1, 1, -1):
		# start two index variables from
		# two corners of the array and
		# move them toward each other
		b = 0
		c = i - 1
		while (b < c):
			# A triplet found
			if (ar[b] + ar[c] == ar[i]):
				return True
			else:
				if (ar[b] + ar[c] < ar[i]):
					b = b + 1
				else:
					c = c - 1
	# If we reach here, then no triplet found
	return False

# Driver program to test above function */
ar = [3, 1, 4, 6, 5]
ar_size = len(ar)
if(isTriplet(ar, ar_size)):
	print("Yes")
else:
	print("No")

# This code is contributed by Aditi Sharma
