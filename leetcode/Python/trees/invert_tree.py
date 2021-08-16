class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        queue = [root]

        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node is None:
                continue

            current_node.left, current_node.right = current_node.right, current_node.left

            if current_node.left:
                self.invertTree(current_node.left)

            if current_node.right:
                self.invertTree(current_node.right)

        return root
