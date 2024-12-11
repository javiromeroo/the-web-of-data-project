# The Web of Data Project

Este repositorio contiene los archivos hechos para poder llevar a cabo el proyecto del curso CC7220 de la Universidad de Chile. El proyecto corresponde a transformar archivos sobre Airbnbs y restaurantes en el estado de Nueva York en formato .csv a triples RDF en formato .ttl, para hacerlo se utilizó TARQL y luego se subieron los archivos al endpoint Apache Jena Fuseki, donde se realizaron consultas que utilizan ambos datasets, además se hicieron consultas sobre información geográfica utilizando LinkedGeoData e información obtenida de los datasets.

Para recrear el proyecto se deben seguir los siguientes pasos:

1. Descargar Apache Jena Fuseki y ejecutarlo
2. Descargar los 3 archivos.ttl (AB.ttl, Restaurant.ttl, Neighbourhood.ttl)
3. Cargar los 3 archivos.ttl en el endpoint de Apache Jena Fuseki
4. Realizar las queries que se encuentran en el archivo Consultas.txt o realizar nuevas queries

## Integrantes

- [Javiera Romero](https://github.com/javiromeroo)
- [Ignacio Humire](https://github.com/ihumire)
- [Vicente Thiele](https://github.com/ElVichoSiu)

## Referencias

- [TARQL](https://tarql.github.io/)
- [Apache Jena Fuseki](https://jena.apache.org/documentation/fuseki2/)
- [Dataset Airbnbs](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)
- [Dataset Restaurantes](https://www.kaggle.com/datasets/beridzeg45/nyc-restaurants?resource=download)