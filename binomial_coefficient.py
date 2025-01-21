def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

n, k = 5, 2
print(f"C({n}, {k}) =", binomial_coefficient(n, k))


'''
Binomial Coefficient Problem
Definition: Calculate combinations (n choose k), representing the number of ways to choose k items from n items.
Objective: Solve combinatorial problems like Pascal’s Triangle.
Diagram:
scss
Copy
Edit
C(5, 2) = 10
(Pascal’s Triangle)
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
'''