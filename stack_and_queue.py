#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:11:35 2020

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Algorithms Related to Stack and Queue %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

An implementation of stack/queue related algoritms

Includes: 
    (1) Build a stack, and construct its basic operations 
    (2) Build a queue, and construct its basic operations

@author: Wenqing Hu (Missouri S&T)

"""

class stack:
    
    def __init__(self,
                 stack_list):
        self.list = stack_list
        
    def push(self, element):
        self.list.insert(0, element)
        
    def pop(self):
        return self.list.pop(0)
    
    def show(self):
        print(self.list)
        return None
    

class queue:
    
    def __init__(self,
                 queue_list):
        self.list = queue_list
        
    def push(self, element):
        self.list.append(element)
        return None
    
    def pop(self):
        return self.list.pop(0)
    
    def show(self):
        print(self.list)
        return None
        
    
    
if __name__ == "__main__":
    
    queue_list = [0, 1, 2, 3, 4]
    queue = queue(queue_list)
    queue.show()
    queue.push(0)
    queue.show()
    queue.pop()
    queue.show()
    
    stack_list = [0, 1, 2, 3, 4]
    stack = stack(stack_list)
    stack.show()
    stack.push(0)
    stack.show()
    stack.pop()
    stack.show()