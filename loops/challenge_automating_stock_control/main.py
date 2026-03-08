# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing Started")
for item, details in inventory.items():
    print(f"Processing {item}")
    current_stock, min_stock, restock_qty, on_sale = details
    while current_stock < min_stock:
        current_stock += restock_qty
        details[0] = current_stock
        details[3] = current_stock > discount_threshold
print("Processing completed")

    