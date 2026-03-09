# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
revenues = []
revenue_per_product = []
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i]*quantities_sold[i])
    return(revenue)

def formatted_output(revenues):
    return(sorted(revenues))
                       
revenues = calculate_revenue(prices, quantities_sold)

for name,rev in zip(products, revenues):
    revenue_per_product.append((name,rev))

revenue_per_product = formatted_output(revenue_per_product)

for i in range(len(revenue_per_product)):
    print(f"{revenue_per_product[i][0]} has total revenue of ${revenue_per_product[i][1]}")
# Example of expected output line (do not remove):
