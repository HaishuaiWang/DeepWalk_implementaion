This is a python implementation of DeepWalk by Bryan Perozzi. This is a contribution for Dr. Guozhu Dong's repository which is a collection of Feature Engineering projects for his new textbook called 'Feature Engineering' [currently unplublished]. 

**Dataset** : BlogCatalog 

download here:
[mat file](http://leitang.net/social_dimension.html) or [csv files](http://socialcomputing.asu.edu/datasets/BlogCatalog3)
- Number of users : 10,312
- Number of friendships/edges : 333,983
- Number of groups to which users can subscribe to : 39

**Implementation in progress**

02/21/18 - Graph.py

This contains helper functions to load the dataset, pre processing the graph and generating a corpus of random walks for the graph.

02/21/18 - DeepWalk.ipynb

This notebook computes embeddings for all the nodes in the graph using Word2Vec. 


**References:**

[DeepWalk: Online Learning of Social Representations](http://dl.acm.org/citation.cfm?id=2623732)

[Distributed Representations of Words and Phrases and their Compositionality](arXiv:1310.4546v1)