from textblob import TextBlob
import time

count = 0
neg = 0
pos = 0
ntrl = 0

with open("westworld_qoutes.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)

        if analysis.sentiment.polarity > 0:
            pos += 1

        elif analysis.sentiment.polarity < 0:
            neg += 1
          
        else:
        	ntrl += 1
        
        count +=1

print ("Positive = {}".format(pos) )
print ("Negative = {}".format(neg) )
print ("Neutral  = {}".format(ntrl) )
print ("Out of {} quotes".format(count) )
