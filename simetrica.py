pertence = lambda x, l : (len(l) > 0 and (l[0] == x or pertence(x, l[1:])))
diferenca = lambda a, b : (len(a) > 0 and ((not pertence(a[0], b) and [a[0]] + diferenca(a[1:], b)) or (diferenca(a[1:], b)))) or []
uniao = lambda a, b : a+b
simetrica = lambda a, b : uniao(diferenca(a,b), diferenca(b,a))
print(simetrica(map(int, raw_input().split()), map(int, raw_input().split())))
