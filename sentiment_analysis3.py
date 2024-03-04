import nltk
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords #imported inbuilt stopwords from NLTK library
from scraper import sapiens
text=sapiens
lowercase=text.lower()
clean_text=lowercase.translate(str.maketrans('','',string.punctuation))
tokenized_word=nltk.word_tokenize(clean_text,"english")


final_word=[]
emotn_lst=[]

for word in tokenized_word:
    if word not in stopwords.words("english"):
        final_word.append(word)

with open("emotion.txt","r") as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_word:
            emotn_lst.append(emotion)
print(emotn_lst)
w=Counter(emotn_lst)
print(w)
def sentiment_analyze(s_text):
    score=SentimentIntensityAnalyzer().polarity_scores(s_text)
    neg=score["neg"]
    pos=score["pos"]
    if neg>pos:
        print("Negetive Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Neutral sentiment")
        
sentiment_analyze(clean_text)

#plot graph
fig,ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.show()


