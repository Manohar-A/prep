def gridtraveller(n,m,memo = {}):
    key1 = (n,m)
    key2 = (m,n)
    if(key1 in memo):
        return memo[key1]
    if (key2 in memo):
        return memo[key2]
    if(n == 1 and m == 1):
        return 1
    if(n == 0 or m == 0):
        return 0
    memo[key1] = gridtraveller(n-1, m,memo) + gridtraveller(n,m-1,memo)
    memo[key2] = memo[key1]
    return memo[key1]
print(gridtraveller(30,30))
