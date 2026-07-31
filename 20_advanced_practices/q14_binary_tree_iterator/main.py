"""
Q14: Custom iterator that traverses a binary tree using in-order
traversal (left -> node -> right).

Run with: python main.py
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class InOrderIterator:
    """
    A custom ITERATOR (implements __iter__ and __next__) that performs
    in-order traversal iteratively using an explicit stack, instead of
    recursion, so it behaves like a real lazy iterator.
    """

    def __init__(self, root):
        self._stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node is not None:
            self._stack.append(node)
            node = node.left

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stack:
            raise StopIteration
        node = self._stack.pop()
        if node.right is not None:
            self._push_left(node.right)
        return node.value


def main():
    print("Q14: In-order binary tree iterator")

    #         8
    #       /   \
    #      3     10
    #     / \      \
    #    1   6      14
    #       / \     /
    #      4   7   13
    tree = TreeNode(
        8,
        left=TreeNode(3, left=TreeNode(1), right=TreeNode(6, left=TreeNode(4), right=TreeNode(7))),
        right=TreeNode(10, right=TreeNode(14, left=TreeNode(13))),
    )

    print("In-order traversal:")
    for value in InOrderIterator(tree):
        print(value, end=" ")
    print()


if __name__ == "__main__":
    main()
