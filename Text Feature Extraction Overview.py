#part1
# Building a Natural Language Processor From Scratch
%%writefile 1.txt
This is a story about cats
our feline pets
Cats are furry animals

%%writefile 2.txt
This story is about surfing
Catching waves is fun
Surfing is a popular water sport

# Build a vocabulary
vocab = {}
i = 1

with open('1.txt') as f:
    x = f.read().lower().split()

for word in x:
    if word in vocab:
        continue
    else:
        vocab[word]=i
        i+=1

print(vocab)

with open('2.txt') as f:
    x = f.read().lower().split()

for word in x:
    if word in vocab:
        continue
    else:
        vocab[word]=i
        i+=1

print(vocab)

# Feature Extraction
# Create an empty vector with space for each word in the vocabulary:
one = ['1.txt']+[0]*len(vocab)
one

# map the frequencies of each word in 1.txt to our vector:
with open('1.txt') as f:
    x = f.read().lower().split()
    
for word in x:
    one[vocab[word]]+=1
    
one

# Do the same for the second document:
two = ['2.txt']+[0]*len(vocab)

with open('2.txt') as f:
    x = f.read().lower().split()
    
for word in x:
    two[vocab[word]]+=1
    
two

# Compare the two vectors:
print(f'{one}\n{two}')

# Feature Extraction from Text
import numpy as np
import pandas as pd

df = pd.read_csv('TextFiles/smsspamcollection.tsv', sep='\t')

df.head()

# Check for missing values
df.isnull().sum()

df['label'].value_counts()

from sklearn.model_selection import train_test_split

X = df['message']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Scikit-learn's CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()

X

# Text preprocessing, tokenizing and the ability to filter out stopwords are all included in [CountVectorizer]
#fit vectorizer to the data (build a vocab, count the number of words)
# count_vect.fit(X_train)
# X_train_count = count_vect.transform(X_train)
# another way to avoid the two line above we can do it in one line
#transfor the ogriginal text message ----> vector
X_train_count = count_vect.fit_transform(X_train)

X_train_count
X_train.shape
X_train_count.shape


#part2
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_count)
X_train_tfidf.shape
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train a Classifier
from sklearn.svm import LinearSVC

clf = LinearSVC()
clf.fit(X_train_tfidf,y_train)

# Build a Pipeline
from sklearn.pipeline import Pipeline

text_clf = Pipeline([('tfidf',TfidfVectorizer()),('clf',LinearSVC())])

text_clf.fit(X_train,y_train)
predictions = text_clf.predict(X_test)
X_test

from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

from sklearn import metrics
metrics.accuracy_score(y_test,predictions)
text_clf.predict(["Hi how are you doing today?"])
text_clf.predict(["Congragulations! You've benn selected as a winner. TEXT WON to 44255 congratulations free entry to contest."])