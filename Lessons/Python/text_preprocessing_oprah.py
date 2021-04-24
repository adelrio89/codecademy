from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech
import re

lemmatizer = WordNetLemmatizer()

oprah_wiki = '<p>Working in local media, she was both the youngest news anchor and the first black female news anchor at Nashville\'s WLAC-TV. </p>'

oprah_wiki_cleaned = re.sub(r'<.?p>|\.','', oprah_wiki).lower()

tokenized_oprah = word_tokenize(oprah_wiki_cleaned)

lemmatized_oprah = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized_oprah]

print("This is the tokenized string:")
print(tokenized_oprah)
print("This is the lemmatized string:")
print(lemmatized_oprah)