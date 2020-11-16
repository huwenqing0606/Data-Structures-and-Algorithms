#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:36:09 2020

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Sorting Algorithms %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

An implementation of various sorting algoritms

Includes: 
    (1)     straight-insertion sort
    (2)     shell sort
    (3)     bubble sort
    (4)     quick sort
    (5)     simple-selection sort
    (x)     Merge-insertion sort
    (x)     Heap sort
    (x)     Merge sort
    (x)     Intro sort
    (x)     Odd–even sort
    (xx)    Cocktail shaker sort
    (xx)    Cycle sort
    (xx)    Smooth sort
    (xx)    Tim sort
    (xx)    Block sort

@author: Wenqing Hu (Missouri S&T)
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

    def quick(self, low, high):
        m = high - low
        if m==0:
            return None
        else:
            pivot = self.seq[low]
            seq_left_pivot = []
            seq_right_pivot = []
            for i in range(1, m):
                if self.seq[low + i] < pivot:
                    seq_left_pivot.append(self.seq[low + i])
                else:
                    seq_right_pivot.append(self.seq[low + i])
            k = len(seq_left_pivot)
            for i in range(k):
                self.seq[low + i] = seq_left_pivot[i]
            self.seq[low + k] = pivot
            for i in range(k+1, m):
                self.seq[low + i] = seq_right_pivot[i-k-1]

            self.quick(low, low+k)
            self.quick(low+k+1, high)
        return None

    def simple_selection(self):
        n = len(self.seq)
        for i in range(n):
            for j in range(i, n):
                if self.seq[j] < self.seq[i]:
                    temp = self.seq[i]
                    self.seq[i] = self.seq[j]
                    self.seq[j] = temp
        return None




if __name__ == "__main__":
    
    n = 100
    seq = np.arange(n)
    method = "simple_selection"
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
        sort.quick(0, n)
    elif method == "simple_selection":
        sort.simple_selection()
    else:
        print("No method corresponds!")
    print(method, "sorted sequence=", sort.seq)
    
