class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}  

        self.left = Node(0, 0)   # Least Recently Used side
        self.right = Node(0, 0)  # Most Recently Used side

        self.left.next = self.right
        self.right.prev = self.left

    # Removing a Node from the list
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert a node right before the tail (MRU position)
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to MRU position
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node and insert it
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # If capacity exceeded, remove LRU
        if len(self.cache) > self.cap:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]
        
