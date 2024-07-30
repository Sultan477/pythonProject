# Вам дана вершина бинарного дерева head.
# Необходимо развернуть дерево:
# поменять местами левого и правого потомка для каждого из потомков.
# Напишите функцию invert_tree(head),
# которая на вход будет принимать вершину бинарного дерева,
# а на выходе будет возвращать вершину развернутого дерева.

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(head):
    if not head:
        return None
    head.left, head.right = invert_tree(head.right), invert_tree(head.left)
    return head

if __name__ == '__main__':
    # Создаем дерево
    node = Node(4)
    node.left = Node(2)
    node.right = Node(7)
    node.left.left = Node(1)
    node.left.right = Node(3)
    node.right.left = Node(6)
    node.right.right = Node(9)

    # Развернем дерево
    new_node = invert_tree(node)

    # Выведем результат разворота дерева
    def print_tree(node):
        if not node:
            return
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)

    # print_tree(new_node)

    from collections import deque


    def print_tree_visual(node):
        if not node:
            return

        queue = deque()
        queue.append(node)

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.popleft()
                if current:
                    print(current.val, end=' ')
                    queue.append(current.left)
                    queue.append(current.right)
                else:
                    print('None', end=' ')

            print()  # Переход на новую строку между уровнями дерева


    # Пример вывода развернутого дерева в виде дерева
    print_tree_visual(new_node)

