# Import all the required modules
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import numpy as np
import pandas as pd

import string
import nltk
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os

# Define the location of the directory
path = r"C:/Users/Gani/Desktop/Cleveland State University/Third Sem/Data Mining/Lab/Lab 2/"

# Change the directory
os.chdir(path)
list = []
wordsCountAll = []
# stemWordList = []

# Iterate over all the files in the directory
for file in os.listdir():
 if file.endswith('.txt'):
  # Create the filepath of particular file
  file_path = f"{path}/{file}"
  read_files(file_path)


def read_files(file_path):
 with open(file_path, 'r', encoding="utf8") as file:
  # list.append(file.read())
  contents = file.read()

  # Breaking into lines and remove leading and trailing space on each
  lines = (line.strip() for line in contents.splitlines())
  # Breaking multi-headlines into a line each
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
  # Drop blank lines
  text = '\n'.join(chunk for chunk in chunks if chunk)

  # Removing hyper link and regular expressions and stop words
  hyperlink_removed_text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
  te = text.translate(str.maketrans('', '', string.punctuation))
  pattern = r'[0-9]'
  new_string = re.sub(pattern, '', te)
  new_string = new_string.lower()
  # print(new_string)
  bg1 = re.sub('machine learning', ' machinelearning ', new_string)
  bg2 = re.sub('deep learning', ' deeplearning ', bg1)
  bg3 = re.sub('data mining', ' datamining ', bg2)
  final = re.sub("\s\s+", " ", bg3)
  final2 = re.sub("–", "", final)
  final3 = re.sub('[^a-zA-Z0-9 \n\.]', ' ', final2)
  ps = PorterStemmer()
  words_final_list = word_tokenize(filtered_words)
  for w in words:
   wordlist.append(w)
   stemWordList.append(ps.stem(w))
  print("stem", stemWordList)

  words_list = words_final_list.split()
  # print(words_list)
  # print(words)
  filtered_words = [word for word in words_list if word not in stopwords.words('english')]
  # print("fil", filtered_words)

  count = pd.value_counts(np.array(filtered_words))
  words_find = ['research', 'data', 'mining', 'analytics', 'datamining', 'machinelearning', 'deeplearning']
  wordscount = []
  for i in words_find:
   # print(i, "appears", filtered_words.count(i), "times" )
   wordscount.append(filtered_words.count(i))

  # print(wordscount)
  wordsCountAll.append(wordscount.copy())
  # print("Total words count for 6 six files for seven words in an array", wordsCountAll)
