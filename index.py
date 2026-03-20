from collections import OrderedDict
from typing import Any, Optional

class LRUCache:
    """
    A Least Recently Used (LRU) Cache implementation using an OrderedDict.
    Provides O(1) time complexity for both get and put operations.
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self._capacity = capacity
        self._cache: OrderedDict[Any, Any] = OrderedDict()

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieve an item from the cache by key.
        Returns None if the key is not found.
        """
        if key not in self._cache:
            return None
        
        # Move the accessed item to the end to mark it as most recently used
        self._cache.move_to_end(key)
        return self._cache[key]

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update an item in the cache.
        If the cache exceeds its capacity, the least recently used item is evicted.
        """
        if key in self._cache:
            self._cache.move_to_end(key)
        
        self._cache[key] = value
        
        if len(self._cache) > self._capacity:
            # popitem(last=False) removes the first item (least recently used)
            self._cache.popitem(last=False)

    def __len__(self) -> int:
        return len(self._cache)

    def clear(self) -> None:
        """Clear all items from the cache."""
        self._cache.clear()