edge(start,left).
edge(start,right).
edge(left,goal).
edge(right,goal).
heuristic(start,3).
heuristic(left,2).
heuristic(right,1).
heuristic(goal,0).
 
best_first(S, G, P) :-
    heuristic(S, H), search([H-[S]], G, R), reverse(R, P).
search([_-[G|P]|_], G, [G|P]).
search([_-[N|P]|Open], G, R) :-
    findall(H-[X,N|P],
      (edge(N,X), \+ member(X,[N|P]), heuristic(X,H)), Kids),
    append(Open,Kids,All), keysort(All,Sorted),
    search(Sorted,G,R).
