# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:56:39 2018

@author: Roland
"""

# Simulating a population

import numpy as np
import random


# parameters

kMapSize = 100 # <- Only set up for a square plane right now (x = y)
kPopSize = 10
kFoodCount = 10


# CREATE A DICTIONARY FOR OUR POPULATION ======================================
# As part of the construction process we will use a dictionary to keep record
# of which statistic is stored in each index for our individuals:
ind_info = {
        "name":0,
        "x_pos": 1,
        "y_pos":2,
        "energy":3,
        "status":4}

# Now we can quickly determine which index to use when coding. For example, if 
# we want to reference the energy of the individual but can't remember the index,
# we simply type:
ind_info["energy"]
#... and this gives it to us!


# GENERATE OUR POPULATION =====================================================

name = list(range(kPopSize))
x_pos = [0] * kPopSize
y_pos = [0] * kPopSize
energy = [10] * kPopSize
status = [1] * kPopSize # <- 1 for alive, 0 for dead
eaten = [0] * kPopSize
# Pull together our population using zip()
population_zip = zip(name, x_pos, y_pos, energy, status)

# And create a list of nested lists
population = [list(l) for l in population_zip]

# -------------------------------------S---------------
# How do we reference individuals in the population?
population[0] # <- pulls the first individual
population[0][ind_info["name"]] # <- pulls the first individual's name
# ----------------------------------------------------



# SIMULATE MOVING =============================================================

# We need to shift the x or y coordinate by 1/-1 at each step.

# For each individual we determine an axis to move on and a direction to move:

# Initialize empty lists:
axis = []
direction = []

# Loop through the population:
for i in range(kPopSize):
    axis.append(random.randint(1,2))
    if random.randint(0,1) == 1: # <- This if-else clause is probably not the best method
        direction.append(1)
    else:
        direction.append(-1)

# Now use these to update population and 'move' our individuals!
for i in range(kPopSize):
    population[i][axis[i]] = population[i][axis[i]] + direction[i] 
    
    # We also need to reduce the energy of our individuals.
    # We can use our dictionary ind_info to reference the positions!
    # This means we can reference specific charactersistics of our individuals
    # without using ugly indexes (and getting all confused when we come back to
    # look at our code)!
    population[i][ind_info["energy"]] = population[i][ind_info["energy"]] - 1
    
""" Dirty fix for this movement off the map """
# We say that any creature that tries to move "off" the map, moves on the same axis
# but turns around and moves the other way. That way we can fix it by just adding 2
# to any x or y values that are less than zero.
for i in range(kPopSize):
    if population[i][ind_info["x_pos"]] < 0:
        population[i][ind_info["x_pos"]] = population[i][ind_info["x_pos"]] + 2

    if population[i][ind_info["y_pos"]] < 0:
        population[i][ind_info["x_pos"]] = population[i][ind_info["x_pos"]] + 2
    
# Put this all into a function: (TO BE COMPLETED)
def move():
    """ Moves our individuals in a random direction and then reduces their energy
    by 1. This function does not take any arguments and relies on parameters 
    within the simulation code """            
        
        
        


# FOOD CONSUMPTION ============================================================

# We need to loop through our population and check each food location to see if
# anyone has found something to eat.

for i in range(kPopSize):
    xloc = population[i][ind_info["x_pos"]] # <- get x location of current individual
    yloc = population[i][ind_info["y_pos"]] # <- get y location of current individual
    loc = [xloc, yloc] # <- combine to create a complete location
    
    # Now loop through each piece of food to see if we get a match
    for j in range(kFoodCount):
        if loc = food[j]:
            population[i][ind_info["eaten"]] = 1

food[0]

# UPDATE DEAD/ALIVE STATUS ====================================================        




# START OF DAY PHASE ==========================================================

# We start by simulating the food.
# We create a list of tuples containing the coordinates for each piece of food.

""" WE NEED TO EDIT THIS SO THAT FOOD SPAWNS ARE DISTINCT """

# Initialize empty lists of the x and y coordinates for each piece of food:
food_x = []
food_y = []

for i in range(kFoodCount):
    food_x.append(random.randint(0,kMapSize - 1)) # remove 1 to get 100 squares
    food_y.append(random.randint(0,kMapSize - 1))

# Use zip to create tuples...
food = zip(food_x, food_y)
# ... and convert to a list:
food_list = list(food)

# We can create a function to make this a little tidier:
def grow_food(foodCount, mapSize):
    """ Samples x and y coordinates within the range of the map and then 
    uses these value to create tuples to act as coordinates for food """
    food_x = []
    food_y = []
    
    for i in range(kFoodCount):
        food_x.append(int(random.uniform(0,kMapSize + 1)))
        food_y.append(int(random.uniform(0,kMapSize + 1)))

    food_zip = zip(food_x, food_y)
    
    food = [list(l) for l in food_zip]

    return(food)

food = grow_food(kFoodCount, kMapSize)    





    
    
    

    




# Start with our population. We create a list of length equal to our pop size
population = [1] * kPopSize

# We want to loop through "days" to see how many of our population survive each day

# Initialize our empty survival list
survival = []

# Generate our survival probs
for i in range(kPopSize):
    survival.append(random.uniform(0,1))

# Apply our logic to see who survives
result = survival < 1



