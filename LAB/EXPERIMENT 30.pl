fact(rain).
rule(wet_grass, [rain]).
rule(slippery_road, [wet_grass]).
 
backward_chain(Goal) :-
    fact(Goal).
backward_chain(Goal) :-
    rule(Goal, Conditions),
    prove_all(Conditions).
prove_all([]).
prove_all([Goal|Rest]) :-
    backward_chain(Goal),
    prove_all(Rest).
