# preprocessor.py

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_input(user_input):
    words = word_tokenize(user_input)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

def load_dataset(filepath):
    return pd.read_csv(filepath)

def preprocess_dataset(df):
    # Assuming we only need 'name', 'genre', 'director', 'star', and 'country' for recommendation
    # Remove any rows with missing values in these columns
    df = df[['name', 'genre', 'director', 'star', 'country']].dropna()
    return df
