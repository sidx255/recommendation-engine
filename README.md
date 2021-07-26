# Team HackOverflow - Recommendation Engine

Recommendation Engine, developed @ Bajaj FInserv's HackRX '21 by Team HackOverflow

## Description

Simple Python Implementation of recommendation engine. The following were components of the final solution after the hack:

### 1) URL crawl
We write a script to find all possible Bajaj Finserv (https://www.bajajfinserv.in/) Internal URLs + External URLs, and obtain the meta description and keywords from the content of the website.
Dependencies: BeautifulSoup, Requests

### 2) Data Cleansing
Once we obtain all URLs and corresponding keywords in a CSV file, we will get rid of incorrect, irrelevant, or corrupted data from the CSV file.
Dependencies: Pandas, Numpy

### 3) Keyword Extraction
For the extraction of keywords/topics from the search query entered by the user, we will be using LDA, an exmaple of topic model and is used to classify text in a document to a particular topic. It builds a topic per document model and words per topic model, modeled as Dirichlet distributions, which will be used to generate keyword recommendations for the search query.
Dependencies: NTLK, Gensim

### 4) Word Association
Next, we will be using WordNet, which is a lexical database specifically designed for natural language processing, to find the word associations of the extracted keywords. We will be using the natural language toolkit in order to look up word associations from this database
Dependencies: wordnet


## Getting Started

### Dependencies

* Python 3.x
* Node JS
* EJS

### Installing
* Preferably, create a python system-site virtual environment
* Activate the venv
* Install NodeJS 

### Execution
* Clone and set working directory
```
git clone https://github.com/HackRx2-0/ps4_hackoverflow
cd ps4_hackoverflow
```
* Install Python packages from requirements.txt
```
pip install -r requirements.txt
```
* Install Node packages
```
npm install
```
* Run App
```
npm start
```
  or
```
node server.js
```
* Open [http://localhost:3000](https://localhost:3000)

## Other Functions
### URL crawling
```
python extractor.py -m MAX_CRAWL_URL https://www.bajajfinserv.in/
```
where, MAX_CRAWL_URL = Integer(Number of maximum URLs to be crawled)

### Word Association
```
python wordass.py
```
Find similarities/associations or correlations with words in a document


## Help
Please contact anyone of the authors

## Authors

* Siddharth Sharma [@sidx255](https://github.com/sidx255)
* Riya Kumar [@RiyaKumar00](https://github.com/RiyaKumar00)
* Milan Mandal [@milanmandal](https://github.com/milanmandal)

## Acknowledgments

* [BERT](https://github.com/google-research/bert)
* [NTLK](https://www.nltk.org/)
* [YAKE](https://github.com/LIAAD/yake)
* [Wordnet for NTLK](https://pythonprogramming.net/wordnet-nltk-tutorial/)
