# Sentiment Analysis Project
# Load the Data
import numpy as np
import pandas as pd

df = pd.read_csv('TextFiles/moviereviews.tsv',sep='\t')

df.head()

df.dropna(inplace=True)

#remove single strings
blanks = []

for i,la,rv in df.itertuples():
    if type(rv) == str:
        if rv.isspace():
            blanks.append(i)

blanks

df.drop(blanks,inplace=True)

df['label'].value_counts()

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

df['scores'] = df['review'].apply(lambda review:sid.polarity_scores(review))

df['compound'] = df['scores'].apply(lambda d:d['compound'])

df.head()

df['compound_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')

df.head()

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

accuracy_score(df['label'],df['compound_score'])

print(classification_report(df['label'],df['compound_score']))

print(confusion_matrix(df['label'],df['compound_score']))