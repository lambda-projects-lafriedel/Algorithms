#!/usr/bin/python

import sys

'''
**UNDERSTAND THE PROBLEM
Return a list of inner lists, where each inner list has a possible order of plays of rock/paper/scissors for n turns. So if n = 2, ['rock', 'paper'] etc and if n = 3, ['rock', 'paper', 'rock'] etc. Length of inner list == n

Instantiate a list cache the length of n

Instantiate a list = ['rock', 'paper', 'scissors']

For each index in rps list

return [list + list] ?

n = 3:
 0 1 2
[r r r] 0
[r r p] 
[r r s] 
[r p r] 3
[r p p] 
[r p s] 
[r s r] 
[r s p] 
[r s s]
[p r r] 
[p r p] 
[p r s] 
[p p r] 
[p p p] 
[p p s] 
[p s r] 
[p s p] 
[p s s]
[s r r] 
[s r p] 
[s r s] 
[s p r] 
[s p p] 
[s p s] 
[s s r] 
[s s p] 
[s s s]

'''

def rock_paper_scissors(n):














    # List of n elements, instantiated with empty strings
    final_list = ([[""] * n] * 3) * 3 * 3
    plays_list = ['rock', 'paper', 'scissors']

    def rps_inner(n, list):
        nonlocal plays_list
        no

      # I need the index of the 
        while n > 0:
            for i in len(plays_list):
            final_list[n][n-1] = plays_list[i]
            rps_inner(n-1, final_list)

      return plays_list[n]

    return rps_inner(n, final_list)


        

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')