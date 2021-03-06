def sum_series(n,m=0,o=1):
	"Starting with m and o, take the nth term of the sequence generated by recursively summing."
	if n ==1:
		return m
	elif n==2:
		return o
	else:
		return sum_series(n-1,m,o)+sum_series(n-2,m,o)
def fibonacci(n):
	"Applies sum_series with m=0,o=1"
	return sum_series(n)
def lucas(n):
	"Applies sum_series with m=2, o=1"
	return sum_series(n,2,1)

if __name__ == '__main__':
	#check to make sure everything agrees with known values
	assert lucas(8)==sum_series(8,2,1)
	assert fibonacci(17)==sum_series(17)
	assert lucas(8)==29
	assert fibonacci(7)==8
	assert sum_series(4,3,2)==7
	print("No errors...yet")