#!/usr/bin/python

import argparse

'''
**UNDERSTAND THE PROBLEM**

Return maximum profit that can be made from a single buy and sell. 
Must buy first before selling.
Both buying and selling are required.

Edge cases:
Must check that all list items are numbers
If 1 or 0 items in list, return 0
If two numbers in list...would I have to do anything differently than what the main case would be?

**MAKE A PLAN**

In order to compute a max profit, the number being subtracted from the sale number will always be to the LEFT of the sale price, in other words, at a lower index.

We are NOT looking for the highest number in the list - a higher profit can be made with a lower sale price, depending on the order of stock prices.

Hint provided suggests keeping track of "current min price so far" and "max profit so far." After a calculation is run, the value should be compared to the current value of the stored variable it relates to, and update if it makes sense to do so.

Could use index() to compare index values, but this potentially falls short if the same price shows up in two different locations in the list.

Store index 1 in a variable.
Loop through all indicies before it and subtract 0 from 1, store in max_price_so_far.
Increase index by 1 (to 2)
Loop through again, subtracting 2 from 0, 1
If new result is greater than the stored result, update max_price_so_far
Keep going, and once the loop is complete, return max_price_so_far
'''

def find_max_profit(prices):
    # Edge case: Price list length of 0 or 1 returns a profit of 0.
    if len(prices) < 2: # constant
        return 0 # constant

    max_profit = 0 # constant
    current_index = 1 # constant

    for p in range(len(prices)-1): # O(n)
        price = prices[p+1] # constant
        for i in range(0, current_index): # O(n)
            profit = price - prices[i]

            if profit < 0 and max_profit == 0:
                max_profit = profit
            elif profit > max_profit:
                max_profit = profit
        current_index += 1
    
    return max_profit

'''
**ANALYZE**
First pass time complexity: O(n^2)
First pass space complexity: O(c) / constant
Space complexity is great, time complexity is not. It's poor because of the nested for loops.

Improvements:
Can I store and maintain the current value being compared without resorting to a loop?
I could instantiate max_profit as -inf so I don't have to account for negative profits
'''


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))