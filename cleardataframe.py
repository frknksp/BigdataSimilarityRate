import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np

def cleardf():
    df = pd.read_csv('C:/Users/frknk/Desktop/archive/rows.csv',low_memory=False)
    column_df = df[['Product', 'Issue', 'Company', 'State', 'Complaint ID', 'ZIP code']]
    clear_df = column_df.dropna()

    # remove punct
    def remove_punctuation(x):
        try:
            # x = x.translate(str.maketrans('', '', string.punctuation))
            x = x.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).replace(' '*4, ' ').replace(' '*3, ' ').replace(' '*2, ' ').strip()
        except:
            pass
        return x

    for col in clear_df.columns:
        print(col)
        clear_df[col] = clear_df[col].apply(remove_punctuation)

    # remove stop words 3 column
    stop_words = nltk.corpus.stopwords.words('english')

    for col in clear_df.columns[:3]:
        print(col)
        clear_df[col] = clear_df[col].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

    clear_df.to_csv('cleardf.csv', index=False)


