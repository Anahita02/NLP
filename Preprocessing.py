import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
import re
nltk.download('omw-1.4')

text = """In the heart of the city, where neon signs flicker like distant stars, lies an enigmatic garden. It defies the laws of nature, a place where reality waltzes with the impossible. The Quantum Garden, they call it—a sanctuary for dreamers, misfits, and those who seek solace beyond the mundane.

The entrance is unassuming—a wrought-iron gate adorned with ivy. As you step through, the air shimmers, and the world shifts. Time becomes elastic, stretching and contracting like a cosmic accordion. The path ahead forks into infinite possibilities, each leading to a different version of yourself.

The flora here is sentient. Trees whisper secrets in forgotten languages, their leaves rustling with forgotten memories. Flowers bloom in hues unseen by human eyes—quantum petals that pulse with uncertainty. You pluck one, and it becomes both alive and dead, Schrödinger’s bloom.

The sky overhead is a canvas of fractals. Clouds morph into dragons, then into equations, then into forgotten love letters. The sun, a quantum ember, casts shadows that dance between dimensions. If you lie on the grass, you might glimpse parallel worlds—the you who chose a different path, the you who never left that café, the you who kissed the stranger at the crossroads.

In the Quantum Garden, conversations defy linearity. You might chat with a Victorian poet about black holes or debate string theory with a jazz-playing octopus. The benches are occupied by ghosts—scientists, artists, lovers—all sipping tea from Möbius cups. They share theories, swap stories, and laugh at the absurdity of existence.

The fountain at the center is a singularity. Its water spirals upward, defying gravity, carrying wishes and regrets. Throw a coin, and it might land in your own pocket or in the lap of your doppelgänger. The ripples echo across realities, touching lives you’ve never lived.

As twilight settles, the Quantum Garden reveals its true magic. The stars descend, not as distant pinpricks, but as sentient beings. They alight on your shoulders, whispering forgotten constellations. Orion tells tales of lost civilizations; Vega hums forgotten lullabies. And Cassiopeia? She weaves constellations into your hair, making you part of the cosmic tapestry.

But beware—the garden has its rules. Never ask for your future; it’s a Möbius loop that leads nowhere. Never pick the silver roses—they bind you to this place, and eternity can be lonely. And never, ever mention the Uncertainty Bench, where lovers sit, knowing they might kiss or vanish into probability clouds.

As dawn approaches, you’ll find yourself at the exit. The gate creaks shut, and the Quantum Garden fades. But its echoes linger—the scent of quantum jasmine, the taste of parallel raindrops, the warmth of conversations across time.

And so, you step back into the city, where neon signs flicker and people rush past, unaware of the garden they walk beside. But you carry its magic—the uncertainty, the wonder, the knowledge that reality is but one thread in the cosmic weave."""

sentences = nltk.sent_tokenize(text)
sentences

words = nltk.word_tokenize(text)
words

p_stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [p_stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)
    print(sentences[i])

p_lemmatizer = WordNetLemmatizer()

sentencess = nltk.sent_tokenize(text)

for i in range(len(sentencess)):
    words = nltk.word_tokenize(sentencess[i])
    words = [p_stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentencess[i] = ' '.join(words)
    print(sentencess[i])


corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [p_stemmer.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()
x


corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [p_lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
x = tf.fit_transform(corpus).toarray
x