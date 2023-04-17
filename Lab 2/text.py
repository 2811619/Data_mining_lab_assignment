'''
CIS-660 Lab 2 Assignment
Author: Mohamed Gani Mohamed Sulthan
CSU ID: 2811619
Major: Master’s in computer science
'''

# Import all the required modules
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import numpy as np
import pandas as pd

import nltk
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

'''Function defining the web-crawler/core, which will fetch information from a given website, and push the contents to
the second function calculating_frequency                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ()'''
def start(url):

	# empty list to store the contents of
	# the website fetched from our web-crawler
	wordlist = []
	stemWordList = []

	# Sunnie website
	# session = requests.Session()
	# retry = Retry(connect=3, backoff_factor=0.5)
	# adapter = HTTPAdapter(max_retries=retry)
	# session.mount('http://', adapter)
	# session.mount('https://', adapter)
	#
	# session.get(url)

	source_code = requests.get(url, verify = False).text

	# BeautifulSoup object will ping the requested url for data
	soup = BeautifulSoup(source_code, 'html.parser')

	# Storing the content of the page by using get_text in soup object
	# content = soup.findAll("div",{"id" : "page"})
	# print("content",content)

	#content = soup.find('div').text
	content = soup.get_text()

	# changing the set of words in to lower cases
	lowerCaseWords = content.lower()
	#print("lower: ", lowerCaseWords)
	new_text = re.sub(r"[^a-zA-Z0-9 ]", "", lowerCaseWords)
	#print("Removed sepcial characters: ", new_text)

	# Storing the single words and storing in to the list
	words = lowerCaseWords.split()
	#print("Storing single word in the list: ", words)

	# stemming
	ps = PorterStemmer()
	words = word_tokenize(new_text)
	for w in words:
		wordlist.append(w)
		stemWordList.append(ps.stem(w))
		# print(w, " : ", ps.stem(w))

	#print("Actual word", wordlist)
	#print("Stemming word:", stemWordList)
	# for each_word in words:
	# 	wordlist.append(each_word)

	# res = [(x, i.split()[j + 1]) for i in words
	# 	   for j, x in enumerate(i.split()) if j < len(i.split()) - 1]
	#
	# print(res)

	# sending the single word list to clean the content having unwanted symbols and count
	calculating_frequency(words)

	# Bigrams findings
	bigram = ['machine learning', 'data mining', 'deep_learning']

	print("\nBigrams words counts:")
	for i in bigram:
		print(i, "appears", len(re.findall(i, lowerCaseWords)), "times")

	# Splitting the words in to bigrams and put it in the list
	nltk_tokens = nltk.word_tokenize(lowerCaseWords)
	bigramsWordList = list(nltk.bigrams(nltk_tokens))
	# print("The formed bigrams are : ", bigramsWordList)

	# clean_wordlist(bigramsWordList)


# Function removes any unwanted symbols
def calculating_frequency(wordlist):

	clean_list = []
	for word in wordlist:
		symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

		for i in range(len(symbols)):
			word = word.replace(symbols[i], '')

		if len(word) > 0:
			clean_list.append(word)
	# print('clean', clean_list)

	count = pd.value_counts(np.array(clean_list))
	#print(count)

	# print(f'"research" appears {clean_list.count("research")} time(s)')
	print("Single word counts:")
	singleWord = ['research', 'data', 'mining', 'analytics']
	list = []
	for i in singleWord:
		print(i, "appears", clean_list.count(i),"times")

# Driver code
if __name__ == '__main__':
	url = ["https://www.edx.org/course/data-science-machine-learning", "https://en.wikipedia.org/wiki/Engineering", "http://my.clevelandclinic.org/research", "https://en.wikipedia.org/wiki/Data_mining",
		   "https://en.wikipedia.org/wiki/Data_mining#Data_mining", "https://eecs.csuohio.edu/~sschung/"]
	urlString = 0
	for i in url:
		# url = "https://en.wikipedia.org/wiki/Data_mining"
		# starts crawling and prints output
		urlString += 1
		print("\nDoc",urlString,"finding term frequecy process started")
		start(i)
