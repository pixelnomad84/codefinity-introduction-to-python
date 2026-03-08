# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for product, values in products.items():
    values[0] = float(values[0])
    values[1] = int(values[1])
    total_sales_list.append(values[0]*values[1])
for product, total in zip(products, total_sales_list):
    print(f"Total Sales for {product}: ${total}")
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
total_sum = sum(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")