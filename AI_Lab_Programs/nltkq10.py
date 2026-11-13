import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
for p in ("punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4", "averaged_perceptron_tagger", "averaged_perceptron_tagger_eng"): nltk.download(p, quiet=True)

open("passage.txt", "w").write("Natural Language Processing is a branch of Artificial Intelligence that helps computers understand, interpret and generate human language. It is used in many applications such as chatbots and search engines.")
text = open("passage.txt").read()
sent = "The children were running quickly and studying happily"
stop = set(stopwords.words("english"))
tokens = word_tokenize(sent)
tags = nltk.pos_tag(tokens)

print("(a) Stop word removal")
print(" ".join(w for w in word_tokenize(text) if w.isalnum() and w.lower() not in stop))

print("\n(b) Stemming")
ps = PorterStemmer()
print([ps.stem(w) for w in tokens])

print("\n(c) POS tagging")
print(tags)

print("\n(d) Lemmatization")
wl = WordNetLemmatizer()
m = {"J": wordnet.ADJ, "V": wordnet.VERB, "R": wordnet.ADV}
print([wl.lemmatize(w, m.get(t[0], wordnet.NOUN)) for w, t in tags])