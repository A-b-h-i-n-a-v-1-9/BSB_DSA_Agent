import random
from datetime import datetime

# --- Topic Sequence ---
TOPIC_SEQUENCE = [
    "arrays", "strings", "linked list", "stack", "queue",
    "hash table", "recursion", "binary search", "sorting",
    "heap/priority queue", "tree", "graph", "dynamic programming",
    "backtracking", "greedy", "trie"
]

# --- Hardcoded LeetCode Problems ---
LEETCODE_PROBLEMS = {
    "arrays": [
        ("Two Sum", "https://leetcode.com/problems/two-sum/"),
        ("Best Time to Buy and Sell Stock", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"),
        ("Contains Duplicate", "https://leetcode.com/problems/contains-duplicate/"),
        ("Product of Array Except Self", "https://leetcode.com/problems/product-of-array-except-self/"),
        ("Maximum Subarray", "https://leetcode.com/problems/maximum-subarray/"),
        ("Maximum Product Subarray", "https://leetcode.com/problems/maximum-product-subarray/"),
        ("Find Minimum in Rotated Sorted Array", "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"),
        ("Search in Rotated Sorted Array", "https://leetcode.com/problems/search-in-rotated-sorted-array/"),
        ("3Sum", "https://leetcode.com/problems/3sum/"),
        ("Container With Most Water", "https://leetcode.com/problems/container-with-most-water/")
    ],
    "strings": [
        ("Valid Anagram", "https://leetcode.com/problems/valid-anagram/"),
        ("Longest Substring Without Repeating Characters", "https://leetcode.com/problems/longest-substring-without-repeating-characters/"),
        ("Palindrome Permutation", "https://leetcode.com/problems/palindrome-permutation/"),
        ("Group Anagrams", "https://leetcode.com/problems/group-anagrams/"),
        ("Valid Parentheses", "https://leetcode.com/problems/valid-parentheses/"),
        ("Longest Palindromic Substring", "https://leetcode.com/problems/longest-palindromic-substring/"),
        ("String to Integer (atoi)", "https://leetcode.com/problems/string-to-integer-atoi/"),
        ("Implement strStr()", "https://leetcode.com/problems/implement-strstr/"),
        ("Count and Say", "https://leetcode.com/problems/count-and-say/"),
        ("Simplify Path", "https://leetcode.com/problems/simplify-path/")
    ],
    "linked list": [
        ("Reverse Linked List", "https://leetcode.com/problems/reverse-linked-list/"),
        ("Merge Two Sorted Lists", "https://leetcode.com/problems/merge-two-sorted-lists/"),
        ("Add Two Numbers", "https://leetcode.com/problems/add-two-numbers/"),
        ("Remove Nth Node From End of List", "https://leetcode.com/problems/remove-nth-node-from-end-of-list/"),
        ("Linked List Cycle", "https://leetcode.com/problems/linked-list-cycle/"),
        ("Intersection of Two Linked Lists", "https://leetcode.com/problems/intersection-of-two-linked-lists/"),
        ("Palindrome Linked List", "https://leetcode.com/problems/palindrome-linked-list/"),
        ("Reorder List", "https://leetcode.com/problems/reorder-list/"),
        ("Flatten a Multilevel Doubly Linked List", "https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/"),
        ("Copy List with Random Pointer", "https://leetcode.com/problems/copy-list-with-random-pointer/")
    ],
    "stack": [
        ("Min Stack", "https://leetcode.com/problems/min-stack/"),
        ("Evaluate Reverse Polish Notation", "https://leetcode.com/problems/evaluate-reverse-polish-notation/"),
        ("Largest Rectangle in Histogram", "https://leetcode.com/problems/largest-rectangle-in-histogram/"),
        ("Sliding Window Maximum", "https://leetcode.com/problems/sliding-window-maximum/"),
        ("Decode String", "https://leetcode.com/problems/decode-string/"),
        ("Basic Calculator II", "https://leetcode.com/problems/basic-calculator-ii/")
    ],
    "queue": [
        ("Implement Queue using Stacks", "https://leetcode.com/problems/implement-queue-using-stacks/"),
        ("Implement Stack using Queues", "https://leetcode.com/problems/implement-stack-using-queues/"),
        ("Rotting Oranges", "https://leetcode.com/problems/rotting-oranges/"),
        ("Design Hit Counter", "https://leetcode.com/problems/design-hit-counter/"),
        ("Sliding Puzzle", "https://leetcode.com/problems/sliding-puzzle/")
    ],
    "tree": [
        ("Maximum Depth of Binary Tree", "https://leetcode.com/problems/maximum-depth-of-binary-tree/"),
        ("Symmetric Tree", "https://leetcode.com/problems/symmetric-tree/"),
        ("Binary Tree Level Order Traversal", "https://leetcode.com/problems/binary-tree-level-order-traversal/"),
        ("Convert Sorted Array to Binary Search Tree", "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/"),
        ("Validate Binary Search Tree", "https://leetcode.com/problems/validate-binary-search-tree/"),
        ("Binary Tree Inorder Traversal", "https://leetcode.com/problems/binary-tree-inorder-traversal/"),
        ("Binary Tree Preorder Traversal", "https://leetcode.com/problems/binary-tree-preorder-traversal/"),
        ("Binary Tree Postorder Traversal", "https://leetcode.com/problems/binary-tree-postorder-traversal/"),
        ("Path Sum", "https://leetcode.com/problems/path-sum/"),
        ("Flatten Binary Tree to Linked List", "https://leetcode.com/problems/flatten-binary-tree-to-linked-list/")
    ],
    "graph": [
        ("Number of Islands", "https://leetcode.com/problems/number-of-islands/"),
        ("Course Schedule", "https://leetcode.com/problems/course-schedule/"),
        ("Clone Graph", "https://leetcode.com/problems/clone-graph/"),
        ("Minimum Height Trees", "https://leetcode.com/problems/minimum-height-trees/"),
        ("Graph Valid Tree", "https://leetcode.com/problems/graph-valid-tree/")
    ],
    "dynamic programming": [
        ("Coin Change", "https://leetcode.com/problems/coin-change/"),
        ("Climbing Stairs", "https://leetcode.com/problems/climbing-stairs/"),
        ("Longest Increasing Subsequence", "https://leetcode.com/problems/longest-increasing-subsequence/"),
        ("House Robber", "https://leetcode.com/problems/house-robber/"),
        ("Maximum Subarray", "https://leetcode.com/problems/maximum-subarray/"),
        ("Unique Paths", "https://leetcode.com/problems/unique-paths/"),
        ("Word Break", "https://leetcode.com/problems/word-break/"),
        ("Minimum Path Sum", "https://leetcode.com/problems/minimum-path-sum/"),
        ("Decode Ways", "https://leetcode.com/problems/decode-ways/"),
        ("Edit Distance", "https://leetcode.com/problems/edit-distance/")
    ],
    "backtracking": [
        ("N-Queens", "https://leetcode.com/problems/n-queens/"),
        ("Sudoku Solver", "https://leetcode.com/problems/sudoku-solver/"),
        ("Word Search", "https://leetcode.com/problems/word-search/"),
        ("Combination Sum", "https://leetcode.com/problems/combination-sum/"),
        ("Palindrome Partitioning", "https://leetcode.com/problems/palindrome-partitioning/")
    ],
    "greedy": [
        ("Jump Game", "https://leetcode.com/problems/jump-game/"),
        ("Gas Station", "https://leetcode.com/problems/gas-station/"),
        ("Queue Reconstruction by Height", "https://leetcode.com/problems/queue-reconstruction-by-height/"),
        ("Task Scheduler", "https://leetcode.com/problems/task-scheduler/"),
        ("Lemonade Change", "https://leetcode.com/problems/lemonade-change/")
    ],
    "trie": [
        ("Implement Trie", "https://leetcode.com/problems/implement-trie-prefix-tree/"),
        ("Add and Search Word - Data structure design", "https://leetcode.com/problems/add-and-search-word-data-structure-design/"),
        ("Word Search II", "https://leetcode.com/problems/word-search-ii/"),
        ("Replace Words", "https://leetcode.com/problems/replace-words/"),
        ("Longest Word in Dictionary", "https://leetcode.com/problems/longest-word-in-dictionary/")
    ]
}

# --- Helper to get problems for a topic ---
def get_leetcode_links_for_topic(topic):
    return LEETCODE_PROBLEMS.get(topic, [])

# --- Adaptive topic-based recommendation ---
def recommend_next_problems(progress_data, topic_sequence=TOPIC_SEQUENCE):
    if progress_data.get("weak_topics"):
        next_topic = progress_data["weak_topics"][0]
    else:
        for t in topic_sequence:
            if t not in progress_data.get("solved", []):
                next_topic = t
                break
        else:
            next_topic = topic_sequence[0]

    links = get_leetcode_links_for_topic(next_topic)
    return next_topic, links

# --- Legacy function for "Recommend Problem" button ---
def recommend_problem(progress_data):
    if progress_data.get("weak_topics"):
        topic = random.choice(progress_data["weak_topics"])
    else:
        topic = random.choice(TOPIC_SEQUENCE)

    problems = get_leetcode_links_for_topic(topic)
    if problems:
        title, url = random.choice(problems)
        return f"{title}: {url}"
    return "No problem available"
