parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,pat).
parent(bob,ann).
parent(pat,jim).

male(tom).
male(bob).
male(jim).

female(liz).
female(pat).
female(ann).
female(pam).


child(X,Y):-parent(Y,X).

mom(X,Y):-parent(X,Y),female(X).

grandparent(X,Y):-parent(X,Z),parent(Z,Y).

sameparent(X,Y):-parent(Z,Y),parent(Z,X),X\==Y.

sister(X,Y):-parent(Z,Y),parent(Z,X),female(X).
