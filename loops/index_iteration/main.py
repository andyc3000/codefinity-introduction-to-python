prices = [29.99, 45.50, 12.75, 38.20]

for cost in range(len(prices)):
    if cost == 0:
        prices[cost] *= 0.90
    elif cost == 1:
        prices[cost] *= 0.80
    elif cost == 2:
        prices[cost] *= 0.85
    elif cost == 3:
        prices[cost] *= 0.95
    else:
        prices[cost]
    print(f"Updated price for {cost}: ${prices[cost]:.2f}")
    