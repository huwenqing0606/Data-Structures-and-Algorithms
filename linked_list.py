#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:56:41 2020


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Algorithms Related to Linked Lists %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

An implementation of linked list and related algoritms

Includes: 
    (1) Build a linked list

@author: Wenqing Hu (Missouri S&T)

"""

# build a node in a linked list
class Node:
    
    def __init__(self,
                 node_id,
                 node_context,
                 next_node
                 ):
        self.id = node_id
        self.context = node_context
        self.next = next_node
    
    def show(self):
        print(self.context)
        return None
    
# build a linked list
class linked_list:
    
    def __init__(self, 
                 number_nodes, 
                 node_contexts,
                 next_nodes
                 ):
        self.nodes = [Node(i, node_contexts[i], next_nodes[i]) for i in range(number_nodes)]
        
    def next_node_context(self, node_id):
        return self.nodes[self.nodes[node_id].next].context


if __name__=="__main__":
    
    linked_list = linked_list(3, ['a', 'b', 'c'], [1, 2, 0])
    print(linked_list.next_node_context(0))

