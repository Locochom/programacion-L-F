# BASE DE CONOCIMIENTOS DE PELíCULAS EN PROLOG

Este proyecto es una base de conocimiento sobre películas implementada en Prolog que permite realizar consultas sobre diversos aspectos del cine.


## Requisitos

- [SWI-Prolog](https://www.swi-prolog.org/) instalado en tu sistema.


## Archivos

- `base_de_conocimiento_peliculas.pl`: Contiene los hechos (datos de películas) y reglas (consultas posibles).


## Cómo usar

1. Abre SWI-Prolog.
2. Carga el archivo con el comando: `consult('base_de_conocimiento_peliculas.pl').`.
3. Realiza consultas utilizando las reglas definidas.


## CONSULTAS DISPONILBES

### Consultas básicas
- `pelicula(Titulo, Generos, Actor, Director, Calificacion, Anio).` - Consulta todos los datos de una película

### Consultas especializadas
- `altamente_recomendada(Titulo).` - Películas con calificación IMDb ≥ 8.5
- `peliculas_por_actor(Actor, Titulo).` - Películas de un actor específico
- `peliculas_por_ano(Anio, Titulo).` - Películas estrenadas en un año específico
- `recomendada_para_fans_de_genero(Titulo, Genero).` - Películas de un género con calificación > 8.0
- `peliculas_por_director(Director, Titulo).` - Películas de un director específico
- `tienen_genero_en_comun(Titulo1, Titulo2, Genero).` - Películas que comparten un género
- `peliculas_destacadas_por_ano(Anio, Titulo).` - Películas con calificación > 8.0 en un año
- `pelicula_clasica(Titulo).` - Películas estrenadas antes del 2000
- `pelicula_reciente(Titulo).` - Películas estrenadas desde 2020
- `peliculas_por_decada(Decada, Titulo).` - Películas de una década específica (ej: 1990)


## Ejemplos de consultas

1. Películas altamente recomendadas (≥8.5)
    altamente_recomendada(Titulo).
    Ejemplo de resultado: Titulo = 'Inception'

2. Películas por actor
    peliculas_por_actor('Timothee Chalamet', Titulo).
    Ejemplo de resultado: Titulo = 'Dune' ; Titulo = 'Dune 2' ; Titulo = 'Bones and All'

3. Películas por año
    peliculas_por_ano(2019, Titulo).
    Ejemplo de resultado: Titulo = 'Midsommar' ; Titulo = 'Parasite' ; Titulo = 'Jojo Rabbit'

4. Recomendadas para fans de un género
    recomendada_para_fans_de_genero(Titulo, animacion).
    Ejemplo de resultado: Titulo = 'Your Name' ; Titulo = 'Spider-Man: Into the Spider-Verse'

5. Películas por director
    peliculas_por_director('Quentin Tarantino', Titulo).
    Ejemplo de resultado: Titulo = 'Kill Bill Vol.1' ; Titulo = 'Kill Bill Vol.2' ; Titulo = 'Pulp Fiction'

6. Películas con género en común
    tienen_genero_en_comun('Inception', 'The Matrix', Genero).
    Ejemplo de resultado: Genero = ciencia_ficcion ; Genero = accion

7. Películas destacadas por año
    peliculas_destacadas_por_ano(2023, Titulo).
    Ejemplo de resultado: Titulo = 'Oppenheimer' ; Titulo = 'Spider-Man: Across the Spider-Verse'

8. Películas clásicas (antes de 2000)
    pelicula_clasica(Titulo).
    Ejemplo de resultado: Titulo = 'The Shining' ; Titulo = 'Alien' ; Titulo = 'Pulp Fiction'

9. Películas recientes (≥2020)
    pelicula_reciente(Titulo).
    Ejemplo de resultado: Titulo = 'Dune' ; Titulo = 'Everything Everywhere All at Once'

10. Películas por década
    peliculas_por_decada(2010, Titulo).  % Películas de la década 2010-2019
    Ejemplo de resultado: Titulo = 'Inception' ; Titulo = 'Whiplash' ; Titulo = 'Parasite'


## Géneros disponibles

Los géneros incluidos en la base de conocimiento son:
- ciencia_ficcion
- drama
- musical
- romance
- accion
- thriller
- terror
- comedia
- animacion
- fantasia
- aventura
- crimen
- psicologico
- familia
- misterio
- biografia
- historia
- guerra
- slasher
- satira