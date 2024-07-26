class Node:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insertWord(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            current = current.children[letter]
        current.isEndOfWord = True

    def searchWord(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return  current.isEndOfWord

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True

# Пример использования
if __name__ == '__main__':
    trie = Trie()
    trie.insertWord('apple')
    trie.insertWord('banana')

    print(trie.searchWord('apple'))
    print(trie.searchWord('app'))
    print(trie.startsWith('ban'))
    print(trie.startsWith('band'))