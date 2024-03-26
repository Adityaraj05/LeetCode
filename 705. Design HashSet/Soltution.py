# Here, ListNode represents a node in a linked list. Each node has a key attribute to store the value and a next attribute to point to the next node in the list.
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
# MyHashSet is a class representing a simple hash set implementation. In the constructor (__init__ method), it initializes a list named set containing 10**4 ListNode objects, each initialized with a key of 0.
class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range (10**4)]
    # The add method adds a key to the hash set. It calculates the index in the hash set array using modulo division. Then, it iterates through the linked list at that index until it finds the end of the list or a node with the same key. If it finds a node with the same key, it doesn't add it again. Otherwise, it adds a new node with the key to the end of the linked list.
    def add(self, key: int) -> None:
        index = key % len(self.set)
        current = self.set[index]
        while current.next:
            # Handling the duplicated 
            if current.next.key == key:
                return
            current = current.next
            # adding the key to the last of the lindkedlist
        current.next = ListNode(key)
        
    # The remove method removes a key from the hash set. It calculates the index, iterates through the linked list at that index, and if it finds a node with the given key, it removes it by bypassing it (setting the next pointer of the previous node to the node after the one being removed).
    def remove(self, key: int) -> None:
        index = key % len(self.set)
        current = self.set[index]
        while current.next:
            # if we find the key then change the pointer of the node to remove the key 
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        
#    The contains method checks whether a key exists in the hash set. It calculates the index, iterates through the linked list at that index, and returns True if it finds a node with the given key. Otherwise, it returns False after iterating through the entire linked list.
    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        current = self.set[index]
        while current.next:
            # if we find the key then change linkedlist then return the True
            if current.next.key == key:
                return True
            current = current.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
