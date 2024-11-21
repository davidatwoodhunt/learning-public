import pytest
from leetcode.array_string.bestTimeToBuyAndSellStock_I import Solution as bestTimeToBuyAndSellStock_I_Solution
from leetcode.array_string.firstOcurrance import Solution as firstOcurrance_Solution
from leetcode.array_string.longestCommonPrefix import Solution as longestCommonPrefix_Solution
from leetcode.array_string.partition import Solution as partition_Solution
from leetcode.array_string.removeDuplicate import Solution as removeDuplicate_Solution
from leetcode.array_string.removeDuplicates_II import Solution as removeDuplicates_II_Solution
from leetcode.array_string.removeElement import Solution as removeElement_Solution
from leetcode.array_string.rotate_array import Solution as rotateArray_Solution
from leetcode.array_string.romanToInteger import Solution as romanToInteger_Solution
from leetcode.array_string.zigzag import Solution as zigzag_Solution


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0)
])
def test_bestTimeToBuyAndSellStock_I(prices, expected):
    solution = bestTimeToBuyAndSellStock_I_Solution()
    assert solution.maxProfit(prices) == expected


@pytest.mark.parametrize("haystack, needle, expected", [
    ('sadbutsad', 'sad', 0),
    ('leetcode', 'leeto', -1)
])
def test_firstOcurrance(haystack, needle, expected):
    solution = firstOcurrance_Solution()
    assert solution.firstOcurrance(haystack, needle) == expected


@pytest.mark.parametrize("strs, expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], "")
])
def test_longestCommonPrefix(strs, expected):
    solution = longestCommonPrefix_Solution()
    assert solution.longestCommonPrefix(strs) == expected


@pytest.mark.parametrize("s, expected", [
    ("aab", [['a', 'a', 'b'], ['aa', 'b']])
])
def test_partition(s, expected):
    solution = partition_Solution()
    assert solution.partition(s) == expected


@pytest.mark.parametrize("nums, expected_length", [
    ([1, 1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
])
def test_removeDuplicate(nums, expected_length):
    solution = removeDuplicate_Solution()
    assert solution.removeDuplicates(nums) == expected_length


@pytest.mark.parametrize("nums, expected_length", [
    ([1, 1, 1, 2, 2, 3], 5),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7)
])
def test_removeDuplicates_II(nums, expected_length):
    solution = removeDuplicates_II_Solution()
    assert solution.removeDuplicates(nums) == expected_length


@pytest.mark.parametrize("nums, val, expected_length", [
    ([3, 2, 2, 3], 3, 2)
])
def test_removeElement(nums, val, expected_length):
    solution = removeElement_Solution()
    assert solution.removeElement(nums, val) == expected_length


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
])
def test_rotateArray(nums, k, expected):
    solution = rotateArray_Solution()
    solution.rotate(nums, k)
    assert nums == expected


@pytest.mark.parametrize("s, expected", [
    ('III', 3),
    ('IV', 4),
    ('IX', 9),
    ('LVIII', 58),
    ('MCMXCIV', 1994),
    ('MMMCMXCIX', 3999)
])
def test_romanToInteger(s, expected):
    solution = romanToInteger_Solution()
    assert solution.romanToInt(s) == expected


@pytest.mark.parametrize("s, numRows, expected", [
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI')
])
def test_zigzag(s, numRows, expected):
    solution = zigzag_Solution()
    assert solution.convert(s, numRows) == expected
