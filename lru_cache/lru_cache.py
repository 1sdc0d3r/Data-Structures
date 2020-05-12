class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
# limit = 10

    def __init__(self, limit=10):
        self.storage = {}
        self.length = 0
        self.limit = limit
        self.head = None
        self.tail = None

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        prev_head = self.head
        if key in self.storage:
            current = self.head
            while current.next and list(current.value)[0] != key:
                current = current.next

            self.head = current
            self.head.next = prev_head
            prev_head.prev = self.head

            prev_current = current
            current.prev.next = current.next
            prev_current.next.prev = current.prev
            return list(self.head.value.values())[0]
        else:
            return False
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
        # self.cache[key] = value
    """

    def set(self, key, value):
        new_node = Node({key: value})
        prev_head = self.head

        if key in self.storage:
            self.storage[key] = value
            current = self.head
            while current.next and list(current.value)[0] != key:
                current = current.next
            # print("current", current.value)

            self.head = new_node
            self.head.next = prev_head
            prev_head.prev = self.head

            current.prev.next = current.next
            current.next.prev = current.prev

        elif not self.head:
            self.length += 1
            self.head = new_node
            self.tail = new_node
            self.storage[key] = value

        else:
            self.length += 1
            self.head = new_node
            self.head.next = prev_head
            prev_head.prev = new_node
            self.storage[key] = value
            if self.length > self.limit:
                del(self.storage[(list(self.tail.value)[0])])
                self.tail.prev.next = None
                self.tail = self.tail.prev


# newCache = LRUCache()
# newCache.set("Name1", "value1")
# newCache.set("Name2", "value2")
# newCache.set("Name3", "value3")
# newCache.set("Name4", "value4")
# newCache.set("Name5", "value5")
# newCache.set("Name6", "value6")
# newCache.set("Name7", "value7")
# newCache.set("Name8", "value8")
# newCache.set("Name6", "new6")
# print(newCache.storage)
# print(newCache.get("Name7"))
# print(newCache.head.value)
# newCache.get("Name5")
