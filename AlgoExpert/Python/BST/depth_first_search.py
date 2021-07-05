# you're given a Node class that has a name and an array of optional children nodes.
# when put together, nodes form an acyclic tree like structure

# implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the
# Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in
# the input array and returns it

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        pass
