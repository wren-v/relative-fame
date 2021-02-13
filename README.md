# Relative Fame
A data science project to determine what cities in a given state were/are home to the most "famous" people per capita.

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is to find which cities are connected to the least famous people, which have a standard level of fame, and which punch above their weight class with regards to fame.

### Methods Used
* Statistics
* Data Visualization

### Technologies
* Python
* XML
* Tableau

### Resources
* [Wikipedia Special Export](https://en.wikipedia.org/wiki/Special:Export)

## Project Description
The source of data for this project Wikipedia's Special Export, which exports the contents of specified Wikipedia pages to XML. Exporting "Category:Cities in Iowa" yields the complete text for all the pages that correspond with cities in Iowa. By then parsing the information from this XML file, a new file can be created with contains the name of a city, and all of the notable residents associated with it.
* Limitation: As Wikipedia relies on volunteer contributors, the notable people section of each page may be inaccurate, either containing a person not associated with a city, or not containing a person (with a Wikipedia article) related to that city.

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data for Iowa is [here](CitiesInIowa.xml) within this repo.    
3. Data processing/transformation scripts are being kept [here](mineCities)

## Contact
* Feel free to contact me with any questions about this project. My email is "wvogelschmidt" + "@" + "colgate.edu"
