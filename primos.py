verifica = lambda i, x : ((i < x) and ((x % i == 0) or (verifica(i + 1, x))))
primos = lambda l : filter(lambda x : not verifica(2,x), l)
print(primos(map(int, raw_input().split())))