import spacy
nlp = spacy.load('en_core_web_sm')
from spacy import displacy
doc = nlp(u'Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million. '
         u'By contrast, Sony sold only 7 thousand Walkman music players.')

displacy.render(doc,style='ent',jupyter=True)
for sent in doc.sents:
    displacy.render(nlp(sent.text),style='ent',jupyter=True)

colors = {'ORG':'red'}
options = {'ents':['PRODUCT','ORG'],'colors':colors}
displacy.render(doc,style='ent',jupyter=True,options=options)

colors = {'ORG': 'linear-gradient(90deg, #aa9cfc, #fc9ce7)', 'PRODUCT': 'radial-gradient(yellow, green)'}

options = {'ents': ['ORG', 'PRODUCT'], 'colors':colors}

displacy.render(doc, style='ent', jupyter=True, options=options)

displacy.serve(doc,style='ent',options=options)