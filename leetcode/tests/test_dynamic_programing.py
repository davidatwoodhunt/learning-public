from leetcode.dynamic_programming.climbing_stairs import Solution as climbing_stairs_Solution
from leetcode.dynamic_programming.house_robber import Solution as house_robber_Solution
from leetcode.dynamic_programming.word_break import Solution as word_break_Solution
from leetcode.dynamic_programming.coin_change import Solution as coin_change_Solution
from leetcode.dynamic_programming.longest_increasing_subsequence import Solution as longest_increasing_subsequence_Solution
from leetcode.dynamic_programming.traingle import Solution as traingle_Solution
from leetcode.dynamic_programming.minimum_path_sum import Solution as minimum_path_sum_Solution
from leetcode.dynamic_programming.knapsack import Solution as knapsack_Solution
from leetcode.dynamic_programming.longest_common_subsequence import Solution as longest_common_subsequence_Solution
from leetcode.dynamic_programming.subset_sum import Solution as subset_sum_Solution
from leetcode.dynamic_programming.minimum_edit_distance import Solution as minimum_edit_distance_Solution
from leetcode.dynamic_programming.minimum_path_sum import Solution as minimum_path_sum_Solution
import pytest 
import ast 

@pytest.mark.parametrize("test_input,expected", [
    [2, 2],
    [3, 3],
    [4, 5],
    [5, 8],
    [6, 13],
    [7, 21],
    [8, 34],
    [9, 55],
    [10, 89],
    [11, 144],
    [12, 233],
    [13, 377],
    [14, 610],
    [15, 987],
    [16, 1597],
    [17, 2584],
    [18, 4181],
    [19, 6765],
    [20, 10946],
    [21, 17711],
    [22, 28657],
    [23, 46368],
    [24, 75025],
    [25, 121393],
    [26, 196418],
    [27, 317811],
    [28, 514229],
    [29, 832040],
    [30, 1346269],
    [31, 2178309],
    [32, 3524578],
    [33, 5702887],
    [34, 9227465],
    [35, 14930352],
    [36, 24157817],
    [37, 39088169],
    [38, 63245986],
    [39, 102334155],
    [40, 165580141],
    [41, 267914296],
    [42, 433494437],
    [43, 701408733],
    [44, 1134903170],
    [45, 1836311903]
    ]
    )
def test_climbing_stairs(test_input, expected):
    solution = climbing_stairs_Solution()
    assert solution.climbStairs(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    [[1,2,3,1], 4],
    [[2,7,9,3,1], 12],
    [[2,1,1,2], 4],
    [[2,3,2], 4],
    [[1,2,3,1,1,2], 6],
    [[2,7,9,3,1,1,2], 14],
    [[2,1,1,2,1,2], 6],
    [[2,3,2,1,2], 6],
    [[1,2,3,1,1,2,1,2], 8],
    [[2,7,9,3,1,1,2,1,2], 16],
    [[2,1,1,2,1,2,1,2], 8],
    [[2,3,2,1,2,1,2], 8],
    [[1,2,3,1,1,2,1,2,1,2], 10],
    [[2,7,9,3,1,1,2,1,2,1,2], 18]
    ]
    )
def test_house_robber(test_input, expected):
    solution = house_robber_Solution()
    assert solution.rob(test_input) == expected

@pytest.mark.parametrize("test_input,word_dict,expected", [
    ["leetcode", ["leet","code"], True],
    ["applepenapple", ["apple","pen"], True],
    ["catsandog", ["cats","dog","sand","and","cat"], False],
    ["catsanddog", ["cats","dog","sand","and","cat"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand","cats","anddog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand","cats","anddog","sand","dog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand","cats","anddog","sand","dog","catsanddog","catsand","cats","anddog","sand","dog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand","cats","anddog","sand","dog","catsanddog","catsand","cats","anddog","sand","dog","catsanddog","catsand","cats","anddog","sand","dog"], True]
    ]
    )
def test_word_break(test_input, word_dict, expected):
    solution = word_break_Solution()
    assert solution.wordBreak(test_input, word_dict) == expected

@pytest.mark.parametrize("test_input,word_dict,expected", [
    ["leetcode", ["leet","code"], True],
    ["applepenapple", ["apple","pen"], True],
    ["catsandog", ["cats","dog","sand","and","cat"], False],
    ["catsanddog", ["cats","dog","sand","and","cat"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand","cats","anddog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand","cats","anddog","sand","dog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand","cats","anddog","sand","dog","catsanddog","catsand","cats","anddog","sand","dog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sanddog","catsanddog","catsand","cats","anddog","sand","dog","catsanddog","catsand","cats","anddog","sand","dog","catsanddog","catsand","cats","anddog","sand","dog"], True],
    ["catsanddog", ["cats","dog","sand","and","cat","sand","catsanddog","catsand","cats","anddog","sand","dog","catsanddog","catsand","cats","anddog","sand","dog","catsanddog","catsand","cats","anddog","sand","dog"], True],
])
def test_word_break_2(test_input, word_dict, expected):
    solution = word_break_Solution()
    assert solution.wordBreak(test_input, word_dict) == expected


@pytest.mark.parametrize("test_input,expected", [
    ["fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami", False]
    ]
    )
def test_word_break_2(test_input, expected):
    with open('leetcode/tests/data/sliding_window_minSubarrayLen_12_input.txt', 'r') as file:
        word_dict = file.read().replace('[', '').replace(']', '').replace(' ', '').split(',')
    solution = word_break_Solution()
    assert solution.wordBreak(test_input, word_dict) == expected

@pytest.mark.parametrize("coins,amount,expected", [
    [[1,2,5], 11, 3],
    [[2], 3, -1],
    [[1], 0, 0],
    [[1], 1, 1],
    [[1], 2, 2],
    [[1,2], 2, 1],
    [[1,2], 3, 2],
    [[1,2,3], 3, 1],
    [[1,2,3], 4, 2],
    [[1,2,3], 5, 2],
    [[1,2,3], 6, 2]
    ]
    )
def test_coin_change(coins,amount, expected):
    solution = coin_change_Solution()
    assert solution.coinChange(coins,amount) == expected


@pytest.mark.parametrize("nums,expected", [
    [[10,9,2,5,3,7,101,18], 4],
    [[0,1,0,3,2,3], 4],
    [[7,7,7,7,7,7,7], 1]
    ]
    )
def test_longest_increasing_subsequence(nums, expected):
    solution = longest_increasing_subsequence_Solution()
    assert solution.lengthOfLIS(nums) == expected

@pytest.mark.parametrize("test_input,expected", [
    ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
    ([[-10]], -10),
    ([[1],[2,3]], 3),
    ([[1],[2,3],[4,5,6]], 7),
    ([[1],[2,3],[4,5,6],[7,8,9,10]], 14)
])
def test_traingle_recursive(test_input, expected):
    solution = traingle_Solution()
    assert solution.minimumTotal_recursive(test_input) == expected

@pytest.mark.parametrize("fpath,expected", [
    ('leetcode/tests/data/triangle_dp_1.txt', 0),
])
def test_recursive_triangle_from_file(fpath,expected):
    with open(fpath, 'r') as file:
        test_input = file.read()
    solution = traingle_Solution()
    test_input = ast.literal_eval(test_input)
    assert solution.minimumTotal_recursive(test_input) == expected

#test iterative triangle
@pytest.mark.parametrize("test_input,expected", [
    ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
    ([[-10]], -10),
    ([[1],[2,3]], 3),
    ([[1],[2,3],[4,5,6]], 7),
    ([[1],[2,3],[4,5,6],[7,8,9,10]], 14)
])
def test_traingle_iterative(test_input, expected):
    solution = traingle_Solution()
    assert solution.minimumTotal_iterative(test_input) == expected

@pytest.mark.parametrize("fpath,expected", [
    ('leetcode/tests/data/triangle_dp_1.txt', 0),
])
def test_iterative_triangle_from_file(fpath,expected):
    with open(fpath, 'r') as file:
        test_input = file.read()
    solution = traingle_Solution()
    test_input = ast.literal_eval(test_input)
    assert solution.minimumTotal_iterative(test_input) == expected


#minimum Path sum 
@pytest.mark.skip('pass for now')
@pytest.mark.parametrize("test_input,expected", [
    ([[1,3,1],[1,5,1],[4,2,1]], 7),
    ([[1,2,3],[4,5,6],[7,8,9]], 21),
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 34),
    ([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 65),
    ([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]], 111),
    ([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42],[43,44,45,46,47,48,49]], 175),
    ([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16],[17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32],[33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48],[49,50,51,52,53,54,55,56],[57,58,59,60,61,62,63,64]], 260)
])
def test_minimum_path_sum(test_input, expected):
    solution = minimum_path_sum_Solution()
    assert solution.minPathSum(test_input) == expected
    

## KnapSack
@pytest.mark.parametrize(
    "values, weights, capacity, expected",
    [
        ([60, 100, 120], [10, 20, 30], 50, 220),  # Standard test case
        ([10, 40, 30, 50], [5, 4, 6, 3], 10, 90),  # Another case with different values and weights
        ([20, 50, 30], [10, 20, 30], 0, 0),  # Case where capacity is 0
        ([100], [50], 50, 100),  # Case with one item that exactly fits
        ([10, 20, 30], [1, 2, 3], 5, 50),  # Case where you can fit multiple items
        ([], [], 10, 0),  # Case with no items
        ([70, 80, 90], [10, 20, 30], 10, 70),  # Case where only one item can fit
    ]
)
def test_knapsack(values, weights, capacity, expected):
    solution = knapsack_Solution()
    assert solution.knapsack(values, weights, capacity) == expected

# Longest common subsequence
@pytest.mark.parametrize(
    "text1, text2, expected",
    [
        ("abcde", "ace", 3),  # Standard test case
        ("abc", "abc", 3),  # Case where both strings are the same
        ("abc", "def", 0),  # Case where strings have no common subsequence
        ("abc", "", 0),  # Case where one string is empty
        ("", "abc", 0),  # Case where one string is empty
        ("abcde", "ace", 3),  # Case where the common subsequence is at the end
        ("abcde", "aec", 2),  # Case where the common subsequence is in the middle
        ("abcde", "b", 1),  # Case where the common subsequence is one character
        ("abcde", "f", 0),  # Case where there is no common subsequence
    ]
)
def test_longest_common_subsequence(text1, text2, expected):
    solution = longest_common_subsequence_Solution()
    assert solution.longestCommonSubsequence(text1, text2) == expected


#subset sum 
@pytest.mark.parametrize(
        "nums, target, expected",
    [
        ([2,3,7,8,10], 11, True),  # Standard test case
        ([2,3,7,8,10], 12, True),  # Standard test case
        ([2,3,7,8,10], 13, True),  # Standard test case
        ([2,3,7,8,10], 14, False),  # Standard test case
        ([2,3,7,8,10], 15, True),  # Standard test case
        ([2,3,7,8,10], 16, False),  # Standard test case

    ])
def test_subset_sum(nums, target, expected):
    solution = subset_sum_Solution()
    assert solution.canPartition(nums, target) == expected

#minimum edit distance
@pytest.mark.parametrize(
        "word1, word2, expected",
    [
        ("horse", "ros", 3),  # Standard test case
        ("intention", "execution", 5),  # Standard test case
        ('abcdef', 'azced', 3)
    ])
def test_minimum_edit_distance(word1, word2, expected):
    solution = minimum_edit_distance_Solution()
    assert solution.minDistance(word1, word2) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),  # Standard 3x3 grid, path: 1 -> 3 -> 1 -> 1 -> 1
        ([[1]], 1),                              # Single element grid
        ([[1, 2], [1, 1]], 3),                   # Simple 2x2 grid, path: 1 -> 1 -> 1
        ([[5, 9, 1], [3, 7, 1], [2, 1, 1]], 12), # Complex 3x3 grid
    ]
)
def test_minPathSum_recursive(grid, expected):
    solution = minimum_path_sum_Solution()
    assert solution.minPathSum(grid) == expected

#matrix chain multiplication
@pytest.mark.skip
@pytest.mark.parametrize(
        "arr, expected",
    [
        ([1, 2, 3, 4], 18),  # Standard test case
        ([1, 2, 3, 4, 5], 38),  # Standard test case
        ([1, 2, 3, 4, 5, 6], 88),  # Standard test case
        ([1, 2, 3, 4, 5, 6, 7], 168),  # Standard test case
        ([1, 2, 3, 4, 5, 6, 7, 8], 288),  # Standard test case
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 448),  # Standard test case
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 648),  # Standard test case
    ])

def test_matrix_chain_multiplication(arr, expected):
    solution = matrix_chain_multiplication_Solution()
    assert solution.matrixChainOrder(arr) == expected