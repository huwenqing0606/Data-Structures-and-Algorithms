#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:51:39 2020

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Hashing %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Insert a randomly generated sequence to a Hash table via a modulus Hash map H(key) = key mod p, p <= m
When collision happens, use linear probing to determine the Hash position
Given a randomly selected sample from the sequence, locate its position after Hashing

@author: Wenqing Hu (Missouri S&T)

"""

import random
from random import seed
from random import shuffle

random.seed(1)

# the class Hashing
class Hashing:
    
    def __init__(self, 
                 number_sample, # the number of samples that are being Hashed 
                 function_mod, # the prime number p for building the Hash function H(key) = key mod p
                 table_length, # the length of the Hash table
                 incremental_seq, # the d_i sequence for linear probing
                 ):
        self.n = number_sample
        self.p = function_mod
        self.m = table_length
        self.d = incremental_seq
        self.table = [None for _ in range(self.m)]
        
        
    # generate a sequence of random numbers for Hashing, integers range from [0, sample_max]
    def generate_sample(self, sample_max):
        if sample_max < self.n:
            sample_max = self.n
        sample = [_ for _ in range(sample_max)]
        shuffle(sample)
        sample = [sample[_] for _ in range(self.n)]
        return sample        

    # find the hash position of a given sample point H(key) = key mod p 
    # when collision happens, use linear probing from incremental_seq to determine the Hash position
    def find_position(self, key):
        H_key = key // self.p
        position = H_key
        counter = 1
        while self.table[position] != None:
            position = position + self.d[counter]
            counter = counter + 1
        return position
    
    # fill all keys in sample using hashing
    def fill_table(self, sample):
        for i in range(self.n):
            key = sample[i]
            position = self.find_position(key)
            self.table[position] = key
        return self.table            
    
    # given a key, search for its position on the Hash table
    def search_table(self, key):
        position = key // self.p
        counter = 1
        while self.table[position] != key:
            position = position + self.d[counter]
        if position >= self.m:
            position = -1
        return position



"""
################################ MAIN TESTING FILE #####################################
################################ FOR DEBUGGING ONLY #####################################

testing the Hash map and collision processing
"""

if __name__ == "__main__":
    
    number_sample = 10 # the number of samples that are being Hashed 
    function_mod = 3 # the prime number p for building the Hash function H(key) = key mod p
    table_length = 30 # the length of the Hash table
    incremental_seq = [_ for _ in range(10)] # the d_i sequence for linear probing
                 
    hashing = Hashing(number_sample, function_mod, table_length, incremental_seq)
    sample = hashing.generate_sample(sample_max=20)
    print("samples are ", sample)
    hashing.fill_table(sample)
    print("hash table is given by ", hashing.table)
    for i in range(number_sample):
        key = sample[i]
        position = hashing.search_table(key)
        print("sample", sample[i], "is at hash table position", position)

