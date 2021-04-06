## Trees

![Tree Labeled](../images/treeLabeled.png)

![Types of Trees](../images/comparingAlgorithms.png)

### Describe a Tree

- a *full* tree is where a node has NO children or TWO children
    - if it has a descendant, it MUST have TWO of them

- in a *complete* tree (heap), when we fill out a node, we go top to bottom, then left to right

- a *perfect* binary tree is one that is both complete AND also full
    - every node that has descendants or children, have TWO

### Explain the Traversals
- the prefix tells us the order in which we visit the node we're sitting at

#### Pre Order - before we visit the left and right subtree, we visit the node
- Self => Left => Right

#### In Order - we visit the node in the mid of the left and right subtree
- Left => Self => Right

#### Post Order - after we visit the left and right subtree, we visit the node
- Left => Right => Node
