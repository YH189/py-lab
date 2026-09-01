def is_valid_shift(shift):
    return isinstance(shift,int) and 1<= shift <= 25

def is_valid_text(text):
    return isinstance(text,str) and len(text) >0

def caesar(text,shift, encypt=True, Strict = False):

    if not is_valid_shift(shift):
        return 'Invalid shift value'
    if not is_valid_text(text):
        return 'Invalid text value'
    if Strict and not text.replace(' ','').isalpha():
        return 'Text contains invalid characters in strict mode'
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet+alphabet.upper(), shifted_alphabet+shifted_alphabet.upper())
    return text.translate(translation_table)

user_text = input('Enter the message for Encryption or Decryption:')
user_shift = int(input('Enter a shift value from 1-25:'))
user_mode = input('Encrypt or Decrypt (E/d):')
should_encrypt = user_mode == 'E'

result = caesar(user_text,user_shift,should_encrypt)
print(f'Result:{result}')
