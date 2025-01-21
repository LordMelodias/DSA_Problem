def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    print("what is items: ", items)
    total_value = 0
    for w, v in items:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += v * (capacity / w)
            break
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value:", fractional_knapsack(weights, values, capacity))


'''
Fractional Knapsack Problem:
Definition: A greedy algorithm to maximize the total value of items that can fit into a knapsack of fixed capacity by taking fractions of items if necessary.

Objective: Maximize the total value within the given weight capacity.

Example:
Items: (Weight, Value) = [(10, 60), (20, 100), (30, 120)]
Capacity = 50
Solution: Take 20 (100%) of item 1, 20 (100%) of item 2, and (50%) of item 3.
'''