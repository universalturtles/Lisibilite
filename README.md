Website: https://universalturtles.github.io/Lisibilite/

[![CodeFactor](https://www.codefactor.io/repository/github/universalturtles/lisibilite/badge)](https://www.codefactor.io/repository/github/universalturtles/lisibilite)

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
* Debrup Chakraborty

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

# MVP

* A Web UI where a user can paste a block of text and when clicked submit gives back the readability scores
> The readability scores should be easily understandable and a graph possibly
> Display the text is suitable for what age
* An API that can be access to post a text and gives back a readability score JSON
> Should have token access and should be rate limited
* Users should be able to sign-up and see history of submitted text after sign-in

## First Thoughts

* An elegant responsive web application where the user can upload a Doc, PDF or text file and view the readability metrics.
* A user should be able to download a well-formatted report in PDF with a custom headline and the metrics of the uploaded document
* The user should be able to easily understand the interpretation of the metrics with well-formed graphs/charts
* The application should also provide metrics such as the number of words, number of sentences, and number of paragraphs 
> The user should have the option to ignore titles, sub-headings, figure captions, table captions, references etc
* There should be support for HATEOAS, HAL compliant fine-grained ReST APIs for all the above features.
> The APIs should be secured by API Tokens (The generation of API tokens for users can be made self-service on a later stage. Initially it will be on request)

## Based on Additional Brain Storming
- Word Counts with an ability to filter out articles, titles, figures, tables, references etc., (Academic)
- Ability to create readability reports with custom title and sections
*Some sections in the report can be* 
    - Lisibilite Readability Graph - Something in my mind
    - Word Density Analysis
    - Noun Phrase / Verb Phrase Composition Analysis
    - And one day - some day - Summary / Abstract of the text
    - Text Sentiment - someday - one day
    - Spelling Errors
- An API for programmatic access to our service (**No one has given it as such**)
    - Initially, it will be very much rate limited. We can see how we can extend it.
- One day, someday, we can start supporting other languages - **that will be yoyo**
- I believe we must give the facility of user accounts. We must also categorize some of our features as "Premium", for which they will have to pay :P (Of course all these would be after we get enough user traffic). That would also give us scope for some user-specific analytics.
* The service should be available as MS Word Plugin
* The service should be available as a LibreOffice Plugin
* The service should be available as a responsive cross-platform application server over the cloud.


# A sample Django REST Webapp

https://github.com/rupdeb/PythonWebapp.git

