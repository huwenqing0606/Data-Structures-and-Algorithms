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
    
    def __init__(self, context = None, pt_next = None):
        self.context = context
        self.next = pt_next
    
    def show(self):
        print(self.context)
        return None
    
# build a linked list



