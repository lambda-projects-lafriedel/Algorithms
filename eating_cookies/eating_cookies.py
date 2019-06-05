#!/usr/bin/python

import sys


'''
**UNDERSTAND THE PROBLEM**
Function returns the number of ways (permutations) Cookie Monster can eat n cookies

Calculating permutations usually == recursion
Recursive base case: When amount of cookies to eat equals 0

Edge case: negative numbers (return 0)

For 5 cookies in jar (13 permutations):
1+1+1+1+1
1+1+1+2
1+1+2+1
1+1+3
1+2+1+1
1+2+2
1+3+1
2+1+1+1
2+1+2
2+2+1
2+3
3+1+1
3+2

I want to find all the ways that the numbers 1, 2, and 3 can be added up and equal n, including duplicate (but reversed) uses

0,1,2,3


'''


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    cookies_per_turn = [0,1,2,3]



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')