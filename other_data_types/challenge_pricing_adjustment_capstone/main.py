#Grocery Store System
grocery_inventory = {
    "Milk":     ("Dairy", 3.50, 8),
    "Eggs":     ("Dairy", 5.50, 30),
    "Bread":    ("Bakery", 2.99, 15),
    "Apples":   ("Produce", 1.50, 50)
}
price_item_egg = grocery_inventory.get("Eggs")[1]
if price_item_egg > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = ("Dairy", price_item_egg -1, 30)

else:
    print("The price of Eggs is reasonable")
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
stock_item_milk = grocery_inventory.get("Milk")[2]
if stock_item_milk < 10:
    print ("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = ("Dairy", 3.50, stock_item_milk+20)

else:
    print("Milk has sufficient stock")

price_item_apple = grocery_inventory.get("Apples")[1]
if price_item_apple > 2:
    print("Apples removed from inventory due to high price")
    grocery_inventory.pop("Apples")
print("Updated inventory:", grocery_inventory)
