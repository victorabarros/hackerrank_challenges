# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root: Node):
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    resp = 0
    second_to_last, last = None, None
    if root.left:
        last = root.left
        resp += 1
    elif root.right:
        last = root.right
        resp += 1

    while True:
        if last.left:
            second_to_last = last
            last = last.left
            resp += 1
        elif last.right:
            second_to_last = last
            last = last.right
            resp += 1
        else:
            break

    return resp


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
