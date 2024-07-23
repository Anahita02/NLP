#part1
import spacy
nlp = spacy.load('en_core_web_sm')
mystring = '"We\'re moving to L.A.!"'
print(mystring)

doc = nlp(mystring)

for token in doc:
    print(token.text)

doc2 = nlp(u"We're here to help! Send snail-mail, email support@oursite.com or visit us at http://www.oursite.com!")

for t in doc2:
    print(t)

doc3 = nlp(u'A 5km NYC cab ride costs $10.30')

for t in doc3:
    print(t)

#Punctuation that exists as part of a known abbreviation will be kept as part of the token.
doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")

for t in doc4:
    print(t)

#count the number of tokens
len(doc4)

#Counting Vocab Entries
len(doc4.vocab)

doc5 = nlp(u'It is better to give than to receive.')

doc5[0]

doc5[2:5]

#docs can't be reassignment
doc5[0] = 'test'

doc8 = nlp(u'Apple to build a Hong Kong factory for $6 million')

for token in doc8:
    print(token.text, end=" | ")

for entity in doc8.ents:
    print(entity)

for entity in doc8.ents:
    print(entity)
    print(entity.label_)
    print('\n')

for entity in doc8.ents:
    print(entity)
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print('\n') 

# Noun Chunks
doc9 = nlp(u"Autonomous cars shift insurance liability toward manufacturers.")

for chunk in doc9.noun_chunks:
    print(chunk)

#part2 = tokenization visualized
# display the dependency graphic dep =syntax dependency
from spacy import displacy

doc = nlp(u'Apple is going to build a U.K. factory for $6 million.')

displacy.render(doc,style='dep',jupyter=True,options={'distance':110}) # distance is optional and it is the distancde between the tokens.

#Visualizing the entity recognizer
doc = nlp(u'Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million.')

displacy.render(doc,style='ent',jupyter=True)

# Creating Visualizations Outside of Jupyter
# doc = nlp(u'This is a sentence.')
# displacy.serve(doc, style='dep')
# #in google search 127.0.0.1:5000