soma = lambda l : reduce(lambda x, y : x + y, l)
media = lambda l : soma(l) / len(l)
num = lambda x, l : map(lambda y : (y - x)*(y - x), l)
desvio = lambda l : (soma(num(media(l), l))/len(l))**(1/2.0)
tupla = lambda l : (media(l), desvio(l))
print(tupla(map(float, raw_input().split())))