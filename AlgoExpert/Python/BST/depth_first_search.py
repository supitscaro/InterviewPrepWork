# you're given a Node class that has a name and an array of optional children nodes.
# when put together, nodes form an acyclic tree like structure

# implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the
# Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in
# the input array and returns it

# NOTES
# since we need to go from left to right, we can do in-order traversal
# !! we can't actually do in-order traversal because the self is the actual node, not the tree
# we nee to actually append self to the array, and if self has children then we need to recursively call
# the depthFirstSearch where we pass in our array
# then we can just return the array
# we have an addChild function that we can also put to use
# if we hit None, we should just return

# PSEUDOCODDE
'''
    def depthFirstSearch(self, array):
        array.append(self)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

'''


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            depthFirstSearch(array)
        return array
