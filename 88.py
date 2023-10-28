def find_min_coins(coins, target_amount):
    coins.sort()
    num_coins = 0
    coins_combination = []
    for coin in coins:
        num_coin = target_amount // coin
        num_coins += num_coin
        target_amount -= num_coin * coin
        coins_combination.append((coin, num_coin))
        if target_amount == 0 or len(coin_combination) == 2:
            break
    return num_coins, coin_combination
coins = list(map(int, input("Print nominal cherez space: ").split()))
target_amount = int(input("Print sum: "))
num_coins, coin_combination = find_min_coins(coins, target_amount)
print(f"Min col v monet: {num_coins}")
print("Kombination i if coll:")
for coin, num in coin_combination:
    print(f"nominal {coin}: {num} coina")
