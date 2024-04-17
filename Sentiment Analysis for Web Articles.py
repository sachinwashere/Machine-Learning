

!pip install nltk
!pip install textblob
!pip install newspaper3k
from textblob import TextBlob
from newspaper import Article
url = "https://timesofindia.indiatimes.com/topic/murder-in-gurgaon"
article = Article(url)
article.download()
article.parse()
article.nlp

text = article.text
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity #-1 to 1
print(sentiment)