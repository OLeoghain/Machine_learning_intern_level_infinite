
# coding: utf-8
This is a Naive Bayes implementation of Spam-Ham from enron data set
# In[ ]:


# import nltk
import os
import random
from collections import Counter
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify


# In[27]:


stoplist = stopwords.words('english')

def init_lists(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'rb')
        a_list.append(f.read())
    f.close()
    return a_list
        


# In[58]:


def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(sentence))]


# In[59]:


def get_features(text, setting):
    if setting=='bow':
        return {word: count for word, count in Counter(preprocess(text)).items() if not word in stoplist}
    else:
        return {word: True for word in preprocess(text) if not word in stoplist}


# In[60]:


def train(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    # initialise the training and test sets
    train_set, test_set = features[:train_size], features[train_size:]
    print ('Training set size = ' + str(len(train_set)) + ' emails')
    print ('Test set size = ' + str(len(test_set)) + ' emails')
    # train the classifier
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier


# In[61]:


def evaluate(train_set, test_set, classifier):
    # check how the classifier performs on the training and test sets
    print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)))
    print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)))
    # check which words are most informative for the classifier
    classifier.show_most_informative_features(20)


# In[62]:


# initialise the data
spam = init_lists('Enron/enron1/spam/')
ham = init_lists('Enron/enron1/ham/')
all_emails = [(email, 'spam') for email in spam]
all_emails += [(email, 'ham') for email in ham]
random.shuffle(all_emails)
print ('Corpus size = ' + str(len(all_emails)) + ' emails')


# In[64]:


# extract the features
all_features = [(get_features(email, ''), label) for (email, label) in all_emails]
print('Collected ' + str(len(all_features)) + ' feature sets')


# In[66]:


# train the classifier
train_set, test_set, classifier = train(all_features, 0.8)


# In[67]:


# evaluate its performance
evaluate(train_set, test_set, classifier)


# Amit Lohan @ Level Infinite Winter Internship
