person(aarav, date(12, 5, 2004)).
person(priya, date(3, 9, 2003)).
person(rahul, date(21, 1, 2005)).
person(sneha, date(8, 12, 2004)).
 
birth_date(Name, Day, Month, Year) :-
    person(Name, date(Day, Month, Year)).
