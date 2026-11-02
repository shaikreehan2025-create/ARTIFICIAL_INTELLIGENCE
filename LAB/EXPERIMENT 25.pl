banana_at(middle).
 
action(state(M,B,floor,no), walk, state(B,B,floor,no)) :-
    M \= B.
action(state(P,P,floor,no), push, state(middle,middle,floor,no)) :-
    banana_at(middle), P \= middle.
action(state(middle,middle,floor,no), climb, state(middle,middle,box,no)).
action(state(middle,middle,box,no), grab, state(middle,middle,box,yes)).
 
plan(state(_,_,_,yes), []).
plan(S,[A|Rest]) :- action(S,A,N),
    plan(N,Rest).
 
solution(Plan) :- plan(state(door,window,floor,no), Plan).
