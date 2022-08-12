#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:37:17 2022

@author: windhoos
"""
'''
import binpacking
from ortools.linear_solver import pywraplp


def binp():
    b = { 'a': 10, 'b': 10, 'c':11, 'd':1, 'e': 2,'f':7 }
    
    b = list(b.values())
    bins = binpacking.to_constant_volume(b,11)
    print("===== list\n",b,"\n",bins)

def create_data_model(weights,capacity):
    """Create the data for the example."""
    data = {}
    #weights = [48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30]
    data['weights'] = weights
    data['items'] = list(range(len(weights)))
    data['bins'] = data['items']
    data['bin_capacity'] = capacity
    return data

def ortools(w,c):
    #w=weights = [1,2,3]
    #c=capacity = int(1)
    data = create_data_model(w,c)

    # Create the mip solver with the SCIP backend.
    #solver = pywraplp.Solver.CreateSolver('SCIP')
    solver = pywraplp.Solver.CreateSolver('GLOP')
    #solver = pywraplp.Solver.CreateSolver('GUROBI')

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}
    for i in data['items']:
        for j in data['bins']:
            x[(i, j)] = solver.IntVar(0, 1, 'x_%i_%i' % (i, j))

    # y[j] = 1 if bin j is used.
    y = {}
    for j in data['bins']:
        y[j] = solver.IntVar(0, 1, 'y[%i]' % j)

    # Constraints
    # Each item must be in exactly one bin.
    for i in data['items']:
        solver.Add(sum(x[i, j] for j in data['bins']) == 1)

    # The amount packed in each bin cannot exceed its capacity.
    for j in data['bins']:
        solver.Add(
            sum(x[(i, j)] * data['weights'][i] for i in data['items']) <= y[j] *
            data['bin_capacity'])

    # Objective: minimize the number of bins used.
    solver.Minimize(solver.Sum([y[j] for j in data['bins']]))

    status = solver.Solve()
    
    binlist=[]
    
    if status == pywraplp.Solver.OPTIMAL:
        num_bins = 0.
        for j in data['bins']:
            if y[j].solution_value() == 1:
                bin_items = []
                bin_weight = 0
                for i in data['items']:
                    if x[i, j].solution_value() > 0:
                        bin_items.append(i)
                        bin_weight += data['weights'][i]
                if bin_weight > 0:
                    num_bins += 1
                    #print('Bin number', j)
                    #print('  Items packed:', bin_items)
                    #print('  Total weight:', bin_weight)
                    #print()
                    binlist.append([bin_items,bin_weight])
        #print()
        #print('Number of bins used:', num_bins)
        #print('Time = ', solver.WallTime(), ' milliseconds')
    else:
        pass
        print('error')
    
    return binlist
'''
# Python program to find number of bins required using
# First Fit Decreasing algorithm.
 
# Returns number of bins required using first fit
# online algorithm

def firstFit(weight, n, c):
    # Initialize result (Count of bins)
    res = 0
    # Create an array to store remaining space in bins
    # there can be at most n bins
    bin_rem = [0]*n
    
    plank_sort=[]
    for i in range(len(bin_rem)):
        plank_sort.append([])
    # Place items one by one
    for i in range(n):
        # Find the first bin that can accommodate
        # weight[i]
        j = 0
        while( j < res):
            if (bin_rem[j] >= weight[i]):
                bin_rem[j] = bin_rem[j] - weight[i]
                plank_sort[j].append(weight[i])
                break
            j+=1
        # If no bin could accommodate weight[i]
        if (j == res):
            bin_rem[res] = c - weight[i]
            plank_sort[res].append(weight[i])
            res= res+1
            
    plank_sort2 = [ele for ele in plank_sort if ele != []]
            
    return res, plank_sort2

# Returns number of bins required using first fit
# decreasing offline algorithm
def firstFitDec(weight, c):
    n=len(weight)
    # First sort all weights in decreasing order
    weight.sort(reverse = True)
    # Now call first fit for sorted items

    return firstFit(weight, n, c)
 