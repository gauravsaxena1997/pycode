from textblob import TextBlob
import time
'''
analyze = TextBlob ("These Violent Delights Have Violent Ends")
print (dir(analyze))
print ( analyze.translate(to='es') )
print ( analyze.detect_language() )
print (analyze.tags)
print (analyze.sentiment)
'''

pos_count = 0
pos_correct = 0

with open("positive.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)

        if analysis.sentiment.polarity >= 0.0001:
            if analysis.sentiment.polarity > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open("negative.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity <= -0.0001:
            if analysis.sentiment.polarity < 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

# Check polarity
'''
pos_correct = 0
pos_count = 0
nutrl_in_pos = 0
with open('positive.txt','r') as f:
	for line in f.read().split('\n'):
		# print (line)
		analyze = TextBlob (line)
		if analyze.sentiment.polarity > 0:
			pos_correct +=1
		elif analyze.sentiment.polarity == 0:
			nutrl_in_pos +=1
		pos_count +=1

neg_correct = 0
neg_count = 0
nutrl_in_neg = 0
with open('negative.txt','r') as f:
	for line in f.read().split('\n'):
		# print (line)
		analyze = TextBlob (line)
		if analyze.sentiment.polarity <= 0:
			neg_correct +=1
		elif analyze.sentiment.polarity == 0:
			nutrl_in_neg +=1
		neg_count +=1

print ("Positive accuracy: {}% and Neutral:{}, via {} samples".format((pos_correct/pos_count)*100 ,nutrl_in_pos ,pos_count))
print ("Negative accuracy: {}% and Neutral:{}, via {} samples".format((neg_correct/neg_count)*100 ,nutrl_in_neg ,neg_count))
'''