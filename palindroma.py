confere = lambda w : (len(w) < 2) or(w[0]==w[-1] and confere(w[1:len(w)-1]))
percorre = lambda n, w : (len(w)>= n and(confere(w) or percorre(n, w[:len(w)-1])))
palindroma = lambda n, w : (len(w) >= n and(palindroma(n, w[1:]) or percorre(n, w)))
print(palindroma(int(input()), raw_input()))