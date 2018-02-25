This is a python implementation of DeepWalk by Bryan Perozzi. This is a contribution for Dr. Guozhu Dong's repository which is a collection of Feature Engineering projects for his new textbook called 'Feature Engineering' [currently unplublished]. 

**Dataset** : BlogCatalog 

download here:
[mat file](http://leitang.net/social_dimension.html) or [csv files](http://socialcomputing.asu.edu/datasets/BlogCatalog3)
- Number of users : 10,312
- Number of friendships/edges : 333,983
- Number of groups to which users can subscribe to : 39

**Implementation in progress**

02/21/18 - Graph.py

This contains helper functions to load the dataset, pre-processing the graph and generating a corpus of random walks for the graph.

02/21/18 - DeepWalk.ipynb

This notebook computes embeddings for all the nodes in the graph using Word2Vec. 

02/22/18 - Classifier.py

This contains helper functions to score the word embeddings. It loads the saved word2vec embeddings and performs classification. Classifiers can be added as needed. Make sure they support Multiclass classification. Micro and Macro F1 scores are computed for perfomance comparison. 

02/24/18 - Bug fixes and optimizations

Added timers for each stage. Reporting parameters for each stage. Optimized code for generating walks. Distributed word2vec training to multiple cores. Added 'F1 score vs Training size' graph for each classifier.  

**Results will be tabulated along with conclusions soon**
 

**References:**

[DeepWalk: Online Learning of Social Representations](http://dl.acm.org/citation.cfm?id=2623732)

[Distributed Representations of Words and Phrases and their Compositionality](http://papers.nips.cc/paper/5021-distributed-representations-of-words-andphrases)