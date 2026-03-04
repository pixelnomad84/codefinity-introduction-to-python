vegetables = ["tomatoes", "potatoes", "onions"]
if "onions" in vegetables:
    vegetables.remove("onions")
if not "carrots" in vegetables:
    vegetables.append("carrots")
if not "cucumbers" in vegetables:
    vegetables.append("cucumbers")
vegetables.sort()
print("updated vegetable Inventory:" ,vegetables)
    