## Keyword topic modeling data 

This repository has two files. The first one (keywords_description.json) contains the name of a software repo (e.g., https://w3id.org/okn/i/Software/abrahamnunes/fitr, the repo name is the last part, i.e., abrahamnunes/fitr) and a keyword list extracted from its description, automatically. 

The second file contains the similar information but with keywords added manually by the authors.


Data has been extracted from SOSEN: https://dev.endpoint.mint.isi.edu/dataset.html

Queries (keywords_description.json): 

```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sdm: <https://w3id.org/okn/o/sdm#>
PREFIX sd: <https://w3id.org/okn/o/sd#>
PREFIX ex: <http://example.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select  ?soft (GROUP_CONCAT(DISTINCT ?o;SEPARATOR=', ') AS ?description_keywords) where {
  ?s <https://w3id.org/okn/o/sosen#hasDescriptionKeyword>/rdfs:label ?o.
  
}group by ?soft 
```

and  (keywords.json)

```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sdm: <https://w3id.org/okn/o/sdm#>
PREFIX sd: <https://w3id.org/okn/o/sd#>
PREFIX ex: <http://example.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select  ?soft (GROUP_CONCAT(DISTINCT ?o;SEPARATOR=', ') AS ?keywords) where {
  ?soft sd:keywords ?o.
  
}group by ?soft
```
