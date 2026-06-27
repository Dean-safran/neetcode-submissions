class trieNode :
    def __init__(self) :
        self.children = [None] * 26
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = trieNode()

    def insert(self, word: str) -> None:
        pointer = self.root
        for i in range(len(word)) : 
            index = ord(word[i]) - ord("a")
            """
            if the node at the index exists, continue
            through trie until the next letter in word
            doesn't exist in trie, then start adding nodes
            """
            if not pointer.children[index] : #if next letter doesn't exist
                pointer.children[index] = trieNode() 
                pointer = pointer.children[index]
            else : 
                pointer = pointer.children[index]
        pointer.end_of_word = True
        


    def search(self, word: str) -> bool:
        pointer = self.root
        for i in range(len(word)) : 
            index = ord(word[i]) - ord("a")
            if pointer.children[index] : 
                pointer = pointer.children[index]
            else : 
                return False
        return (pointer.end_of_word or False)

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for i in range(len(prefix)) : 
            index = ord(prefix[i]) - ord("a")
            if pointer.children[index] : 
                pointer = pointer.children[index]
            else : 
                return False
        return True
        