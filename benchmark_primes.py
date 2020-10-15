#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Author: Vadym Tkachuk
# Date: 02.03.2019
# License: MIT
# Purpose: This is a module for speed testing prime's module functions.
 

import timeit
import primes


def run_test():
    SETUP_CODE = '''
import primes	
import random
import numpy as np
# n = random.randint(10000000, 100000000)'''

# Making names of is_prime#() functions and testing them.
# a_prime = 99999989 is a prime number close to 100 000 000. It takes too long in some cases
# 99991
    a_prime = 30011 #9973 # With less a_prime numbers speed results may differ from function number!
    print("Testing 12 functions with " + str(a_prime) + ".")
    for n in range (1, 13):
        TEST_CODE = "primes.is_prime" + str(n) + "(" + str(a_prime) + ")" # Making funcs names.
        times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10)
        print('Is_primes' + str(n) + '() minimum time is: {}'.format(min(times)))


def benchmark_matrix():

    def fill_matrix():
        a_prime = 17
        dimension_const = 100
        arr = [[[0 for _ in range(dimension_const)] for _ in range(dimension_const)] for _ in range(dimension_const)]
        for i in range(1,dimension_const):
            for j in range(1, dimension_const):
                for k in range(1, dimension_const):
                    arr[i][j][k] = primes.is_prime1(a_prime)

    SETUP_CODE = ''''''
    TEST_CODE = fill_matrix
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=10)
    print('\nFill_matrix minimum time is: {}'.format(min(times)))


if __name__ == '__main__':
    run_test()
    benchmark_matrix()