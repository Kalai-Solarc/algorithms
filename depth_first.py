from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    current = root

    while current:
        if val < current.val:
            current = current.left
        elif val > current.val:
            current = current.right
        else:
            return current

    return None


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = [(root, False)]

    while stack:
        (node, visited) = stack.pop()

        if node:
            if visited:
                result.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

    return result
