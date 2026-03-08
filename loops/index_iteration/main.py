prices = [29.99, 45.50, 12.75, 38.20]
discount = [10,20,15,5]
for cost in range(len(prices)):
    prices[cost] -= prices[cost] * (discount[cost]/100)
    print(f"updated price for item {cost+1}: ${prices[cost]:.2f}")