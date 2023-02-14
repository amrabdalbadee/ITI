import time

def fib_memo(n, m):
    if n in m:
        return m[n]

    answer = fib_memo(n - 1, m) + fib_memo(n - 2, m)
    m[n] = answer
    return answer
def fib(n):
    m = {1: 1, 2: 1}
    return fib_memo(n, m)

# Function for nth Fibonacci number
def Fibonacci(n):
	if n < 0:
		print("Incorrect input")

	elif n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

seconds = time.time()
print(Fibonacci(40))
seconds = time.time() - seconds
print(f"the speed of fibonacci without DP is {seconds}")

seconds = time.time()
print(fib(40))
seconds = time.time() - seconds
print(f"the speed of fibonacci with DP is {seconds}")
