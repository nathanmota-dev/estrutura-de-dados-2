class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Exemplo de uso:
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert(root, key)

print("Arvore de pesquisa binaria em ordem crescente:")
inorder(root)