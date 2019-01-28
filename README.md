# Lisibilite
Repo for maintaining the code base for hybrid readability index calculation application. 
It is called Lisibilite - meaning Readability in French.

## Why this name?
Because, it sounded fun!

# **** Draft ****

# Key Contributors
* Shyam Mohan K
* Viren Chhabria
* Arun Thundyill Saseendran

# Tech Stack
| Attribute | Choice |
| ------ | ----- |
|Language|Python|
|Linter|Pylint|
|Formatting|pep8|
|Package Management|Pip/Conda|
|Framework|Django|
|Containerization|Docker|
|Orchestration|Kubernetes|

# Wiki
https://github.com/ats0stv/Lisibilite/wiki

# Primary User Stories
* An elegant responsive web application where the user can upload a Doc, PDF or text file and view the readability metrics.
* A user should be able to download a well-formatted report in PDF with a custom headline and the metrics of the uploaded document
* The user should be able to easily understand the interpretation of the metrics with well-formed graphs/charts
* The application should also provide metrics such as the number of words, number of sentences, and number of paragraphs 
> The user should have the option to ignore titles, sub-headings, figure captions, table captions, references etc
* There should be support for HATEOAS, HAL compliant fine-grained ReST APIs for all the above features.
> The APIs should be secured by API Tokens (The generation of API tokens for users can be made self service on a later stage. Initially it will be on request)


