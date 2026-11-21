products = {}
keys_string = input("Enter your products(click space to enter next product):")
keys = keys_string.split()
for n in keys:
    key = n
    value = input(f"explanation of {n}:")
    products[key] = value
print(products)
