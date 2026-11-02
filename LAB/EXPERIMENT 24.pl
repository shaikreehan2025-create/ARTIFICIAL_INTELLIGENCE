diet(diabetes, 'low-sugar meals').
diet(diabetes, 'whole grains and vegetables').
diet(hypertension, 'low-salt meals').
diet(hypertension, 'fruits and vegetables').
diet(anemia, 'iron-rich foods').
 
suggest(Disease, Food) :-
    diet(Disease, Food).
