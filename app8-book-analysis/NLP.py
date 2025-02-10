import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# run this when setting up a new env
# nltk.download('stopwords')
# nltk.download('vader_lexicon')


# Reading the data
with open("miracle_in_the_andes.txt", "r", encoding='utf-8') as file:
    book = file.read()

# Regex matching to get all words
pattern = re.compile("[a-z]+")
findings = re.findall(pattern, book.lower())

# Counting words
d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

# Restructure to list, and sort by count desc
d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)

# Removing stop words
english_stopwords = stopwords.words("english")
filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append({word, count})
#print(filtered_words)

# Analyze the mood of text
analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(book)
# print(scores) {'neg': 0.116, 'neu': 0.76, 'pos': 0.125, 'compound': 1.0}

chapter_pattern = re.compile("Chapter [0-9]+")
chapters = re.split(chapter_pattern, book)
chapters = chapters[1:]

for chapter in chapters:
    scores = analyzer.polarity_scores(chapter)
    print(scores)