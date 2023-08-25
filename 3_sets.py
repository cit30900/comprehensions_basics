def main():
    # Define a string
    quote = "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character."

    # Make a list of each letter in the string
    letters = [l for l in quote]

    # Filter out spaces - we only want letters
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = [l for l in quote.upper() if l in alpha]
    print(letters)
  
    # Create a set that holds only unique values
    letters_set = set(letters)
    print(letters_set)

if __name__== "__main__":
  main()