"""
Q11: Text Classification for a given sentence using NLTK.

A Naive Bayes classifier is trained on a small labelled set of sentences
(positive / negative sentiment). Each sentence is turned into a
"bag of words" feature dictionary, and the trained model then classifies
a new sentence.

NOTE: wordpunct_tokenize is used so that no extra NLTK data is needed
for tokenization; stop words are the only corpus downloaded.
"""

import random

import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

nltk.download("stopwords", quiet=True)
STOP_WORDS = set(stopwords.words("english")) - {"not", "no", "never"}  # keep negations

# ----------------------------------------------------------------------------
# 1. Labelled training data
# ----------------------------------------------------------------------------
TRAIN_DATA = [
    ("I love this movie, it is absolutely wonderful", "positive"),
    ("What a fantastic and amazing experience", "positive"),
    ("The food was delicious and the staff were friendly", "positive"),
    ("I am so happy with this great product", "positive"),
    ("This is the best day of my life", "positive"),
    ("An excellent film with brilliant acting", "positive"),
    ("I really enjoyed the show, it was fun and exciting", "positive"),
    ("The service was outstanding and I will come back", "positive"),
    ("Beautiful design and works perfectly", "positive"),
    ("She is a kind and lovely person", "positive"),
    ("I hate this movie, it is terrible", "negative"),
    ("What a horrible and boring experience", "negative"),
    ("The food was awful and the staff were rude", "negative"),
    ("I am so disappointed with this bad product", "negative"),
    ("This is the worst day of my life", "negative"),
    ("A dreadful film with poor acting", "negative"),
    ("I really disliked the show, it was dull and annoying", "negative"),
    ("The service was slow and I will never come back", "negative"),
    ("Ugly design and it does not work", "negative"),
    ("He is a cruel and nasty person", "negative"),
]


# ----------------------------------------------------------------------------
# 2. Feature extraction
# ----------------------------------------------------------------------------
def preprocess(sentence):
    """Lower-case, tokenize, keep alphabetic non-stop-words."""
    tokens = wordpunct_tokenize(sentence.lower())
    return [t for t in tokens if t.isalpha() and t not in STOP_WORDS]


def extract_features(sentence):
    """Bag-of-words: {'contains(word)': True, ...}"""
    return {f"contains({w})": True for w in preprocess(sentence)}


# ----------------------------------------------------------------------------
# 3. Train / test
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    random.seed(1)
    featuresets = [(extract_features(text), label) for text, label in TRAIN_DATA]
    random.shuffle(featuresets)

    split = int(0.8 * len(featuresets))
    train_set, test_set = featuresets[:split], featuresets[split:]

    classifier = NaiveBayesClassifier.train(train_set)
    print(f"Accuracy on held-out test set: {accuracy(classifier, test_set):.2f}")

    print("\nMost informative features:")
    classifier.show_most_informative_features(8)

    # Retrain on ALL data for the final model used on new sentences.
    classifier = NaiveBayesClassifier.train(featuresets)

    test_sentences = [
        "This is a wonderful and amazing film",
        "The food was terrible and I am disappointed",
        "I love the friendly staff",
        "What a boring and awful show",
    ]
    # test_sentences = [input("Enter a sentence to classify: ")]   # <- user input

    print("\nClassification of new sentences:")
    for sent in test_sentences:
        feats = extract_features(sent)
        label = classifier.classify(feats)
        probs = classifier.prob_classify(feats)
        print(f"  '{sent}'\n     -> {label.upper()} "
              f"(pos={probs.prob('positive'):.2f}, neg={probs.prob('negative'):.2f})")
