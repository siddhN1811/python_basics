#Generators Are Single-Iteration Objects
p=print
l1=list(range(5))
p(l1)
g1=iter(l1)
p(next(g1))
p(next(g1))
p(next(g1))
p()
g2=iter(l1)
p(next(g2))
p(next(g2))
p(next(g2))
p()
g3=(x for x in range(5))
w1=iter(g3)
p(next(w1))
p(next(w1))
w2=iter(g3)
p(next(w2))
p(next(w2))