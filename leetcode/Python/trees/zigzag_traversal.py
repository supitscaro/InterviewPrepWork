# Given the root of a binary tree, return the zigzag level order traversal of its nodes value

class TreeNode:
    def __init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        queue = [root]

        right_to_left = True

        while len(queue) > 0:
            level_length = len(queue)
            current_level = []

            for _ in range(level_length):
                current_node = queue.pop(0)

                if right_to_left:
                    current_level.append(current_node.val)
                elif not right_to_left:
                    current_level.insert(0, current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            queue.append(current_level)
            right_to_left = not right_to_left

        return result
