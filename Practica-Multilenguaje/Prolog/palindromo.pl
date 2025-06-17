palindromo(Texto) :-
    atom_chars(Texto, Lista),
    include(is_alnum, Lista, Filtrado),
    maplist(to_lower, Filtrado, Normalizado),
    reverse(Normalizado, Normalizado).

is_alnum(C) :-
    char_type(C, alnum).

to_lower(C, L) :-
    char_type(L, lower(C)).
to_lower(C, C) :-
    char_type(C, lower).