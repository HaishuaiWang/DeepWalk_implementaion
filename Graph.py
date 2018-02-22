
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy.io


# In[87]:

#network = pd.read_csv('Flickr-dataset/data/edges.csv',header=None)
#groups = pd.read_csv('Flickr-dataset/data/group-edges.csv',header=None)
#g = nx.read_edgelist('edges.csv',delimiter=',',create_using=nx.Graph(),nodetype=int)
#path = 'blogcatalog.mat'


# In[13]:

def parse_mat_file(path):
    
    edges = []
    subscriptions = []
    g = nx.Graph()
    mat = scipy.io.loadmat(path)
    nodes = mat['network'].tolil()
    subs = mat['group'].tolil()
    
    for start_node,end_nodes in enumerate(nodes.rows, start=0):
        for end_node in end_nodes:
            edges.append((start_node,end_node))
    
    g.add_edges_from(edges)
    
    for i,subs_row in enumerate(subs.rows, start=0):
        subscriptions.append((i,[sub for sub in subs_row]))
        
    return g, subscriptions


# In[89]:

def random_walk(G, start_node, path_len):
    path = [str(start_node)]
    current = start_node
    
    while(len(path) < path_len):
        if(len(G.neighbors(current)) == 0):
            break
        
        current = random.choice(G.neighbors(current))
        path.append(str(current))
        
        #restarts allowed. Even if it randomly picks its previous neighbour in the path.
    return path


# In[90]:

def remove_self_loops(G):
    
    loops = []
    
    #Get loops
    for i,j in G.edges_iter():
        if i==j:
            loops.append((i,j))
    
    G.remove_edges_from(loops)
    return G


# In[1]:

def build_walk_corpus(G, max_paths, path_len):
    
    corpus = []
    
    for start_node in G.nodes_iter():
        for path_count in range(max_paths):
            walk = random_walk(G, start_node, path_len)
            corpus.append(walk)
    
    return corpus

