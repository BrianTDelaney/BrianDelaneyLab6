# Brian Delaney's encoding function

def encode(number):
    encoded_number = ''
    for digit in number:
        digit = int(digit) + 3
        encoded_number = encoded_number + digit
    return encoded_number
