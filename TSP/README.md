# TSP using A*

## Problem:

Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?

## State Space

**State:** List of cities

**Start State:** Salesman in the start city and has not visited any other city

**Goal State:** Salesman has visited all the cities and reached the start city again

**Action:** Add new city that have not yet visited

**Cost:**

**1. Edge Cost:** Distance between the cities represented by the nodes, use this cost to calculate g(n).
	
**2. Heuristic Cost:** Distance to the nearest unvisited city from the current city + estimated distance to travel all          the unvisited cities (MST heuristic used here) + nearest distance from an unvisited city to the start city. **This is an 	admissible heuristic function.**


## Compile and Run

g++ TSP.cpp

./a.out

## Input & Output

Give the input number of cities and their adjacency matrix like

**Enter the no. of Cities:** 5

**Enter the path cost**

0 &nbsp; 12 &nbsp;10  &nbsp;19  &nbsp;8 &nbsp;

12  &nbsp;0 &nbsp; 3 &nbsp;  7 &nbsp;  2 &nbsp;

10 &nbsp; 3 &nbsp;  0 &nbsp;  6 &nbsp;  20

19 &nbsp; 7 &nbsp;  6 &nbsp;  0 &nbsp;  4 &nbsp;

8 &nbsp; 2 &nbsp;  20 &nbsp; 4 &nbsp;  0 &nbsp;

