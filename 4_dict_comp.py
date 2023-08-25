def main():
    # Define a dictionary
    products = {"Latte": 3.5, "Mocha": 4.0, "Matcha": 4.5, "Drip": 1.5, "Americano": 2.0, "Cortado": 2.5, "Macchiato": 4.5}

    ## Dictionary Comprehension Structure:
    # dictionary = {key: value for vars in iterable}

    # Write the contents of the dictionary into a new dictionary
    products2 = {k: v for (k, v) in products.items()}
    print(products2)

    # Create a list of keys from the dictionary
    keys = [k for (k,v) in products.items()]
    print(keys)

    # Create a list of values from the dictionary
    values = [v for (k,v) in products.items()]
    print(values)

if __name__== "__main__":
  main()