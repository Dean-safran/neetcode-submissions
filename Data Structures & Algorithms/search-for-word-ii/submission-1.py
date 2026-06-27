class trieNode:
    def __init__(self) :
        self.children = [None] * 26
        self.end_of_word = False
    
class Trie:
    def __init__(self) :
        self.root = trieNode()

    def addWord(self, word):
        pointer = self.root
        for ch in word : 
            childIndex = ord(ch) - ord("a")
            if not pointer.children[childIndex] :
                pointer.children[childIndex] = trieNode()
            pointer = pointer.children[childIndex]
        pointer.end_of_word = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """ brute force method is 
            o(number of words * 
            number of tiles in board * 
            4^(length of word))
        """
        result = []
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        rows = len(board)
        cols = len(board[0])
        trie = Trie()
        
        for word in words:
            trie.addWord(word)
        
        def DFS(r, c, curr_TrieNode, word_so_far) :
            nonlocal result, rows, cols, moves
            
            if (min(r,c) < 0 or r >= rows or c >= cols or board[r][c] == "#") :
                return
            
            curr_letter = board[r][c]
            childIndex = ord(curr_letter) - ord("a")
            
            if (not curr_TrieNode.children[childIndex]) :
                return
            
            
            word_so_far += curr_letter
            if curr_TrieNode.children[childIndex].end_of_word :
                result += [word_so_far]
                curr_TrieNode.children[childIndex].end_of_word = False;
            board[r][c] = "#"
            for dy,dx in moves :
                DFS(r + dy, c + dx, curr_TrieNode.children[childIndex], word_so_far)
            board[r][c] = curr_letter
        
        
        for row in range(rows):
            for col in range(cols):
                DFS(row, col, trie.root, "")
        return result
            
        
        

        # Build the trie with all the words (implement classes, etc)
        
        # start the loop over the rows and cols calling DFS on each
        # block, if the current block on the board isn't reachable 
        # from our current position on the Trie, prune + continue
        # to backtrack, if it is, continue along the path with 
        # that block and trieNode

        """ DFS """
        # params: row, col, curr_TrieNode, word_so_far (a string), 
        

        # if the current letter is not in the current root's 
        # children array, or the current letter is "#" (visited)
        # return 

        # if we reach the end of the trie, or the end 
        # of a path on the trie, naturally any neighboring
        # letter will not be in the children of the current trieNode
        # and we return 

        # otherwise recurse on neighbors and the next 
        # letter in trie. 

        # if the root (the current node in trie) is end of word, 
        # add word_so_far to result list and mark node.end_of_word
        # as false, so if we encounter the same word again 
        # on a different path, we don't add a duplicate

        # the DFS inner function uses return to prune and stop recursion
        # if next block isn't in trie. 
        # It's only meant to accumulate words in result list

       

       