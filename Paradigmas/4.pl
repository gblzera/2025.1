pai(joao, maria).
pai(joao, pedro).
mae(ana, maria).
mae(ana, pedro).

irmao(X, Y) :- pai(P, X), pai(P, Y), mae(M, X), mae(M, Y), X \= Y.

#saida:
#?- irmao(maria, pedro).
#true.