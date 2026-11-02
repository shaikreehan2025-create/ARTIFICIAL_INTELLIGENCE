male(john).
male(peter).
female(mary).
female(alice).
female(susan).
parent(john, mary).
parent(john, peter).
parent(mary, alice).
parent(peter, susan).
 
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
