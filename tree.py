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
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, content):
        if self.left_child == None:
            self.left_child = BinaryTree(content)
        else:
            new_node = BinaryTree(content)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, content):
        if self.right_child == None:
            self.right_child = BinaryTree(content)
        else:
            new_node = BinaryTree(content)
            new_node.right_child = self.right_child
            self.right_child = new_node
    
    def build(self, tree, height):
        if height == 0:
            return None
        else:
            tree.insert_left("L")
            self.build(tree.left_child, height-1)            
            tree.insert_right("R")
            self.build(tree.right_child, height-1)       
            
    def traverse_root_first(self, tree):
        if tree == None:
            return None
        else:
            print(tree.root)
            self.traverse_root_first(tree.left_child)
            self.traverse_root_first(tree.right_child)

    def traverse_root_middle(self, tree):
        if tree == None:
            return None
        else:
            self.traverse_root_first(tree.left_child)
            print(tree.root)
            self.traverse_root_first(tree.right_child)

    def traverse_root_last(self, tree):
        if tree == None:
            return None
        else:
            self.traverse_root_first(tree.left_child)
            self.traverse_root_first(tree.right_child)
            print(tree.root)
        
    

if __name__ == "__main__":
    
    tree = BinaryTree("root")
    tree.build(tree, 3)
    traverse_method = "root_last"
    if traverse_method == "root_first":
        tree.traverse_root_first(tree)
    elif traverse_method == "root_middle":
        tree.traverse_root_middle(tree)
    elif traverse_method == "root_last":
        tree.traverse_root_last(tree)
    else:
        print("Traverse Method Error!")
    


