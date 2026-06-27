class trieNode : 
    def __init__(self) : 
        self.children = [None] * 26
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = trieNode()

    # time is o(l) where l is the length of the word since we 
    # do a constant check into the children array to see if 
    # next trieNode letter exists, if not make the node, a constant operation

    # space is o(l) since worst case we create nodes for every 
    # letter in word
    def addWord(self, word: str) -> None:
        pointer = self.root
        for ch in word : 
            index = ord(ch) - ord("a")
            if not pointer.children[index] : 
                pointer.children[index] = trieNode()
            pointer = pointer.children[index]
        pointer.end_of_word = True

    # when the next char is ".", we have to index into all the current
    # node's (the 'root') children, so we essentially treat 
    # every child as a root node and run DFS on them

    # DFS to see if a word exists in trie is o(l), if we have two 
    # dots, worst case in we do 26 searches 26 times, total 
    # time is o(26^2 * l) = o(l), recursion depth is o(1) 
    # since we only recurse when we have a dot, which 
    # is max twice, so space is o(1)  
    def search(self, word: str) -> bool:
        pointer = self.root
        empty = [None] * 26
        
        def dfs(root, i) :
            nonlocal empty
            pointer = root 
            for j in range(i, len(word)) :
                if word[j] == "." : 

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


        