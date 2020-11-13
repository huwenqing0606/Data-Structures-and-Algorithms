#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:36:09 2020

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Sorting Algorithms %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

An implementation of various sorting algoritms

Includes: 
    (1)     Straight-insertion sort
    (2)     Shellsort
    (3)     Bubble sort
    (4)     Quicksort
    (x)     Merge-insertion sort
    (x)     Heapsort
    (x)     Merge sort
    (x)     Introsort
    (x)     Selection sort
    (x)     Odd–even sort
    (xx)    Cocktail shaker sort
    (xx)    Cycle sort
    (xx)    Smoothsort
    (xx)    Timsort
    (xx)    Block sort

@uthor: Wenqing Hu (Missouri S&T)
"""

import numpy as np

class comparison_sort:
    
    def __init__(self,
                 sequence):
        self.seq = sequence
        
    def straight_insertion(self):
        sorted_seq = [self.seq[0]]
        for index in range(1, len(self.seq)):
            element = self.seq[index]
            i=0
            while element >= sorted_seq[i]:
                i= i+1
                if i == len(sorted_seq):
                    break
            sorted_seq.insert(i, element)
        self.seq = sorted_seq
        return None
    
    def shell(self, d):
        m = len(d)
        n = len(self.seq)
        for i in range(m):
            subseq = [self.seq[j * d[i]] for j in range(int(n/d[i]))]
            shellsort = comparison_sort(subseq)
            shellsort.straight_insertion()
            for j in range(int(n/d[i])):
                self.seq[j * d[i]] = shellsort.seq[j]
        return None
    
    def bubble(self):
        n = len(self.seq)
        for i in range(n-1):
            for j in range(n-i-1):
                if self.seq[j] > self.seq[j+1]:
                    x = self.seq[j]
                    self.seq[j] = self.seq[j+1]
                    self.seq[j+1] = x
        return None

    def quick(self):
        sorted_seq = []
        return None





if __name__ == "__main__":
    
    n = 100
    seq = np.arange(n)
    method = "bubble"
    np.random.shuffle(seq)
    print("original sequence=", seq)
    sort = comparison_sort(seq)
    if method == "straight_insertion":
        sort.straight_insertion()
    elif method == "shell":
        sort.shell([5, 3, 1])
    elif method == "bubble":
        sort.bubble()
    elif method == "quick":
        sort.quick()
    else:
        print("No method corresponds!")
    print(method, "sorted sequence=", sort.seq)
    
