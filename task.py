def find_coins_greedy(value: int, coins: list[int]) -> dict:
    change_dict = {}

    for coin in coins:
        if value >= coin:
            count = value // coin
            change_dict[coin] = count
            value -= coin * count

    return change_dict


def find_min_coins(value: int, coins: list[int]) -> dict:
    dp = [float("inf")] * (value + 1)
    dp[0] = 0

    used_coins = [0] * (value + 1)

    for i in range(1, value + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin

    result = {}
    while value > 0:
        coin = used_coins[value]
        if coin == 0:
            return {}
        result[coin] = result.get(coin, 0) + 1
        value -= coin

    return result


coins_list = [50, 25, 10, 5, 2, 1]
print(find_min_coins(113, coins_list))
print(find_coins_greedy(113, coins_list))
