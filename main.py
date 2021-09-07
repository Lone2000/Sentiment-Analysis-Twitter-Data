import sys
sys.setExecutionLimit(55000) 

#FUNCTION DEFINITIONS BELOW

#Punctuation Work
def strip_punctuation(wrd):
    for pun in punctuation_chars:
        if pun in wrd:
            wrd = wrd.replace(pun,"")
    return wrd


#Count Positive Words
def get_pos(sentence):
    sentence_lst = strip_punctuation(sentence).split()
    pos_count = 0
    for i in range(len(positive_words)):
        for j in range(len(sentence_lst)):
            if positive_words[i].lower() == sentence_lst[j].lower():
                pos_count += 1
    return +pos_count


#Count Negative Words
def get_neg(sentence):
    sentence_lst = strip_punctuation(sentence).split()
    neg_count = 0
    for i in range(len(negative_words)):
        for j in range(len(sentence_lst)):
            if negative_words[i].lower() == sentence_lst[j].lower():
                neg_count += 1
        
    return -neg_count



punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
data_file = open("project_twitter_data.csv","r")
result_file = open("resulting_data.csv","w")
#Read Header Row
result_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
#Read the whole data_file + Header, to move the Read Header to Information Line
header = data_file.readline()
result_file.write("\n")

for tweet in data_file:
    tweet_data = tweet.strip().split(",")
    create_row_string = "{},{},{},{},{}".format(int(tweet_data[1]),int(tweet_data[2]),get_pos(tweet_data[0]),get_neg(tweet_data[0]),(get_pos(tweet_data[0])+get_neg(tweet_data[0])))
    result_file.write(create_row_string)
    result_file.write("\n")

data_file.close()
result_file.close()    
