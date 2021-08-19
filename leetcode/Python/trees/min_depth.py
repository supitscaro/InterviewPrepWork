# given a binary tree, find its minimum depth
# the minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node

class Solution:
    def minDepth(root):
        queue = [root]
        res = 0

        if root is None:
            return res

        while len(queue) > 0:
            level_length = len(queue)
            res += 1

            for _ in range(level_length):
                current_node = queue.pop(0)

                if current_node.left is None and current_node.right is None:
                    return res

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

        return res
