# Number of vertices in the graph
# define V 4
V = 4
# check if the colored
# graph is safe or not
def isSafe( graph : bool, color : int) -> bool:
    # check for every edge
    for i in range(V):
        for j in range(i+1, V):
            if (graph[i][j] and color[j] == color[i]):
                return False
    return True

# A utility function to print solution
def printSolution( color: int ):
    print("Solution Exists: Following are the assigned colors \n")
    for i in range(V):
        print(color[i])
    print("\n")

# This function solves the m Coloring problem using recursion.
# It returns false if the m colours cannot be assigned,
# otherwise, return true and prints assignments of colours to all vertices.
# Please note that there may be more than one solutions,
# this function prints one of the feasible solutions.
def graphColoring( graph : bool, m : int, i : int, color : int) -> bool:
    # if current index reached end
    if (i == V):
        # if coloring is safe
        if (isSafe(graph, color)) :
            # Print the solution
            printSolution(color)
            #return True;
        return False

    # Assign each color from 1 to m
    for j in range(1, m+1):
        color[i] = j
        # Recur of the rest vertices
        if (graphColoring(graph, m, i + 1, color)):
            return True
        color[i] = 0

    return False

if __name__ == "__main__":
    # Driver program to test above function
    # Create following graph and test whether it is 3 colorable
    # (3) - --(2)
    #  |    /  |
    #  |   /   |
    #  |  /    |
    # (0) - --(1)
    graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    m = 4 # Number of colors

    # Initialize all color values as 0.
    # This initialization is needed
    # correct functioning of isSafe()
    color = [0]*V

    if (not graphColoring(graph, m, 0, color)):
        print("Solution does not exist")

