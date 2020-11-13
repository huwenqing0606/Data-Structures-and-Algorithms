#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:45:43 2020

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Algorithms Related to Graphs %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

An implementation of graph and related algoritms

Includes: 
    (1) Build a Graph 
    (2) Traverse the Graph Using Depth/Broadth First Search

@uthor: Wenqing Hu (Missouri S&T)

"""

import numpy as np

# build a directed graph data structure
# parameters: 
#   n_vtx = number of vertices of the graph, vertices are labeled as 0, 1, 2, ..., n_vtx-1
#   adj_vtx[k] = list of adjacent vertices that are pointed from vertex k where k = 0, 1, 2, ..., n_vtx-1 
# functions:
#   insert_adj(self, vtx, adj_vtx) = insert an adjacent vertex adj_vtx pointed from given vertex vtx
#   build_random(self, prob) = build a random graph on the given vertices, for each vertex, select its adjacent vertices using Bernoulli trials with probability prob
#   undirected_edges(self) = from the given directed graph, build an undirected versionby returning the undirected edges
class directed_graph:
    
    def __init__(self,
                 number_vertices
                 ):
        self.n_vtx = number_vertices
        self.adj_vtx = [[] for _ in range(self.n_vtx)]

    def insert_adj(self, vtx, adj_vtx):
        for adj in adj_vtx:
            self.adj_vtx[vtx].append(adj)
        return None
    
    def build_random(self, prob):
        for vtx in range(self.n_vtx):
            vtx_set = list(range(self.n_vtx))
            vtx_set.remove(vtx)
            adj_vtx = []
            for adj in vtx_set:
                select = np.random.binomial(1, prob, 1)
                if select:
                    adj_vtx.append(adj)
            self.insert_adj(vtx, adj_vtx)
        return None
    
    def undirected_edges(self):
        edges = []
        for vtx in range(self.n_vtx):
            for adj in self.adj_vtx[vtx]:
                edges.append([vtx, adj])
        for edge in edges:
            if edge[0]>edge[1]:
                start=edge[0]
                edge[0]=edge[1]
                edge[1]=start
        edges = np.unique(edges, axis=0)
        return edges
    

# traverse the graph using DFS (Depth-First-Search)
def DFS(graph):
    
    return 0

# traverse the graph using BFS (Broadth-First-Search)
def BFS(graph):
    return 0


if __name__ == "__main__":

    number_vertices = 10
    prob = 0.2
    
    graph = directed_graph(number_vertices=number_vertices)
    graph.build_random(prob)
    
    print(graph.adj_vtx)
    
    edges=graph.undirected_edges()
        
    print(edges)        
        