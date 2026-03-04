meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)
if "Ham" in deli_dept[0][0] and meat[2]<100:
    meat[2] = 100
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
if not seasonal_meat in deli_dept:
    deli_dept.append(seasonal_meat)
if condiment in deli_dept:
   deli_dept.remove(condiment)

deli_dept.sort()
print("Updated Deli List:", deli_dept)
    
    