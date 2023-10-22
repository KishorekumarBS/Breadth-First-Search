import numpy as np
from queue import Queue


class bfsearch:
    def __init__(self, matrics, node_names) -> None:
        self.graphmatrics = matrics  # Store the adjacency matrix
        self.noOfNodes = len(self.graphmatrics)  # Calculate the number of nodes
        self.node_names = node_names  # Store the names of the nodes

    def bfs(self):
        visitednodes = [False] * self.noOfNodes  # Creating a list to Keep track of visited nodes
        queue = Queue(maxsize=self.noOfNodes)  # Creating a queue for BFS traversal
        queue.put(0)  # Starting BFS from the first node (index 0) that is in our case node "A"
        visitednodes[0] = True  # Marking the first node as visited that is Node "A"
        outputMatrics = np.zeros((self.noOfNodes, self.noOfNodes), dtype=int)  
        # Initializing the output matrix to return since the objective is tor print the output has matrix
        sumtrue=1

        while not queue.empty(): #until the queue is empty this while loop will be running
            visitingnode = queue.get()  # Get the next node to visit
            for neighbors in range(self.noOfNodes):
                
                # Exploring the neighbors of the current node
                if self.graphmatrics[visitingnode][neighbors] == 1 and not visitednodes[neighbors]:
                    visitednodes[neighbors] = True  # Mark the neighbor as visited
                    sumtrue+=1
                    queue.put(neighbors)  # Add the neighbor to the BFS queue
                    outputMatrics[visitingnode][neighbors] = 1  # Mark the edge in the output matrix

        return outputMatrics  # Return the BFS tree as an adjacency matrix

    def __str__(self):
        # Define a custom string representation for the object
        output = ["  " + " ".join(self.node_names)]  # Create the header row with node names
        bfs_result = self.bfs()  # Perform BFS and get the result as an adjacency matrix
        
        # Format and add rows for the BFS tree
        for i in range(self.noOfNodes):
            row = [self.node_names[i]] + [str(val) for val in bfs_result[i]]  # Format row with node name and values
            output.append(" ".join(row))  # Add the formatted row to the output

        return "\n".join(output)  # Combine rows and return as a formatted string

# Defining node names and adjacency matrix
node_names = ["A", "B", "C", "D", "E"]
graphMatrics = np.array([[0, 1, 0, 1, 1],
                         [1, 0, 1, 0, 1],
                         [0, 1, 0, 0, 1],
                         [1, 0, 0, 0, 0],
                         [1, 1, 1, 0, 0]])

# Create an instance of the bfsearch class
result = bfsearch(graphMatrics, node_names)

# Print the result, which displays the BFS tree with node names
print(result)
