def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    print("What is n: ", n) 
    dp = [[0] * n for _ in range(n)]    # Table to store minimum costs
    print("DP: ", dp)
    
    # l is the length of the chain being considered
    for l in range(2, n + 1):       # Chain lengths from 2 to n
        for i in range(n - l + 1):  # Starting index of the chain
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], q)
    return dp[0][n - 1]

p = [1, 2, 3, 4]
print("Minimum multiplication cost:", matrix_chain_order(p))


'''
Chained Matrix Multiplication
Definition: A dynamic programming approach to find the most efficient way to multiply matrices.
Objective: Minimize the total number of scalar multiplications.

Diagram:

Matrices: A(10x20), B(20x30), C(30x40)
Solution: Group as (A*B)*C or A*(B*C)
'''