def find_coins_greedy(amount, coins=[50, 20, 10, 5, 2, 1]):
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

amount = 113
result_greedy = find_coins_greedy(amount)
print("Жадібний алгоритм (find_coins_greedy) результат для суми 113:", result_greedy)

def find_min_coins(amount, coins=[50, 20, 10, 5, 2, 1]):
    max_amount = amount + 1
    min_coins = [max_amount] * (amount + 1)
    min_coins[0] = 0
    coin_used = [None] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin

    if min_coins[amount] == max_amount:
        return None 

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

result_dp = find_min_coins(amount)
print("Алгоритм динамічного програмування (find_min_coins) результат для суми 113:", result_dp)
