fibonacci = lambda n: (n<3 and 1) or (fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(int(raw_input())))