# Christopher Kostas
# Kysa Mesa



# print_menu function
def print_menu():
    # Print the menu
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')


# menu function
def menu(selection, password):
    # Selection 1
    if selection == '1':
        # Print password encoded
        print('Your password has been encoded and stored!\n')

    # Selection 2
    if selection == '2':
        # Print encoded password and original password
        print(f'The encoded password is {encode(password)}, and the original password is .\n')


# encode function
def encode(password):
    # decoded_password variable
    encoded_password = ''

    # For loop for encoding password
    for i in password:
        # Add 3 to each number in password
        encoded_password += str(int(i)+3)
    # Return the encoded password
    return encoded_password


# main method call
if __name__ == "__main__":
    Continue = True
    # While loop to continue program
    while Continue:
        # Print the menu
        print_menu()
        # Prompt the user for menu input
        selection = input('Please enter an option: ')

        # If the user has not asked to exit
        if selection != '3':
            # If the user entered 1
            if selection == '1':
                # Prompt the user to enter a password
                encode(input('Please enter your password to encode: '))
        else:
            # Set the loop boolean to False to exit the loop
            Continue = False
