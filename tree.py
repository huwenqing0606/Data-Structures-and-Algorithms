#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:30:43 2020

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Algorithms Related to Tree %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

An implementation of the binary tree and related algoritms

Includes:
    (1) Binary Tree
    (2) Search on the Binary Tree

@author: Wenqing Hu (Missouri S&T)

"""

class BinaryTree:
    
    def __init__(self,
                 root):
        self.root = root
        self.left_subtree = None
        self.right_subtree = None
        
    def insert_left(self, content):
        if self.left_subtree == None:
            self.left_subtree = BinaryTree(content)
        else:
            new_tree = BinaryTree(content)
            new_tree.left_subtree = self.left_subtree
            self.left_subtree = new_tree

    def insert_right(self, content):
        if self.right_subtree == None:
            self.right_subtree = BinaryTree(content)
        else:
            new_tree = BinaryTree(content)
            new_tree.right_subtree = self.right_subtree
            self.right_subtree = new_tree
    
    def build(self, tree, height):
        if height == 0:
            return None
        else:
            tree.insert_left("L")
            self.build(tree.left_subtree, height-1)            
            tree.insert_right("R")
            self.build(tree.right_subtree, height-1)       
            
    def traverse_root_first(self, tree):
        if tree == None:
            return None
        else:
            print(tree.root)
            self.traverse_root_first(tree.left_subtree)
            self.traverse_root_first(tree.right_subtree)

    def traverse_root_middle(self, tree):
        if tree == None:
            return None
        else:
            self.traverse_root_first(tree.left_subtree)
            print(tree.root)
            self.traverse_root_first(tree.right_subtree)

    def traverse_root_last(self, tree):
        if tree == None:
            return None
        else:
            self.traverse_root_first(tree.left_subtree)
            self.traverse_root_first(tree.right_subtree)
            print(tree.root)
        
    

if __name__ == "__main__":
    
    tree = BinaryTree("root")
    tree.build(tree, 3)
    traverse_method = "root_first"
    if traverse_method == "root_first":
        tree.traverse_root_first(tree)
    elif traverse_method == "root_middle":
        tree.traverse_root_middle(tree)
    elif traverse_method == "root_last":
        tree.traverse_root_last(tree)
    else:
        print("Traverse Method Error!")
    


