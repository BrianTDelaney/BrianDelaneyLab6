# Brian Delaney
def main():
    while True:
        print('''Menu
---------
1. Encode
2. Decode
3. Quit\n''')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('\nPlease enter your password to encode: ')
            encoded_password = encode(password)
            print(f'\nYour password has been encoded and stored!')
        elif choice == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')
        elif choice == 3:
            break
# Uses a while loop that takes in user input and executes functions using if/elif statements.


def encode(number):
    encoded_number = ''
    for digit in number:
        digit = str(int(digit) + 3)
        encoded_number = encoded_number + digit
    return encoded_number
# Function goes digit by digit converting the digit to an integer, adding 3 to it, converting it to a string,
# and then "appending" it to the encoded string.


if __name__ == '__main__':
    main()
# Main function only executes if being run from main program.
