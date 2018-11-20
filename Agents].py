# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:49:16 2018

@author: gy18os
"""

import random
import operator
import matplotlib.pyplot
import Agent_Framework_2


#agent framework 2 is the file i want to input, .agent is the data. 
a = Agent_Framework_2.Agent()
print (a._y, a._x)
a.move()
print(a._y, a._x) 


def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a._x - agents_row_b._x)**2) + 
     ((agents_row_a._y - agents_row_b._y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

 # Make the agents.
for i in range(num_of_agents):
    agents.append(Agent_Framework_2.Agent())

 # Move the agents.
for j in range(num_of_iterations):
     for i in range(num_of_agents):
         agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
     #changed agent labels to match agent frame work.
     matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
 
matplotlib.pyplot.show()

for agents_row_a in agents:
     for agents_row_b in agents:
         distance = distance_between(agents_row_a, agents_row_b) 
         
         f = open("in.txt")
         
         import csv
f = open('data.csv', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    for value in row:				# A list of value
        print(value) 				# Floats
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.


         