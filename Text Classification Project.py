import numpy as np
import pandas as pd

df = pd.read_csv('TextFiles/moviereviews.tsv',sep='\t')

df.head()

len(df)

print(df['review'][0])

print(df['review'][2])

#missing values
df.isnull().sum()

#remove null review
df.dropna(inplace=True) #permanent drop 

df.isnull().sum()

#another method:
blanks = []

#(index,label,review text)
for i,lb,rv in df.itertuples():
    if rv.isspace():
        blanks.append(i)

blanks

df.drop(blanks,inplace=True)

len(df)

from sklearn.model_selection import train_test_split

X = df['review']

y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

text_clf = Pipeline([('tfidf',TfidfVectorizer()),('clf',LinearSVC())])

text_clf.fit(X_train,y_train)

predictions = text_clf.predict(X_test)

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))

print(accuracy_score(y_test,predictions))