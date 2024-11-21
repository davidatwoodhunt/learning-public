import pytest
from leetcode.linked_list.lru_cache import LRUCache as lru_cache_Solution

@pytest.mark.parametrize("capacity, operations, arguments, expected", [
    # Test case 1: Basic functionality
    (2, ["put", "put", "get", "put", "get", "put", "get", "get"], 
        [(1, 1), (2, 2), (1,), (3, 3), (2,), (4, 4), (1,), (3, 3)], 
        [None, None, 1, None, -1, None, -1, 3, 4]),
    
    # Test case 2: Overwrite existing key
    (2, ["put", "put", "put", "get", "put", "get", "get"],
        [(1, 1), (2, 2), (1, 10), (1,), (3, 3), (2,), (1,)],
        [None, None, None, 10, None, -1, 10]),
])
def test_lru_cache(capacity, operations, arguments, expected):
    solution = lru_cache_Solution(capacity)
    for op, arg, exp in zip(operations, arguments, expected):
        if op == "put":
            solution.put(*arg)
        elif op == "get":
            assert solution.get(arg[0]) == exp
