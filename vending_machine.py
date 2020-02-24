from byotest import *

"""
usd_coins = [100, 50, 25, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

def get_change(amount, coins = eur_coins):
   
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
    return change
    
"""

usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20}
eur_coins = {200: 20, 100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}
# Create a dictionary with denomination of coin and its quantity as key, value


def get_change(amount, coins=eur_coins):
    """
    Unlike a list, looping through a dictionary does not keep the order.
    Therefore we use sorted() and reverse order to start with the highest
    denomination. The while ends when coin quantity is zero. An exception is
    thrown if there are insufficient coins to give change.
    """
    change = []
    for denomination in sorted(coins.keys(), reverse=True):
        while denomination <= amount and coins[denomination] > 0:
            amount -= denomination
            coins[denomination] -= 1
            change.append(denomination)
    if amount != 0:
        raise Exception("Insufficient coins to give change.")
    return change


test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 2])
test_are_equal(get_change(35, usd_coins), [25, 10])
test_are_equal(get_change(35), [20, 10, 5])
test_are_equal(get_change(5, {2: 1, 1: 4}), [2, 1, 1, 1])
test_exception_was_raised(get_change, (5, {2: 1, 1: 2}),
                          "Insufficient coins to give change.")





"""

test_are_equal (get_change (0), [])
test_are_equal (get_change (1), [1])
test_are_equal (get_change (2), [2])
test_are_equal (get_change (5), [5])
test_are_equal (get_change (10), [10])
test_are_equal (get_change (20), [20])
test_are_equal (get_change (50), [50])
test_are_equal (get_change (100), [100])
test_are_equal (get_change (3), [2,1])
test_are_equal (get_change (7), [5,2])
test_are_equal (get_change (9), [5, 2,2])
test_are_equal (get_change (35, usd_coins), [25, 10])

"""

print ("All tests pass!")