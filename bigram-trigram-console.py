import collections

#To download the needed libraries:
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

# coding=utf-8

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def bigrams(base, words):
    
    bigrams = []
    suggestions = []

    for i in range(0, len(base)):
        if (i == len(base)-1):
            break
        else:
            if(base[i].lower()==words[1].lower() and base[i-1].lower()==words[0].lower()):
                bigrams.append(base[i+1])

    counter = collections.Counter(bigrams)
    
    for i in range(0,len(counter.most_common())):
        if(i>=3):
            break
        else:
            suggestions.append(counter.most_common()[i][0])
    
    return suggestions


def trigrams(base, words):

    trigrams = []
    suggestions = []

    for i in range(0, len(base)):
        if (i == len(base)-2):
            break
        else:
            if(base[i].lower()==words[2].lower()
               and base[i-1].lower()==words[1].lower()
               and base[i-2].lower()==words[0].lower()):
                
                trigrams.append(base[i+1])
 
    counter = collections.Counter(trigrams)
    
    for i in range(0,len(counter.most_common())):
        if(i>=3):
            break
        else:
            suggestions.append(counter.most_common()[i][0])
    
    return suggestions


with open('shakespeare.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
txtfiltered = [w for w in word_tokenize(data.replace(',',' ').replace('.',' '))]


print(bigrams(txtfiltered, ['this','is']))

print(trigrams(txtfiltered, ['and','then','the']))

