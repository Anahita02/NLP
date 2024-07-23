import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")
from spacy import displacy
displacy.render(doc,style='dep',jupyter=True)
options = {'distance':110,'compact':'True','color':'yellow','bg':'red','font':'Times'}
displacy.render(doc,style='dep',jupyter=True,options=options)

#Handling Large Text
doc2 = nlp(u"This is a sentence. This is another sentence, possibly longer than the other.")
spans = list(doc2.sents)
displacy.serve(spans,style='dep',options={'distance':110})

# 127.0.0.1:5000