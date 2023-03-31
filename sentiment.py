from textblob import TextBlob

with open('myText.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity 

if sentiment <= 1 and sentiment >= .75:
    print("very positive: " + str(sentiment))
elif sentiment < .75 and sentiment >= .5:
    print("positive: " + str(sentiment))
elif sentiment < .5 and sentiment >= .1:
    print("slightly positive: " + str(sentiment))
elif sentiment < .1 and sentiment >= -.1:
    print("neutral: " + str(sentiment))
elif sentiment < -.1 and sentiment >= -.5:
    print("slightly negative: " + str(sentiment))
elif sentiment < -.5 and sentiment >= -.75:
    print("negative: " + str(sentiment))
else:
    print("very negative: " + str(sentiment))
