import sys

def test():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    if direction != 'encode' and direction != 'decode':
        print("Please enter either 'encode' or 'decode' in direction")
        sys.exit()
        
    user_input = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    ALPHABET_LENGTH = len(alphabet)
    output = ''
    for item in user_input:
        pos = alphabet.index(item)
        if direction == 'encode':
            output += alphabet[(pos + shift) % ALPHABET_LENGTH]
        else:
            output += alphabet[(pos - shift) % ALPHABET_LENGTH]
    
    print(f'output: {output}')