
# coding: utf-8

# In[12]:

import numpy as np
import Graph
from gensim.models import KeyedVectors
from sklearn.utils import shuffle as skshuffle
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score

# In[8]:

def sparse2array_inv_binarize(y):
    mlb = MultiLabelBinarizer(range(y.shape[1]))
    mlb.fit(y)
    y_ = mlb.inverse_transform(y.toarray())
    return y_


# In[7]:

#predict() doesn't do a good job of predicting multiple classes per input. Better get the predicted probabilities
#and fetch predictions manually
def custom_predict(classifier, X_test, y_test):
    
    y_test_ = sparse2array_inv_binarize(y_test)
    num_predictions = [len(item) for item in y_test_]
    
    probabilities = classifier.predict_proba(X_test)
    sorted_indices_probs = probabilities.argsort()
    
    preds = [sorted_indices[-num:].tolist() for (sorted_indices,num) in zip(sorted_indices_probs,num_predictions)]
    
    return preds


# In[43]:

def compute_metrics(y_test, preds):
    
    mlb = MultiLabelBinarizer(range(y_test.shape[1]))
    mlb.fit(preds)
    preds = mlb.transform(preds)
    #convert y_test from sparse back and forth to get binarized version.
    #There's probably a better way to do this
    y_test = sparse2array_inv_binarize(y_test)
    y_test = mlb.transform(y_test)
    
    microF1 = f1_score(y_test, preds, average='micro')
    macroF1 = f1_score(y_test, preds, average='macro')
    
    return microF1, macroF1


# In[59]:

def evaluate(G, subs_coo):
    
    #Add classifiers here
    #classifiers = {'Logistic_classifier': OneVsRestClassifier(LogisticRegression(class_weight='balanced')),
    #              'MLP_classifier': MLPClassifier(max_iter=500)}
    classifiers = {'Logistic_classifier': OneVsRestClassifier(LogisticRegression(class_weight='balanced'))}
    
    
    word_vec = KeyedVectors.load_word2vec_format('word2vec.txt', binary=False)
    features_matrix = np.asarray([word_vec[str(node)] for node in range(len(G.nodes()))])
    training_set_size = [0.2, 0.5, 0.8, 0.9]
    all_results = {}
    
    for (name,model) in classifiers.items():
        results = []
        for training_size in training_set_size:
        
            X_train, X_test, y_train, y_test = train_test_split(features_matrix, subs_coo, train_size=training_size, random_state=42)
            model.fit(X_train,y_train)

            preds = custom_predict(model, X_test, y_test)
            microF1,macroF1 = compute_metrics(y_test, preds)
            
            results.append((microF1,macroF1))
        
        all_results[name] = results
    
    return all_results


# In[ ]:



