from nltk.tokenize import RegexpTokenizer

def count_words(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return len(tokens)

