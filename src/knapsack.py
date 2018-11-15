# knapsack


def knapsack(max_weight, num_items, weights, values):
    """
    Solves the single dimension, 0-1, knapsack problem using dynamic programming.
    """
    assert len(weights) == len(values)
    assert num_items == len(weights)
    assert type(max_weight) is IntType

    knapsack = [[0 for x in range(max_weight + 1)] for x in range(num_items+1)] 
    # indices of items used
    knapsack_items = [[[] for x in range(max_weight + 1)] for x in range(num_items+1)]

    # Build table knapsack[][], in bottom up manner 
    for i in range(num_items+1):
        for w in range(maxweight+1): 
            if i==0 or w==0: 
                knapsack[i][w] = 0
            elif weights[i-1] <= w: 
                prev_subset_val = knapsack[i-1][w]
                new_subset_val = values[i-1] + knapsack[i-1][w-weights[i-1]]
                if new_subset > prev_subset:
                    knapsack[i][w] = new_subset_val
                    knapsack_items[i][w] = knapsack_items[i-1][w-weights[i-1]].append(i-1)
                else:
                    knapsack[i][w] = prev_subset_val
                    knapsack_items[i][w] = knapsack_items[i-1][w]
            else: 
                knapsack[i][w] = knapsack[i-1][w] 
                knapsack_items[i][w] = knapsack_items[i-1][w]
  
    return knapsack[n][W], knapsack_items[n][W]