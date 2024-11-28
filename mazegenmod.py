import random
import matplotlib.pyplot as plt


#Generates a maze using the Recursive Backtracking algorithm.
def generate_maze(width, height):

    # Initialize the grid with walls
    grid = [['wall' for i in range(width)] for i in range(height)] 


    def carve_path(row, col):
   
        grid[row][col] = 'path'  # Mark the current cell as a path
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)  # Randomize the directions

        #dr and dc are x and y coordinates of directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < height and 0 <= new_col < width:  # Check if the new position is within the grid
                if grid[new_row][new_col] == 'wall':  # If the new position is a wall
                    grid[row + dr // 2][
                        col + dc // 2] = 'path'  # Carve a path between the current cell and the new cell
                    carve_path(new_row, new_col)  # Recursively carve paths from the new cell


    # Start carving the maze from the center
    carve_path(height // 2, width // 2)

    # Set the entrance and exit
    grid[0][1] = 'entrance'
    grid[height - 1][width - 2] = 'exit'
    grid[height // 2][1] = 'path'  # Ensure the entrance is connected to the maze
    grid[height // 2][width - 2] = 'path'  # Ensure the exit is connected to the maze

    return grid


#displays the maze using matplotlib
def display_maze(maze, title="Maze"):
    
    height = len(maze)
    width = len(maze[0])

    #can either have entrance and exit as passage or as unique colours
    colors = {'wall': 'black', 'path': 'white', 'entrance': 'white', 'exit': 'white', 'route': 'yellow'}

    fig, ax = plt.subplots(figsize=(width / 10, height / 10))

    for row in range(height):
        for col in range(width):
            color = colors.get(maze[row][col], 'gray')  # Get the color for the cell
            ax.add_patch(plt.Rectangle((col, height - 1 - row), 1, 1, color=color))  # Draw the cell

    #formatting the graph
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.gcf().canvas.manager.set_window_title(f"Generated Maze of size {width}x{height}")
    plt.title = title
    plt.show()


#finds the optimal route through the maze
def find_route(maze):
    
    height = len(maze)
    width = len(maze[0])

    #runs a depth-first search to find the route
    def dfs(row, col, visited):

        if (row, col) in visited:
            return False
        visited.add((row, col))

        if maze[row][col] == 'exit':
            return True  # Exit found

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < height and 0 <= new_col < width:
                if maze[new_row][new_col] in ('path', 'exit') and dfs(new_row, new_col, visited):
                    maze[row][col] = 'route'  # Mark the route in yellow while backtracking
                    return True
        return False
    
    #set used for efficiency
    visited = set()
    for row in range(height):
        for col in range(width):
            if maze[row][col] == 'entrance':
                dfs(row, col, visited)
                break

    return maze