#!/usr/bin/python

import math

'''
**UNDERSTAND THE PROBLEM**
Function returns the maximum number of whole recipe batches that can be made considering the amount of ingredients that are available.

If an ingredient from a recipe isn't in the ingredients dictionary, the recipe cannot be made at all.

Need to be able to divide the amounts of ingredients available by the number the recipe calls for.

**MAKE A PLAN**
First, check that all keys from recipe exist in ingredients. If not, return 0

For key in recipe:
  if key not in ingredients:
    return 0
  else:
    do stuff

Ensuring that the keys match up, divide the value in ingredients by the value in recipe
  rec_value = recipe.get(key)
  ing_value = ingredients.get(key)

  Add ing_value / rec_value to a list

If any resulting value is less than 0,  return 0

batches = int(min(list_of_batches))

Out of all the values greater than 1, find and return the minimum value. Could use min()
'''
def recipe_batches(recipe, ingredients):
    batch_amts = []

    for key in recipe:
        if key not in ingredients:
            return 0
        else:
            rec_value = recipe.get(key)
            ing_value = ingredients.get(key)

            batch_amts.append(ing_value / rec_value)
    
    return int(min(batch_amts))
        


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))