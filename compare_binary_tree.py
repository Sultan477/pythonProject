# '''Вам даны два бинарных дерева head_1, head_2. Необходимо проверить, являются ли эти два дерева одинаковыми:
# имеют одинаковую структуру и одинаковые элементы на соответствующих узлах.
# head_1 = [1, 2, 3], head_2 = [1, 2, 3] даст True.
# head_1 = [1, 2], head_2 = [1, None, 2] даст False, т.к. структура не одинаковая.
# Напишите функцию are_trees_equal(head_1, head_2), которая на вход будет принимать два корня дерева и возвращать True или False.'''

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_trees_equal(head_1, head_2):
    if not head_1 and not head_2:
        return True
    if not head_1 or not head_2:
        return False
    if head_1.val != head_2.val:
        return False
    return are_trees_equal(head_1.left, head_2.left) and are_trees_equal(head_1.right, head_2.right)


if __name__ == '__main__':
    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(3)

    node2 = Node(1)
    node2.left = Node(2)
    node2.right = Node(3)

    print(are_trees_equal(node1, node2))

    node3 = Node(1)
    node3.left = Node(2)

    node4 = Node(1)
    node4.right = Node(2)

    print(are_trees_equal(node3, node4))
