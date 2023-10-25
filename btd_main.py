def main():
    while True:
        print('''Main Menu
        ---------
        1. Encode
        2. Decode
        3. Exit\n''')
        choice = int(input('Please select an option from the menu: '))
        if choice == 1:
            password = input('\nPlease enter the password you would like to encode: ')
            encoded_password = encode(password)
            print(encoded_password)
        elif choice == 2:
            encoded_password = input('\nPlease enter the encoded password you would like to decode: ')
            password = decode(encoded_password)
            print(password)
        elif choice == 3:
            print('Goodbye!')
            break


if __name__ == '__main__':
    main()
