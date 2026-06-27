"""
This problem is saying "we're sorting words in alphabetical order, 
but we're making up our own order, return the order"
"""

"""
Create adjacency list in the form of a map {str : list[str]}
Create incoming edge map {str : int}
I think topological sort is needed here

We need a compare function to find the first pair
of letters that differ from each word

add all letters of both words to adj list with no adjancencies,
if they aren't already in map, and add to incEdge map if not 
already there with value 0

we'd call compare(smaller_word, larger_word), it returns a tuple, 
(smaller_letter, larger_letter), we create an edge from smaller letter 
to larger letter
by adding larger letter to neighbors of smaller letter, inc larger 
letter incEdge value by 1 

after all words have been compared, run topological sort on
adjList and incEdge map, adding letters in topological order
"""
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1 :
            return words[0]
        def compare(word1, word2) :
            pointer = 0
            while pointer < len(word1) and pointer < len(word2) :
                if word1[pointer] != word2[pointer] :
                    return (word1[pointer], word2[pointer])
                pointer += 1
            if len(word1) < len(word2) :
                if word1[len(word1) - 1] != word2[pointer] :
                    return (word1[len(word1) - 1], word2[pointer])
                return ("continue", "continue")
            if len(word1) == len(word2) :
                return ("continue", "continue")
            return ("", "")
        
        #connecting edges

        incEdge = {}
        adjList = {}

        for i in range(len(words) - 1) :
            word1 = words[i]
            word2 = words[i+1]

            for ch in word1 : 
                if ch not in adjList :
                    adjList[ch] = []
                    incEdge[ch] = 0
            for ch in word2 : 
                if ch not in adjList :
                    adjList[ch] = []
                    incEdge[ch] = 0
            smaller_ch, larger_ch = compare(word1, word2)
            if smaller_ch == "continue" : 
                continue
            if smaller_ch == "" :
                return ""
            adjList[smaller_ch] += [larger_ch]
            incEdge[larger_ch] += 1
        
        #topological sort 

        queue = deque()
        result = ""

        for ch in incEdge : 
            if incEdge[ch] == 0 :
                queue.append(ch)
        
        while queue :
            curr = queue.popleft()
            for neighbor in adjList[curr] :
                incEdge[neighbor] -= 1
                if incEdge[neighbor] == 0:
                    queue.append(neighbor)
            result += curr
            del adjList[curr]

        if adjList :
            return ""
        else :
            return result
            
            



        