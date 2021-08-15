class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def traverse(root):
        result = []
        queue = [root]

        if root is None:
            return result

        while len(queue) > 0:
            level_length = len(queue)
            current_level = []

            for _ in range(level_length):
                current_node = queue.pop(0)

                current_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            # do result.extend(current_level) to flatten results
            result.append(current_level)

        return result
