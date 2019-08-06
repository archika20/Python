a = int(input("Enter a number to print its factorial"))

def factorial(a):
	if(a==0):
		return 1
	else:
		recurse = factorial(a-1)
		result = a * recurse
		
		return result

def fibonacci (n): 
	if n==0:
		return 0
	elif n == 1:
 		return 1
	else:
		 return fibonacci(n-1) + fibonacci(n-2)

x = factorial(a)
y = factorial(a)

print(x)
print(y)
