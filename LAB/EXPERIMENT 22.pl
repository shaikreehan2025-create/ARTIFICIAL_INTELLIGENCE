can_fly(sparrow).
can_fly(pigeon).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).
 
bird_status(Bird) :-
    can_fly(Bird),
    format('~w can fly.~n', [Bird]).
bird_status(Bird) :-
    cannot_fly(Bird),
    format('~w cannot fly.~n', [Bird]).
