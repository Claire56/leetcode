# First, I wanna know how much money I could have made yesterday if I'd been 
# trading Apple stocks all day.So I grabbed Apple's stock prices from yesterday 
# and put them in a list called stock_prices, where:

# The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
# The values are the price (in US dollars) of one share of Apple stock at that time.
# So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

# Write an efficient function that takes stock_prices and returns the best profit
# I could have made from one purchase and one sale of one share of Apple stock yesterday.

# For example:

stock_prices = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices)
# # Returns 6 (buying for $5 and selling for $11)

def profit(l):
	buy = min(l)
	buy_index = l.index(buy)
	print(f'this is the buy index {buy_index}')
	sell = max(l[buy_index +1 :])
	print(l.index(sell))
	return sell - buy 

print(profit([10,7,5,8,11,9]))
print('two minimums')
print(profit([10,5,5,8,11,9]))
print('two maximums')
print(profit([10,7,5,8,11,9,11]))
print(profit([10,7,5,8,11,9,11]))

# print(dir(stock_prices))