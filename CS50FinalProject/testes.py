from tabulate import tabulate

# nested = {
#     "first": {"one":1, "premier":1},
#     "second": {"two":2, "deuxième":2},
# }
# print(tabulate([nested], headers="keys"))

def min_ignore_none(a, b):
    if a==None:
        return b
    if b==None:
        return a
    return min(a,b)

def min_coins(m, coins):
    memo={}
    memo[0] = 0

    for i in range(1, m+1):
        for coin in coins:
            subproblem = i-coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem)+1)
            print(f"memo: {memo}")
    return memo[m]

coins = [1,4,5]
# print(f"Coins: {coins}")
# list=[5,7,8,9,13,50]
# for x in list:
#     print(f"Min Coins of {x}={min_coins(x, coins)}")
min_coins(8, coins)