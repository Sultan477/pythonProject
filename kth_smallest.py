# Вам дан корень head бинарного дерева поиска (BST) и число k.
# Необходимо найти k-ый (нумерация с единицы) наименьший элемент в этом дереве поиска.
# Каждый узел дерева задается экземпляром класса Node, определенным ниже:
# head = [3,1,4,null,2], k = 1 даст 1.
# head = [5,3,6,2,4,null,null,1], k = 3 даст 3.
# Напишите функцию kth_smallest(head, k), которая на вход будет принимать корень дерево и число k,
# а на выходе выдавать одно значение.

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val

        root = root.right


if __name__ == '__main__':


    # Создаем узлы дерева
    node1 = Node(3)
    node2 = Node(1)
    node3 = Node(4)
    node4 = Node(2)

    # Связываем узлы в дерево
    node1.left = node2
    node1.right = node3
    node2.right = node4

    # Указываем корень дерева
    root = node1

    # Вызываем функцию для поиска 1-го наименьшего элемента
    k = 1
    result = kth_smallest(root, k)
    print(result)  # Ожидаемый результат: 1

    # Создаем другое дерево для второго примера
    node5 = Node(5)
    node6 = Node(3)
    node7 = Node(6)
    node8 = Node(2)
    node9 = Node(4)
    node10 = Node(1)

    node5.left = node6
    node5.right = node7
    node6.left = node8
    node6.right = node9
    node8.left = node10

    root2 = node5

    # Вызываем функцию для поиска 3-го наименьшего элемента
    k = 3
    result2 = kth_smallest(root2, k)
    print(result2)  # Ожидаемый результат: 3

