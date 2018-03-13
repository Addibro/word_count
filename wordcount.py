import sys
import re
from collections import Counter

# Read a file and count the words

file = open(sys.argv[1])

# Data structure to store the words
word_occurrences = {}

# Get usual words
stopwords = open('ignore').read().split()

# Split punctuations (.,")
text = file.read().lower()
text = re.sub('[^a-z]+'," ", text).split()

# Add words and their occurrances 
for word in text:
    if word not in stopwords and len(word) >= int(sys.argv[2]):
        if word not in word_occurrences:
            word_occurrences[word] = 1
        else:    
            word_occurrences[word] += 1   
# Display
for key, value in Counter(word_occurrences).most_common(10):
    print(key, ":", value)
