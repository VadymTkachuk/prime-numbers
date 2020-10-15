#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Author: Vadym Tkachuk
# Date: 02.03.2019
# License: MIT
# Purpose: This is a module for testing if a number is a prime.
# 		   The secondary objective is to test speed of python
#		   and of algos of finding primes.  


""" This module contains several definitions of 
	function desiding if a number is a prime 
	i.e it has no divisors except itself.
    Pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""

import math


def is_prime1(x):
    # If number(x) is evenly divided by following dividers then number(x) is not prime
    divider = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    # An empty list to be able to check whether number(x) is evenly divided:
    remainder = []
    # exceptions for numbers 1,2,3,5,7:
    if x < 2:
        return False
    if x in divider:
        return True
    else:
        for nums in divider:
            remainder.append(x % nums)
        if 0 in remainder:
            return False
        else:
            return True

def is_prime2(n):
    if n == 2: return True
    for i in range(3, int(n**0.5)+1, 2): # n**0.5 is a square root
        if n%i==0:
            return False
    return True


def is_prime3(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6		
    return True


# This is probably among the fastest as it both replaces square root
# with square, and leaves out not only the multiplies of 2
# from the loop but the multiplies of 3 as well.
# %timeit isPrime(800)

def is_prime4(n):
    # Corner Cases
    if (n<= 1): return False
    elif (n<= 3): return True
    elif (n%2 == 0 or n%3 == 0): return False

    i = 5
    while i*i<=n:
        if (n%i==0 or n%(i+2)==0): return False
        i += 6

    return True;

def is_prime5(n):
    if n < 2:
        return False;
    if n % 2 == 0:
        return n == 2  # return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# Using lambda definition:
import numpy as np

def is_prime6(n):
    is_prime=lambda x: all(x % i != 0 for i in range(int(x**0.5)+1)[2:])
    # To find all primes you might use:
    # filter(isPrime, range(4000)[2:])[:5]
    return is_prime(n)


def is_prime7(Number):
    return 2 in [Number,2**Number%Number]


def is_prime8(x):
    if x < 2:  
        return False  
    for n in range(2, (x) - 1):  
        if x % n == 0:  
            return False  
    return True


from math import factorial
def is_prime9(x):
    """
    This method will be slower than the the recursive and enumerative methods here,
    but uses Wilson's theorem, and is just a single line.
    """
    return factorial(x - 1)  % x == x - 1


def is_prime10(x):
    if x < 4:
        return True
    if all([(x > 2), (x % 2 == 0)]):
        return False
    else:
        return np.array([*map(lambda y: ((x % y) == 0).sum(), np.arange(1, x + 1))]).sum() == 2


# Method with sieve of Atkin
def atkin(limit):
    if limit > 2:
        yield 2
    if limit > 3:
        yield 3

    import math
    is_prime = [False] * (limit + 1)

    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2

            if n<=limit and (n%12==1 or n%12==5):
                # print "1st if"
                is_prime[n] = not is_prime[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7:
                # print "Second if"
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11:
                # print "third if"
                is_prime[n] = not is_prime[n]

    for n in range(5,int(math.sqrt(limit))):
        if is_prime[n]:
            for k in range(n**2,limit+1,n**2):
                is_prime[k] = False

    for n in range(5,limit):
        if is_prime[n]: yield n

def is_prime11(n):
    r = list(atkin(n+1))
    if not r: return False
    return True if n == r[-1] else False


import re
# Explanation is here: http://montreal.pm.org/tech/neil_kandalgaonkar.shtml
#
#   ^1?$   # matches beginning, optional 1, ending.
#          # thus matches the empty string and "1".
#          # this matches the cases where N was 0 and 1
#          # and since it matches, will not flag those as prime.
# |   # or...
#   ^                # match beginning of string
#     (              # begin first stored group
#      1             # match a one
#       1+?          # then match one or more ones, minimally.
#     )              # end storing first group
#     \1+            # match the first group, repeated one or more times.
#   $                # match end of string.
def is_prime12(n):
    return not re.match(r'^1?$|^(11+?)\1+$',n*'1')


import unittest_primes
import benchmark_primes
import runpy

if __name__ == '__main__':
    file = "./unittest_primes.py"
    exec(compile(open(file).read(), file, 'exec'))
    # The following lines do not run. Do not know why.
    file = "./benchmark_primes.py"
    exec(compile(open(file).read(), file, 'exec'))