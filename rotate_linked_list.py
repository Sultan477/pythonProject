'''Вам дана голова односвязного списка head. Вам необходимо «повернуть» его направо на k позиций.
Напишите функцию rotate_right(head, k), которая будет возвращать голову повернутого листа.
Вам нельзя создавать новый односвязный список — нужно все изменения делать с существующим (т.е. переставлять связи внутри него).'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def rotate_right(head, k):
    if not head or not head.next:
        return head

    lenght = 1
    current = head

    while current.next:
        current = current.next
        lenght += 1

    # вычисляем фактическое кол-во шагов для поворота
    k = k % lenght

    if k == 0:
        return head

    # Находим новую голову
    new_head_pos = lenght - k
    current.next = head # Замыкаем список в кольцо
    current = head
    for _ in range(new_head_pos - 1):
        current = current.next

    new_head = current.next
    current.next = None

    return new_head

if __name__ == '__main__':

    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    new_head = rotate_right(node1, 2)

    current = new_head
    while current:
        print(current.value)
        current = current.next
