%% Usar SWI-PROLOG
%% Interpretador web: SWISH

% Relações familiares bíblicas
mae(eva, caim).
mae(eva, abel).
pai(adao, caim).
pai(adao, abel).
pai(caim, enoque).

irmaos(X, Y) :-
    pai(Z, Y), pai(Z, X), X \= Y;
    mae(Z, Y), mae(Z, X), X \= Y.

genitor(X, Y) :-
    pai(X, Y), X \= Y;
    mae(X, Y), X \= Y.

neto(X, Z) :-
    genitor(X, Y), genitor(Y, Z).


% Mundo de blocos
sobre(c,a).
sobre(b,d).
sobre_a_mesa(a).
sobre_a_mesa(d).
sobre_a_mesa(e).

livre(X) :-
    % \+ é o operador de quantificação existencial
    sobre_a_mesa(X), \+(sobre(_,X));
    sobre(X,_), \+(sobre(_,X)).