class trieNode : 
    def __init__(self) : 
        self.children = [None] * 26
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = trieNode()

    def addWord(self, word: str) -> None:
        pointer = self.root
        for ch in word : 
            index = ord(ch) - ord("a")
            if not pointer.children[index] : 
                pointer.children[index] = trieNode()
            pointer = pointer.children[index]
        pointer.end_of_word = True


    def search(self, word: str) -> bool:
        pointer = self.root
        empty = [None] * 26
        
        def dfs(root, i) :
            nonlocal empty
            pointer = root 
            for j in range(i, len(word)) :
                if word[j] == "." : 
                    if pointer.children == empty :
                        return False

                    for root in pointer.children :
                        if not root:
                            continue
                        if dfs(root, j + 1) :
                            return True
                    return False
                childIndex = ord(word[j]) - ord("a")
                if not pointer.children[childIndex] : 
                    return False
                pointer = pointer.children[childIndex]
            return pointer.end_of_word
        return dfs(pointer, 0)


        