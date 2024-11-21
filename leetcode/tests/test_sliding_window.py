import pytest
from leetcode.sliding_window.minimum_size_subarray_sum import Solution as minSubArrayLen_Solution

@pytest.mark.parametrize("target, nums, expected", [
    (7, [2,3,1,2,4,3], 2),
    (4, [1,4,4], 1),
    (11, [1,1,1,1,1,1,1,1], 0),
    (11, [1,2,3,4,5], 3),
    (15, [1,2,3,4,5], 5),
    (11, [1,2,3,4,5,6,7,8,9,10], 2),
    (11, [1,2,3,4,5,6,7,8,9,10,11], 1),
    (11, [1,2,3,4,5,6,7,8,9,10,11,12], 1),
    (11, [1,2,3,4,5,6,7,8,9,10,11,12,13], 1),
    (11, [1,2,3,4,5,6,7,8,9,10,11,12,13,14], 1),
    (213, [12,28,83,4,25,26,25,2,25,25,25,12], 8),
])
def test_minSubArrayLen(target, nums, expected):
    solution = minSubArrayLen_Solution()
    assert solution.minSubArrayLen(target, nums) == expected

@pytest.mark.parametrize("file_path, target, expected", [
    ('leetcode/tests/data/sliding_window_minSubarrayLen_12_input.txt', 396893380, 79517)
])
def test_minSubArrayLen_from_file(file_path, target, expected):
    solution = minSubArrayLen_Solution()
    with open(file_path, 'r') as file:
        nums = file.read().replace('[', '').replace(']', '').replace(' ', '').split(',')
    nums = list(map(int, nums))
    assert solution.minSubArrayLen(target, nums) == expected
