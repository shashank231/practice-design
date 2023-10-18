
def kanpsack_0_1(vals, weight, W, curr):
    """
    Returns the maximum price that we can fill in the knapsack

    vals = array of prices
    weight = array of weights
    W = limit of max weight in knapsack
    curr = current index in consideration
    """

    if curr == 0:
        if weight[curr] <= W:
            return vals[curr]
        else:
            return 0

    new_W = W - weight[curr]
    select_curr = -1

    if weight[curr] <= W:
        select_curr = vals[curr] + kanpsack_0_1(vals, weight, new_W, curr-1)

    not_Select_curr = kanpsack_0_1(vals, weight, W, curr-1)
    
    return max(select_curr, not_Select_curr)


vals = [20, 5, 10, 40, 15, 25]
weight = [1, 2, 3, 8, 7, 4]
W = 10
last = len(vals) - 1
ans = kanpsack_0_1(vals, weight, W, last)



print(ans)

