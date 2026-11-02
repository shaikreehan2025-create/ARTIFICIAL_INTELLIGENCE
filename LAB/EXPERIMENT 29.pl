:- dynamic fact/1.
fact(rain).
rule(wet_grass, [rain]).
rule(slippery_road, [wet_grass]).
 
forward_chain :-
    rule(NewFact, Conditions),
    forall(member(C, Conditions), fact(C)),
    \+ fact(NewFact),
    assertz(fact(NewFact)),
    !,
    forward_chain.
forward_chain.
