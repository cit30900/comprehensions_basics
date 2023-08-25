def main():
    # Define a list of numbers
    numbers = [1,2,3,4,5,6,7,8,9,10]

    # Make a list of squared values of **only even** numbers
    squares = [n**2 for n in numbers if n % 2 == 0]
    print(squares)

    # Define a list of states
    states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
    
    # Make a list of states with the letter "e"
    e_states = [s for s in states if 'e' in s]
    print(e_states)

if __name__== "__main__":
  main()