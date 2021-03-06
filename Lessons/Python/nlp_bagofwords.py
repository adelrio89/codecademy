# importing regex and nltk
import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# importing Counter to get word counts for bag of words
from collections import Counter
# importing a passage from Through the Looking Glass
from looking_glass import looking_glass_text
# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech

# Change text to another string:
#text = looking_glass_text
text = """MANY YEARS LATER as he faced the firing squad. Colonel Aureliano Buendfa was to remember that 
distant afternoon when his father took him to discover ice. At that time Macondo was a village of 
twenty adobe houses, built on the bank of a river of clear water that ran along a bed of polished 
stones, which were white and enormous, like prehistoric eggs. The world was so recent that many 
things lacked names, and in order to indicate them it was necessary to point. Every year during the 
month of March a family of ragged gypsies would set up their tents near the village, and with a great 
uproar of pipes and kettledrums they would display new inventions. First they brought the magnet. 
A heavy gypsy with an untamed beard and sparrow hands, who introduced himself as Melquiades, 
put on a bold public demonstration of what he himself called the eighth wonder of the learned al¬ 
chemists of Macedonia. He went from house to house dragging two metal ingots and everybody was 
amazed to see pots, pans, tongs, and braziers tumble down from their places and beams creak from 
the desperation of nails and screws trying to emerge, and even objects that had been lost for a long 
time appeared from where they had been searched for most and went dragging along in turbulent 
confusion behind Melquiades’ magical irons. “Things have a life of their own,” the gypsy proclaimed 
with a harsh accent. “It’s simply a matter of waking up their souls.” Jose Arcadio Buendia, whose 
unbridled imagination always went beyond the genius of nature and even beyond miracles and 
magic, thought that it would be possible to make use of that useless invention to extract gold from 
the bowels of the earth. Melquiades, who was an honest man, warned him: “It won’t work for 
that.” But Jose Arcadio Buendia at that time did not believe in the honesty of gypsies, so he traded 
Iris mule and a pair of goats for the two magnetized ingots. Ursula Iguaran, his wife, who relied on 
those animals to increase their poor domestic holdings, was unable to dissuade him. “Very soon well 
have gold enough and more to pave the floors of the house,” her husband replied. For several 
months he worked hard to demonstrate the truth of his idea. He explored every inch of the region, 
even the riverbed, dragging the two iron ingots along and reciting Melquiades’ incantation aloud. 
The only thing he succeeded in doing was to unearth a suit of fifteenth-century armor which had all 
of its pieces soldered together with rust and inside of which there was the hollow resonance of an 
enormous stone-filled gourd. When Jose Arcadio Buendia and the four men of his expedition 
managed to take the armor apart, they found inside a calcified skeleton with a copper locket 
containing a woman’s hair around its neck. 
"""

cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)

stop_words = stopwords.words('english')
filtered = [word for word in tokenized if word not in stop_words]

normalizer = WordNetLemmatizer()
normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]
# Comment out the print statement below
print(normalized)

# Define bag_of_looking_glass_words & print:
bag_of_looking_glass_words = Counter(normalized)
print(bag_of_looking_glass_words)
