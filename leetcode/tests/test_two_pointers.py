import pytest
from leetcode.two_pointers.is_subsequence import Solution as is_subsequence_Solution
from leetcode.two_pointers.valid_palindrome import Solution as valid_palindrome_Solution

@pytest.mark.parametrize("s, t, expected", [
    ('abc', 'ahbgdc', True),
    ('axc', 'ahbgdc', False),
    ('', 'ahbgdc', True),         # Edge case: empty `s`
    ('abc', '', False),           # Edge case: empty `t`
    ('abc', 'abc', True)          # Exact match
])
def test_is_subsequence(s, t, expected):
    solution = is_subsequence_Solution()
    assert solution.isSubsequence(s, t) == expected

@pytest.mark.parametrize("s, expected", [
    ("Kayak", True),
    ("A man, a plan, a canal: Panama", True),
    ("racecar", True),
    ("hello", False),
    ("", True),                   # Edge case: empty string
    (" ", True),                  # Edge case: single space
    ("12321", True),              # Numeric palindrome
    ("No lemon, no melon", True)  # Phrase palindrome with spaces and punctuation
])
def test_valid_palindrome(s, expected):
    solution = valid_palindrome_Solution()
    assert solution.isPalindrome(s) == expected
