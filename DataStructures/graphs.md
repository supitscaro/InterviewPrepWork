## Graphs

![Graphs](../images/graphs.png)

### Basic Definitions of Graphs
- Order: the number of vertices in the graph
- Size: the number of edges in the graph
- Vertex degree: the number of edges that are incident to a vertex
- Isolated vertex: a vertex that is not connected to any other vertices in the graph
- Directed graph: a graph where all the edges have a direction indicating what is the start vertex and what is end vertex
- Undirected graph: a graph with edges that have no direction
- Weighted graph: edges of the graph have weights
- Unweighted graph: edges of the graph have no weights

### Graphs Explanations
- There are no rules regarding the connection among the nodes or vertices in a graph.
- The edges in a graph are the lines that connect each node or vertex. These edges can connect the nodes in any way possible.

#### Two Types of Edges
There are two types of edges: directed and undirected.
- Directed: connections that are one way. One point is the origin and the other point is the end point
- Undirected: connections are two ways.

Directed edges can be represented as an ordered pair, such as (A, B). *A* would be the origin whereas *B* is the destination. Remember that directed edges only go one way, so we do not have a path from B to A; we only have a path from A to B. If we wanted to have a direction from B to A, we would need to add another edge pointing from B to A.

Undirected edges are represented as {A, B}

### Adjacency Matrix
This matrix is a representation of which nodes in a graph contain edges between them
- once we know the two nodes we want to find an edge between, we find the value the two nodes intersect at
- the values in this matrix are booleans, or 0s and 1s. If there's a 1, that means there's an edge between the two nodes. If there's a 0, that means there's no edge between the two nodes

```javascript
let matrix = [
/*        A  B  C  D  E  F   */
/*A*/    [1, 1, 1, 0, 1, 0],
/*B*/    [0, 1, 0, 0, 0, 0],
/*C*/    [0, 1, 1, 1, 0, 0],
/*D*/    [0, 0, 0, 1, 0, 0],
/*E*/    [1, 0, 0, 0, 1, 0],
/*F*/    [0, 0, 0, 0, 1, 1]
];
```
We can tell if the graph is directed or undirected based on whether the matrix is symmetric or not.
If the values on both sides of the main diagonal are the same, the matrix is considered symmetric.

Meaning: Row E, Column A should be the same value as Row A, Column E

If the edges have direction, note that ```matrix[i][j]``` is not the same as ```matrix[j][i]```

##### Pros and Cons
One thing to note here is that this type of matrix is pretty easy to read and follow. Looking up, inserting, and removing an edge can be done in constant time or O(1).

However,looking at the previous matrix example, you can see how much space is taken that contain the value 0. This matrix is mostly filled with 0s and they take up space that's not necessarily needed.

### Adjacency Lists
This is a hybrid of an adjacency list and an edge list. This is an array of linked lists that shows a representation of a graph and makes it easy to see which other vertices are adjacent to other vertices.

- Every single node/vertex will have a reference to all of its neighbors through an adjacent linked list

The structure of an adjacency list makes it very easy to determine all the neighbors of a particular node/vertex.

```javascript
let graph = {
    'a': ['b', 'c', 'e'],
    'b': [],
    'c': ['b', 'd'],
    'd': [],
    'e': ['a'],
    'f': ['e']
};
```
- the **'keys'** are the vertex
- the **'values'** are the neighboring vertices

The values are connected to the keys.

##### Pros and Cons
Retrieving a node's neighbors with an adjacency list takes constant time.

This is different when trying to find a specific edge, (x, y). We know that to find a vertex, x, in an adjacency list it takes constant time. Our second step is to check if y is in the adjacency list for node x.

Worst case scenario, y could be at the very end of our list or not even exist, which means this will take O(d) time, where d is the degree of vertex x.
    - Note: our *degree* is the number of edges that a vertex has, which is also the number of neighboring nodes.



## Depth First Search
- With this, we use a stack.
    - This stack can either be our own or the call stack via recursion
    - Last In, First Out scenario
- This is all about depth and goes deep
- Its priority is to go deep into its path

#### When To Use It
- Can be used for backtracking, performing a complete search, exhausting every possible path

## Breadth First Search
- With this, we traverse iteratively using a queue
    - First In, First Out
- This is all about breadth and goes *wide*.
- Its priority is to go level by level

#### When To Use It
- Can be used to check if a path exists between each vertex or node, finding distance or levels away from something.
