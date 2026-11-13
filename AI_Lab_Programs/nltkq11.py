from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import wordpunct_tokenize

train = [("I love this movie", "positive"), ("What a wonderful and amazing day", "positive"),
         ("The food was delicious and great", "positive"), ("I am happy with this excellent product", "positive"),
         ("She is a kind and lovely person", "positive"), ("Great acting and a brilliant story", "positive"),
         ("I hate this movie", "negative"), ("What a horrible and boring day", "negative"),
         ("The food was awful and bad", "negative"), ("I am unhappy with this terrible product", "negative"),
         ("He is a cruel and nasty person", "negative"), ("Poor acting and a dull story", "negative")]

feat = lambda s: {w: True for w in wordpunct_tokenize(s.lower())}
clf = NaiveBayesClassifier.train([(feat(s), l) for s, l in train])

for s in ["I love this wonderful movie", "The food was awful and I hate it", "She is a brilliant and kind person"]:
    print(s, "->", clf.classify(feat(s)))