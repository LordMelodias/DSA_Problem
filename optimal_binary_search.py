def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = min((dp[i][k - 1] if k > i else 0) + 
                           (dp[k + 1][j] if k < j else 0) +
                           sum(freq[i:j + 1]) for k in range(i, j + 1))
    return dp[0][n - 1]

keys = [10, 20, 30]
freq = [3, 2, 1]
print("Optimal BST cost:", optimal_bst(keys, freq))


'''
Optimal Binary Search Tree
Definition: Constructs a BST such that the cost of searching keys is minimized, given their frequencies.
Objective: Minimize the search cost based on key frequency.
Diagram:
Keys: [10, 20, 30]
Frequencies: [3, 2, 1]
Solution: Root = 20 (minimizes cost)
'''