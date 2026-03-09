def apply_discount(price, discount=0.05):
    discount_price = price * (1-discount)
    return(discount_price)

def apply_tax(price, tax=0.07):
    tax_price = price * (1+tax)
    return(tax_price)

def calculate_total(price, discount=0.05, tax=0.07):
    total_price = apply_tax(price, tax)
    total_price = apply_discount(total_price, discount)
    return(total_price)

total_cost = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_cost}")
total_cost = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_cost}")
