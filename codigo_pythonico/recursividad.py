def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

print(factorial(4))


#Fibonacci con recursividad

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)