    #      F
    #    /  \
    #   B    G
    #  / \    \
    # A   D    I
    #    / \  /
    #   C   E H

Tree Traversal (Recursion)

Depth First Search(DFS)
    - PRE-order (root, left, right)
        F B A D C E G I H
    - IN-order  (left, root, right)
        A B C D E F G H I
    - POST-order(left, right, root)
        A C E D B H I G F

Pseudo Code
==================
PRE-order:

preOrder(root):
    if (!root):
        return
    access(root)
    preOrder(root->left)
    preOrder(root->right)

IN-order:

inOrder(root):
    if (!root):
        return
    inOrder(root->left)
    access(root)
    inOrder(root->right)

POST-order:

postOrder(root):
    if (!root):
        return
    postOrder(root->left)
    postOrder(root->right)
    access(root)