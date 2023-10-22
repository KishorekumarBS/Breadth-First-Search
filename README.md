# Breadth-First-Search
Goal is to find a BFS traversal for the following graph by implementng with the adjacency matrix
<p align ="center">
<img width="432" alt="Screenshot 2023-10-21 at 9 04 46 PM" src="https://github.com/KishorekumarBS/Breadth-First-Search/assets/69570231/31429364-dc89-4043-9d54-68a8776f7719">
</p>
The bfs method within the bfsearch class implements the Breadth-First Search (BFS) algorithm on a given graph represented by an adjacency matrix.
It starts from an inital node (in my program I took “A” has inital node), systematcally explores its neighbors, and gradually expands its search level by level. In this method, a queue is used to keep track of nodes to be visited next, ensuring that nodes are processed in the order they were discovered.
It starts the traversal from an inital node, marks it as visited, and iteratvely explores its neighbors. For each unvisited neighbor, it marks the neighbor as visited, enqueues it, and updates the BFS tree if an edge is encountered. This process contnues untl all reachable nodes in the graph have been visited.<br>
Queue:empty<br>
visitednodes [False,False, False, False, False]<br>
Queue : 0 #0=A<br>
Visitednodes [True, False, False, False, False]<br>
Pop the first node in the queue and will check the neighbor of 0 (node “A”) and add those to the queue and will mark those has True in the visitednodes<br>
Queue : 1 3 4 #1=B,3=D, 4=E<br>
Visitednodes [True, True, False, True, True]<br>
Now since the neighbors of A are B, D, and E add all three to the queue and mark those three as visited. Now checking for neighbors of 1 (node “B”)<br>
Queue : 3 4 2 #2=C that is the only node yet to visit and adding it to the queue, as well as marking it as True<br>
 
Visitednodes [True, True, True, True, True]<br>
Now the loop will run for the node D and look for any unvisited neighbor node since there is nothing leQ, it will be popped out of the queue<br>
Queue: 4 2<br>
Visitednodes [True, True, True, True, True]<br>
Same happens for 4 and 2 and eventually the queue becomes empty and the program will terminate and the matrix wil be printed.<br>

## Output
“A” has inital node<br>
<img width="203" alt="Screenshot 2023-10-21 at 9 07 01 PM" src="https://github.com/KishorekumarBS/Breadth-First-Search/assets/69570231/eed9c8a0-a0be-48bf-b52a-893516027b62">

## Time complexity
### 1. Initalizing Data Structures:
>• Creatng the visitednodes list of length self.noOfNodes takes O(V) tme, where V is the
number of nodes.
>• Creatng the queue with a maximum size of self.noOfNodes also takes O(V) tme.
### 2. While Loop:
>• The while loop runs untl the queue is empty, and in the worst case, it can run once for
each node in the graph. So, it iterates O(V) tmes. Inside the Loop:
>• The for neighbors in range(self.noOfNodes) loop iterates over all nodes, which is O(V).
>• The check self.graphmatrics[visi;ngnode][neighbors] == 1 and not
visitednodes[neighbors] takes constant tme for each neighbor.
### 3. Enqueuing and Marking:
> • Enqueuing a neighbor (queue.put(neighbors)) and marking it as visited (visitednodes[neighbors] = True) takes constant tme.
So, the overall tme complexity of the BFS traversal in this code is O(V^2). This is because, in the worst case, the code might visit every node, and for each node, it might visit all its neighbors, resultng in a O(V^2).
