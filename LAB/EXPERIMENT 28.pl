symptom(amy, fever).
symptom(amy, cough).
symptom(amy, body_ache).
symptom(ben, sneezing).
symptom(ben, itchy_eyes).
 
diagnosis(P, flu) :-
    symptom(P, fever),
    symptom(P, cough),
    symptom(P, body_ache).
diagnosis(P, allergy) :-
    symptom(P, sneezing),
    symptom(P, itchy_eyes).
