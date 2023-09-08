# sum of list
def sum_and_mult(arr:list):
    arr_sum = 0
    arr_mult = 1

    for element in arr:
        arr_sum += element
        arr_mult *= element

    print(arr)
    print([arr_sum, arr_mult])

sum_and_mult([1, 7, 3])
#O(n)

# Max item and index in a list
#find and print the max element in a list and the integer

def find_max_number(arr: list):
    max_index = 0
    max_item = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i

    return [max_index, max_item]


print(find_max_number([1, 45, 33, 76, 9, 10]))
# O(n)

#codewars.com to practice coding challenges

#sum between min and max elements

def sum_btw_min_and_max(arr: list):
    min_item = max_index = 0
    max_item = max_item = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > arr[max_item]:
            max_item = i
            max_item = arr[i]
        if arr[i] < arr[min_item]:
            min_item = i
            min_item = arr[i]

    sum(arr[min(min_item, max_item) + 1:max(min_item, max_item)])

print(sum_btw_min_and_max([1, 2, 3, 4, 5]))

# best time to buy and sell stock
def buy_sell(prices: list):
    curr_profit = max_profit = 0

    for i in range(len(prices) - 1):
        curr_profit = curr_profit + prices[i + 1] - prices[i]
        if curr_profit > max_profit:
            max_profit = curr_profit
        if curr_profit < 0:
            curr_profit = 0

    return max_profit

test_prices = [7, 1, 5, 3, 6, 4]

print(buy_sell(test_prices))

#buy and sell stock 2
def buy_and_sell_stock(prices: list):
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] - prices[i] > 0:
            profit += prices[i + 1] - prices[i]

    return profit
test_prices = [7, 1, 5, 3, 6, 4]

print(buy_and_sell_stock(test_prices))
