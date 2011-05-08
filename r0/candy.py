#!/usr/bin/env python
from __future__ import print_function
from sys import stderr

#find all numbers with colliding bits
def patrick_sum(n1,n2):
    return (n1|n2)^(n1&n2)

if __name__=="__main__":
    n_cases = input()
    for case in xrange(n_cases):
        n_candies = input()
        candies=sorted(map(int,raw_input().split()),reverse=True)
        gaveAway=[]
        while candies:
            gaveAway.append(candies.pop())
            if candies and reduce(patrick_sum,candies) \
                == reduce(patrick_sum,gaveAway):
                break

        result='Case #%s: %s'%(case+1,sum(candies) \
                if candies else 'NO')
        print(result.replace(":","/%s"%n_cases ),file=stderr)
        print(result)
