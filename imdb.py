import pandas as pd

data = pd.read_csv(r"IMDB Dataset.csv")
print(data.head())

from textblob import TextBlob
text = data.loc[2,"review"]

blob = TextBlob(text)
print("Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)

if blob.sentiment.polarity > 0:
 print("Sentiment: Positive ")
elif blob.sentiment.polarity < 0:
 print("Sentiment: Negative")
else:
 print("Sentiment: Neutral ")

