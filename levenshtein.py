#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
levenshtein.py
'''

def levenshtein_distance(s1, s2):

    matrix = [[0]*(len(s2)+1) for i in xrange(len(s1)+1)]

    for i in xrange(len(s1)+1):
        matrix[i][0] = i

    for j in xrange(len(s2)+1):
        matrix[0][j] = j

    for i in xrange(1, len(s1)+1):
        for j in xrange(1, len(s2)+1):
            
            if s1[i-1] == s2[j-1]:
                delta = 0 # just move cursor
            else:
                delta = 1 # deletion, insertion, substitution (permutation)

            # fill in the cell
            matrix[i][j] = min(matrix[i-1][j]+1 , matrix[i][j-1]+1, matrix[i-1][j-1]+delta)

    return matrix[-1][-1]


import sys
import time
if __name__=="__main__":

    s1 = sys.argv[1]
    s2 = sys.argv[2]

    start = time.time()
    print levenshtein_distance(s1, s2)
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time))
