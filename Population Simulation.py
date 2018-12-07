# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:56:39 2018

@author: Roland
"""


# WORK STREAM =================================================================

# Generate population --> Grow Food --> Move Individuals --> Eat Food


# IMPORT PACKAGES =============================================================
import random
import matplotlib.pyplot as plt


# CREATE A DICTIONARY FOR OUR POPULATION ======================================
# As part of the construction process we will use a dictionary to keep record
# of which statistic is stored in each index for our individuals:
ind_info = {
        "name":0,
        "x_pos": 1,
        "y_pos":2,
        "max_energy":3,
        "curr_energy":4,
        "speed":5,
        "eaten":6,
        "control":7}

# Now we can quickly determine which index to use when coding. For example, if 
# we want to reference the energy of the individual, we simply type:
ind_info["curr_energy"]
#... and this gives us the index we need to use!


# GENERATE OUR POPULATION =====================================================

# Create a function to generate our population. We will create lists and then
# zip them into a list of tuples:

def spawnPopulation(popSize, me):
    name = list(range(popSize))
    x_pos = [0] * popSize
    y_pos = [0] * popSize
    max_energy = [me] * popSize # <- to be kept constant
    curr_energy = max_energy[:] # <- to be updated as the individual moves
    speed = [1] * popSize
    eaten = [0] * popSize # <- indicate whether the individual has eaten
    control = [me] * popSize # <- measures whether energy just goes up because of the lower bound
    # Pull together our population using zip()
    population_zip = zip(name, x_pos, y_pos, max_energy, curr_energy, speed, eaten, control)

    # And create a list of nested lists
    population = [list(l) for l in population_zip]

    #print("COMPLETED - SPAWNING POPULATION")
    
    return(population)

# -------------------------------------S---------------
# How do we reference individuals in the population?
# population[0] # <- pulls the first individual
# population[0][ind_info["name"]] # <- pulls the first individual's name
# ----------------------------------------------------



# SIMULATE MOVING =============================================================

# WE NEED TO ADJUST THIS TO ADD SOME SORT OF "SENSE" TO THE INDIVIDUALS MOVEMENT

# We need to shift the x or y coordinate by 1/-1 at each step.

# We'll define a move() function:
def move(population):
    """ Moves our individuals in a random direction and then reduces their energy
    by 1. This function takes the population list as an argument. """            

    # For each individual we determine an axis to move on and a direction to move:
    # Initialize empty lists:
    axis = []
    direction = []

    # Loop through the population:
    for i in range(len(population)):
        axis.append(random.randint(1,2)) # <- randomize 1 or 2 and use this as an indexed references
        if random.randint(0,1) == 1: # <- This if-else clause is probably not the best method
            direction.append(1)
        else:
            direction.append(-1)

    # Now use these to update population and 'move' our individuals!
    for i in range(len(population)):
        
        # Only move individuals who have not eaten this round and who still have energy:
        if population[i][ind_info["eaten"]] == 0 and population[i][ind_info["curr_energy"]] > 0:
            population[i][axis[i]] = population[i][axis[i]] + direction[i] 
        
            # We also need to reduce the energy of our individuals.
            # We can use our dictionary ind_info to reference the positions!
            # This means we can reference specific charactersistics of our individuals
            # without using ugly indexes (and getting all confused when we come back to
            # look at our code)!
            population[i][ind_info["curr_energy"]] = population[i][ind_info["curr_energy"]] - 1
    
    # Dirty fix for this movement off the map
    # We say that any creature that tries to move "off" the map, moves on the same axis
    # but turns around and moves the other way. That way we can fix it by just adding 2
    # to any x or y values that are less than zero.
    for i in range(len(population)):
        if population[i][ind_info["x_pos"]] < 0:
            population[i][ind_info["x_pos"]] = population[i][ind_info["x_pos"]] + 2
            
        if population[i][ind_info["y_pos"]] < 0:
            population[i][ind_info["y_pos"]] = population[i][ind_info["y_pos"]] + 2
  
    #print("COMPLETED - MOVING POPULATION")    
    
    return(population)
        





# START OF DAY PHASE ==========================================================

# We start by simulating the food.
# We create a list of tuples containing the coordinates for each piece of food.

# We can create a function to make this a little tidier:
def grow_food(foodCount, mapSize):
    """ Samples x and y coordinates within the range of the map and then 
    uses these value to create tuples to act as coordinates for food """
    food_x = []
    food_y = []
    
    for i in range(foodCount):
        food_x.append(int(random.uniform(0, mapSize + 1)))
        food_y.append(int(random.uniform(0, mapSize + 1)))

    food_zip = zip(food_x, food_y)
    
    food = [list(l) for l in food_zip]
    
    # Give a visual of where our food has grown:
    # plt.scatter(*zip(*food), color = "green")
    # plt.show()

    #print("COMPLETED - GROWING FOOD")

    return(food)
  





# FOOD CONSUMPTION ============================================================

# We need to loop through our population and check each food location to see if
# anyone has found something to eat.

def eatFood(p, f):
    """ Loops through the population to get the (x,y) loc for each individaul and
    compares them to the (x,y) locations of all the remaining food. If there is a match
    then the food is eaten (removed from the food list) and the eaten status of the
    individual is updated. """
    
    for i in range(len(p)):
        
        # Skip any individuals who have already eaten this round:
        if p[i][ind_info["eaten"]] == 1:
            continue
        
        # Now for individuals who have not yet eaten:
        xloc = p[i][ind_info["x_pos"]] # <- get x location of current individual
        yloc = p[i][ind_info["y_pos"]] # <- get y location of current individual
        loc = [xloc, yloc] # <- combine to create a complete location
    
        # Now loop through each piece of food to see if we get a match
        for j in range(len(f)):
            if loc == f[j]:
                p[i][ind_info["eaten"]] = 1 # <- update the eaten status for the individual
                p[i][ind_info["curr_energy"]] = 0 # <- reduce energy to 0 as its not needed
                del(f[j]) # <- remove the food from the map
                break

    global population
    population = p
    
    global food
    food = f

    #print("COMPLETED - EATING FOOD")
    
    
# UPDATE DEAD/ALIVE STATUS ====================================================        

def killIndividuals(p):
    """ Deletes any individuals who are both out of energy and did not find food
    to eat this round. """
    
    # Initialize our death records
    death_records = []
    
    for i in range(len(p)):
                
        # Check if the individual is out of energy AND has not eaten this round:
        if p[i][ind_info["curr_energy"]] == 0 and p[i][ind_info["eaten"]] == 0:
            death_records.append(i) # <- if so, add this individual to the death records    

    # Figure out who the survivors are via the death records:
    survivors = set(range(len(p))).difference(death_records)
    
    # Update the global population list:
    global population
    population = [p[s] for s in survivors]
    
    #print("COMPLETED - MORTICIAN'S REPORT")
            
    
    
    
# RESET INDIVIDUALS ===========================================================

# At the end of the day all the surviving members of the population head back to 
# camp at (0,0). We assume that all indivduals who ate make it back to camp safely
# and without loss of energy.    

def returnToCamp(p):
    """ Resets the (x,y) position, energy level and eaten status of the population. """

    for i in range(len(p)):
        p[i][ind_info["curr_energy"]] = p[i][ind_info["max_energy"]] 
        p[i][ind_info["x_pos"]] = 0 
        p[i][ind_info["y_pos"]] = 0
        p[i][ind_info["eaten"]] = 0
            
    return(p)        
 

# MUTATIONS ===================================================================

# For each new child, we give a chance to mutate their characteristics.
def mutate(c):
    
    # Mutate maximum energy:
    mutation_result = random.uniform(0,1)
    
    if mutation_result < 0.1:
        c[ind_info["max_energy"]] = c[ind_info["max_energy"]] - 1
    
    if mutation_result > 0.9:
        c[ind_info["max_energy"]] = c[ind_info["max_energy"]] + 1
        
    return(c)
    

# REPRODUCTION ================================================================
    
# We need to add a reproduction process. Individuals will "reproduce" if they 
# successfully eat food. The reproduction is carried out by creating a replica
# of the parent. For now, given there is no mutation in the program we will just
# directly copy the attributes of the parent.

def reproduce(p):
    
    
    global population_records
    # Initialize our birth records:
    birth_records = []
    
    # loop through each individual
    for i in range(len(p)):
        # check if the individual has eaten:
        if p[i][ind_info["eaten"]] == 1:
            # if so, create a replica:
            child = p[i][:]
            
            # mutate:
            child = mutate(child)
            
            # update the name:
            child[ind_info["name"]] = population_records[-1] + 1
            # and update the population records
            population_records.append(population_records[-1] + 1)
            # add child to the population
            birth_records.append(child)
            
    # Add new births to population:
    p = p + birth_records
    # Print our completion message:
    #print("COMPLETED - REPRODUCTION")
    # Finally return our new population:
    return(p)           
         
            
            
# PULL IT ALL TOGETHER ========================================================


# parameters

kMapSize = 15 # <- Only set up for a square plane right now (x = y)
kPopSize = 100
kFoodCount = 100

# Spawn our population
population = spawnPopulation(kPopSize, me = 30)

# Create a replica that we store as the initial population. We can use this to 
# compare to the final population to see how the natural selection process works:

initial_population = population[:]
# Generate our birth records:
population_records = list(range(kPopSize))

average_energy = []

for days in range(1000):
    
    # Keep a tracker of how the energy progress through the days
    average_energy.append(sum(list(zip(*population))[ind_info["max_energy"]]) / len(population))
    
    # Give the user an output of what day we're on:
    print(days)
    
    # Reproduce!
    population = reproduce(p = population)

    # Return to camp
    population = returnToCamp(p = population)
    
    # Grow Food
    food = grow_food(kFoodCount, kMapSize)
    
    # Only run while individuals still have energy AND food still exists
    while sum(list(zip(*population))[ind_info["curr_energy"]]) > 0 and len(food) > 0:
    
        # Move population
        population = move(population)
    
        # Eat food
        eatFood(p = population, f = food)          
    
    # Kill 0 energy individuals
    killIndividuals(p = population)
    
    

# PLOTTING ====================================================================

# Compare the starting energy of all individuals to the final energy:
plt.hist(list(zip(*population))[ind_info["max_energy"]])           
plt.hist(list(zip(*initial_population))[ind_info["max_energy"]], color = "red")            
 
# And a tracker of how the average energy develops as the days go on:           
plt.plot(average_energy)



# PLAYGROUND ==================================================================

# How do we play around with speed?

# We need a downside to speed (it costs more energy)

# If someone has 2 speed, they get 2 moves on each move turn. We need to search for food
# after each movement (since the individual won't just move past food because they have
# an extra move turn).







