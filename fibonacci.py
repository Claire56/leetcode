# Given a number n, print n-th Fibonacci Number.

def fib(n):
	if n<0:
		return "wrong entry first fibonacci num is zero"
	if n ==0:
		return 0
	if n ==1:
		return 1
	else:
		return fib(n-1) + fib(n-2) 
print(fib(1))
print(fib(2))
print(fib(0))
print(fib(8))
print(fib(18))
print(fib(-18))
# Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential.
# We can observe that this implementation does a lot of repeated work (see the following recursion tree). So this is a bad implementation for nth Fibonacci number.

#                        fib(5)   
#                      /                \
#                fib(4)                fib(3)   
#              /        \              /       \ 
#          fib(3)      fib(2)         fib(2)   fib(1)
#         /    \       /    \        /      \
#   fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
#   /     \
# fib(1) fib(0)


# DYNAMIC PROGRAMMING

def fibo(n):
	# create memoi
	fiboList =[0,1]

	while len(fiboList)< (n+1):
		fiboList.append(0)
	
	if n<=1:
		return n
	else:
		if fiboList[n-1]==0:
			fiboList[n-1] = fibo(n-1) 

		if fiboList[n-2] == 0:
			fiboList[n-2] = fibo(n-2)

	fiboList[n]= fibo(n-1)+ fibo(n-2)

	return fiboList[n]

print(fibo(1))
print(fibo(2))
print(fibo(0))
print(fibo(8))
print(fibo(18))
print(fibo(-18))

# Function for nth fibonacci number - Space Optimisataion 
# Taking 1st two fibonacci numbers as 0 and 1 

def fibonacci(n):
	a=0
	b=1

	if n<=1:
		return n
	else:
		for i in range(2, n+1):
			c = a+b
			a=b
			b=c
		return b
  


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(0))
print(fibonacci(8))
print(fibonacci(18))
print(fibonacci(-18))


















