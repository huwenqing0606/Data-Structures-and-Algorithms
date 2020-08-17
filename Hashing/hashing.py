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

from random import seed
from random import shuffle



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
        
    # generate a sequence of random numbers for Hashing, integers range from [0, sample_max]
    def generate_sample(self, sample_max):
        if sample_max < self.n:
            sample_max = self.n
        sample = [_ for _ in range(sample_max)]
        shuffle(sample)
        sample = [sample[_] for _ in range(self.n)]
        return sample        





"""
################################ MAIN TESTING FILE #####################################
################################ FOR DEBUGGING ONLY #####################################

testing the Hash map and collision processing
"""

if __name__ == "__main__":
    
    number_sample = 10 # the number of samples that are being Hashed 
    function_mod = 3 # the prime number p for building the Hash function H(key) = key mod p
    table_length = 100 # the length of the Hash table
    incremental_seq = [1, 2, 3, 4, 5] # the d_i sequence for linear probing
                 
    hashing = Hashing(number_sample, function_mod, table_length, incremental_seq)
    sample = hashing.generate_sample(sample_max=20)
    print(sample)
    



