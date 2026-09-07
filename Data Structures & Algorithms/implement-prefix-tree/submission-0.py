from collections import deque

class PrefixNode:
    def __init__(self):
        self.children = {} ## to keep 26 characters
        self.endOfWord = False

        # children["a"] = PrefixNode()


class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = PrefixNode()
            current = current.children[char]
        current.endOfWord = True
            


    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.endOfWord


        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True
        
        