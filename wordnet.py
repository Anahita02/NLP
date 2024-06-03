from nltk.corpus import wordnet

synonyms = []
antonyms = []

for s in wordnet.synsets('courageous'):
    for l in s.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name)

print("synonyms of courageous = ",set(synonyms))
print("antonyms of courageous = ",set(antonyms))