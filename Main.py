import mazegenmod as mgm
import sys

#recursion limit increased to handle larger maze sizes
sys.setrecursionlimit(5000)

# Maze dimensions (odd numbers)
width = 99
height = 99


# Generate and display the maze
maze = mgm.generate_maze(width, height)
mgm.display_maze(maze)


# Find and display the optimal route through the maze
route_maze = mgm.find_route(maze)
mgm.display_maze(route_maze, title="Maze with Optimal Route")