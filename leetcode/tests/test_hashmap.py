from leetcode.hashmap.isomorphicSrings import Solution as isomorphicSrings_Solution
from leetcode.hashmap.ransomnote import Solution as ransomnote_Solution
from leetcode.hashmap.twoSum import Solution as twoSum_Solution
from leetcode.hashmap.validAnagram import Solution as validAnagram_Solution
from leetcode.hashmap.wordPattern import Solution as wordPattern_Solution
from leetcode.hashmap.happyNumber import Solution as happyNumber_Solution
from leetcode.hashmap.containsDuplicate import Solution as containsDuplicate_Solution
from leetcode.hashmap.groupAnagrams import Solution as groupAnagrams_Solution
from leetcode.hashmap.longestConsecutiveSequence import Solution as longestConsecutiveSequence_Solution

import pytest 

@pytest.mark.parametrize("s,t,expected", [
    ['egg', 'add', True],
    ['foo', 'bar', False],
    ['paper', 'title', True],
    ['ab', 'aa', False]
    ]
    )
def test_isomorphicSrings(s,t, expected):
    solution = isomorphicSrings_Solution()
    assert solution.isIsomorphic(s,t) == expected

@pytest.mark.parametrize("ransomNote,magazine,expected", [
    ['a', 'b', False],
    ['aa', 'ab', False],
    ['aa', 'aab', True]
    ]
    )
def test_ransomnote(ransomNote,magazine, expected):
    solution = ransomnote_Solution()
    assert solution.canConstruct(ransomNote,magazine) == expected

@pytest.mark.parametrize("nums,target,expected", [
    [[2, 7, 11, 15], 9, [1, 0]],
    [[3, 2, 4], 6, [2, 1]],
    [[3, 3], 6, [1, 0]]
    ]
    )
def test_twoSum(nums,target, expected):
    solution = twoSum_Solution()
    assert solution.twoSum(nums,target) == expected

@pytest.mark.parametrize("s,t,expected", [
    ['anagram', 'nagaram', True],
    ['rat', 'car', False]
    ]
    )
def test_validAnagram(s,t, expected):
    solution = validAnagram_Solution()
    assert solution.isAnagram(s,t) == expected

@pytest.mark.parametrize("pattern,s,expected", [
    ['abba', 'dog cat cat dog', True],
    ['abba', 'dog cat cat fish', False],
    ['aaaa', 'dog cat cat dog', False],
    ['abba', 'dog dog dog dog', False]
    ]
    )
def test_wordPattern(pattern,s, expected):
    solution = wordPattern_Solution()
    assert solution.wordPattern(pattern,s) == expected

@pytest.mark.parametrize("test_input,expected", [
    [19, True],
    [2, False],
    [1, True],
    [7, True]
    ]
    )
def test_happyNumber(test_input, expected):
    solution = happyNumber_Solution()
    assert solution.isHappy(test_input) == expected

@pytest.mark.parametrize("nums,k,expected", [
    [[1,2,3,1], 3, True],
    [[1,0,1,1], 1, True],
    [[1,2,3,1,2,3], 2, False]
    ]
    )
def test_containsDuplicate(nums,k, expected):
    solution = containsDuplicate_Solution()
    assert solution.containsNearbyDuplicate(nums,k) == expected

@pytest.mark.parametrize("test_input,expected", [
    [[""], [[""]]],
    [["a"], [["a"]]],
    [[""], [[""]]]    
    ]
    )
def test_groupAnagrams(test_input, expected):
    solution = groupAnagrams_Solution()
    assert solution.groupAnagrams(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    [[100, 4, 200, 1, 3, 2], 4],
    [[0, 0], 1],
    [[], 0],
    [[0,3,7,2,5,8,4,6,0,1], 9],
    [[9,1,4,7,3,-1,0,5,8,-1,6], 7]
    ]
    )
def test_longestConsecutiveSequence(test_input, expected):
    solution = longestConsecutiveSequence_Solution()
    assert solution.longestConsecutive(test_input) == expected
