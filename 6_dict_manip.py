def main():
    # Define a dictionary
    products = {"Latte": 3.5, "Mocha": 4.0, "Matcha": 4.5, "Drip": 1.5, "Americano": 2.0, "Cortado": 2.5, "Macchiato": 4.5}
    print(products)

    # Increase all of the prices by 10%
    products_inc = {k: v*1.1 for (k,v) in products.items()}
    print(products_inc)

    # Increase all of the prices by 10% for items that are $2.50 or more
    products_inc = {k: v*1.1 for (k,v) in products.items() if v >= 2.5}
    print(products_inc)

    # Merge the updated prices into the original `products` dictionary
    # We want to update `products` and OVERWRITE any value that appears in the `products_inc` dictionary
    products.update(products_inc)
    print(products)

if __name__== "__main__":
  main()