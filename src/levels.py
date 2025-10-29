from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """Return list of lists of node values by level (BFS)."""
    if root is None:
        return []

    res = []
    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


def zigzag_level_order(root):
    """Return list of lists of node values in zigzag order."""
    if root is None:
        return []

    res = []
    q = deque([root])
    left_to_right = True

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not left_to_right:
            level.reverse()
        res.append(level)
        left_to_right = not left_to_right

    return res


def right_side_view(root):
    """Return list of values visible from the right side."""
    if root is None:
        return []

    view = []
    q = deque([root])

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            # last node in this level → rightmost
            if i == level_size - 1:
                view.append(node.val)

    return view
