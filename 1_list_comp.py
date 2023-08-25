def main():
    # Define a list of numbers
    numbers = [1,2,3,4,5,6,7,8,9,10]

    ## LOOP METHOD
    '''
    # Create a new list that will hold the squared values of the elements in the `numbers` list
    squares = []

    # Loop through the `numbers` list and add squared values to the `squares` list
    for n in numbers:
        squares.append(n**2)

    # Print the `squares` list
    print(squares)
    '''
  
    ## LIST COMPREHENSION METHOD
    squares = [n**2 for n in numbers]
    print(squares)
  

if __name__== "__main__":
  main()