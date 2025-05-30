% Definición de zonas
zona(norte).
zona(sur).
zona(este).
zona(oeste).

% Estado de sensores por zona (puedes modificar estos valores para pruebas)
humedad_suelo(norte, baja).
humedad_suelo(sur, media).
humedad_suelo(este, alta).
humedad_suelo(oeste, baja).

temperatura(norte, 35).
temperatura(sur, 29).
temperatura(este, 32).
temperatura(oeste, 33).

hora(norte, 20).
hora(sur, 15).
hora(este, 8).
hora(oeste, 21).

pronostico_lluvia(norte, false).
pronostico_lluvia(sur, true).
pronostico_lluvia(este, false).
pronostico_lluvia(oeste, false).

% 1- Regla: Hora adecuada para regar (antes de las 10 am o después de las 6 pm)
hora_adecuada(Zona) :-
    hora(Zona, H),
    (H < 10 ; H > 18).

% 2- Regla para activar riego según condiciones
activar_riego(Zona) :-
    humedad_suelo(Zona, baja),
    pronostico_lluvia(Zona, false),
    hora_adecuada(Zona).

% 3- Estado del riego
estado_riego(Zona, 'Activado') :-
    activar_riego(Zona).
estado_riego(Zona, 'No activado') :-
    \+ activar_riego(Zona).

% 4- Alerta por temperatura extrema
alerta_calor(Zona) :-
    temperatura(Zona, T),
    T >= 32.

% 5- Recomendaciones según condiciones
recomendacion(Zona) :-
    activar_riego(Zona),
    alerta_calor(Zona), !,
    format('Zona ~w: Alerta: riego activado con temperatura alta. Considere riego nocturno o por goteo.~n', [Zona]).

recomendacion(Zona) :-
    activar_riego(Zona), !,
    format('Zona ~w: Sin recomendaciones especiales para el riego.~n', [Zona]).

recomendacion(Zona) :-
    \+ activar_riego(Zona),
    format('Zona ~w: Sin recomendaciones especiales para el riego.~n', [Zona]).

% Consulta que muestra el diagnóstico completo de todas las zonas
diagnostico_total :-
    zona(Z),
    estado_riego(Z, Estado),
    format('Zona ~w: Riego ~w~n', [Z, Estado]),
    recomendacion(Z),
    fail.
diagnostico_total.
