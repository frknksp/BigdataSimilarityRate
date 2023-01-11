import pandas as pd

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def querypanda(queryvalue,sub):
    data  = pd.read_csv('C:/Users/frknk/Desktop/archive/rows.csv',low_memory=False)

    data.columns =[column.replace(" ", "_") for column in data.columns]
    data.query(f'Complaint_ID == {queryvalue}', inplace = True)

    print(data)
    print(data[f'{sub}'].iloc[0])
    issuedf = data[f'{sub}'].iloc[0]

    stop_words = nltk.corpus.stopwords.words('english')
    removestopwords = lambda x: ' '.join([word for word in x.split() if word not in (stop_words)])
    resultissue = removestopwords(issuedf)
    print(resultissue)
    return resultissue

# querypanda(3238275,"Issue")


