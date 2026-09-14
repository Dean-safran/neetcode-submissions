class Node :
    def __init__(self, key=None, val=None, next=None, prev=None) :
        # val should be a key,value pair that's in cache
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_length = 0
        self.head = Node()
        self.tail = Node()
        self.keys = dict()

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        old_next = self.head.next

        node.prev = self.head
        node.next = old_next

        self.head.next = node
        old_next.prev = node

        return node
    
    def remove(self, node): 
        node.prev.next = node.next
        node.next.prev = node.prev

        return node


    def get(self, key: int) -> int:
        if key in self.keys :
            node = self.keys[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys :
            node = self.keys[key]
            self.remove(node)
            self.insert(node)
            node.val = value
            return 
        else : 
            node = Node(key,value)
            self.insert(node)
            self.keys[key] = node
            self.cache_length += 1
        
        if self.cache_length > self.capacity :
            to_remove = self.tail.prev
            self.remove(to_remove)
            del self.keys[to_remove.key]

        return