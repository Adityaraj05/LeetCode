
class LRUCache:

    def __init__(self, capacity: int):
        # This line sets the capacity of the cache to the provided capacity.
        self.capacity = capacity
        # This line initializes an empty dictionary to store key-value pairs. This dictionary will serve as the cache.
        self.dict = {}
    #  This method is used to retrieve a value from the cache corresponding to the given key.
    def get(self, key: int) -> int:
        # This line checks if the key exists in the cache.
        if key in self.dict.keys():
            # This line retrieves the value corresponding to the key.
            val = self.dict[key]
            #  This line deletes the key-value pair from the dictionary.
            del self.dict[key]
            # his line adds the key-value pair back to the dictionary, effectively updating its position in the cache.
            self.dict[key] = val
            # This line returns the value corresponding to the key if it exists in the cache, otherwise it returns -1.
            return val
        else:
            return -1
    # This method is used to insert or update a key-value pair in the cache.
    def put(self, key: int, value: int) -> None:
        #  This line checks if the key already exists in the cache.
        if key in self.dict.keys():
            # This line deletes the key-value pair from the dictionary.
            del self.dict[key]
            # This line adds the key-value pair back to the dictionary with the updated value.
            self.dict[key] = value
            # If the key doesn't exist in the cache,
        else:
            # his line checks if the cache has reached its maximum capacity.
            if len(self.dict) < self.capacity:
                # This line adds the key-value pair to the dictionary.
                self.dict[key] = value
                # If the cache is full,
            else:
                # This line deletes the oldest key-value pair from the dictionary (i.e., the first key-value pair in the dictionary).
                del self.dict[list(self.dict)[0]]
                # This line adds the new key-value pair to the dictionary.
                self.dict[key] = value
                
