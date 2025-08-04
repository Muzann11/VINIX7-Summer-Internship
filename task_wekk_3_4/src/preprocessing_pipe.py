import pandas as pd
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))

# Preprocessing functions
def to_lowercase(text):
    return text.lower()

def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def remove_urls(text):
    return re.sub(r'http\S+|www\.\S+', '', text)

def remove_html_tags(text):
    return re.sub(r'<.*?>', '', text)

def remove_emails(text):
    return re.sub(r'\S+@\S+', '', text)

def remove_numbers(text):
    return re.sub(r'\d+', '', text)

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text):
    words = word_tokenize(text)
    filtered = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered)

# Master preprocessing pipeline
def preprocess_description(df, column_name):
    df_desc = df[column_name].dropna().drop_duplicates()
    
    df_desc = (
        df_desc.apply(to_lowercase)
               .apply(remove_urls)
               .apply(remove_html_tags)
               .apply(remove_emails)
               .apply(remove_numbers)
               .apply(remove_punctuation)
               .apply(normalize_whitespace)
               .apply(remove_stopwords)
    )
    
    return " ".join(df_desc.astype(str).tolist())

# Load and preprocess
df = pd.read_csv('data/postings.csv')
text = preprocess_description(df, 'description')

# print(text[:500])  # Print first 500 characters of the cleaned text

