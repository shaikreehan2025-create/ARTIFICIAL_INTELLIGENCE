hanoi(1, From, To, _) :-
    format('Move disk from ~w to ~w~n',
           [From, To]).
 
hanoi(N, From, To, Aux) :-
    N > 1,
    Next is N - 1,
    hanoi(Next, From, Aux, To),
    format('Move disk from ~w to ~w~n',
           [From, To]),
    hanoi(Next, Aux, To, From).
