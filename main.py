morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', ' ': '\t'}

letters = {'.-': 'A', '-...': 'B', '-.-.': 'C',
           '-..': 'D', '.': 'E', '..-.': 'F',
           '--.': 'G', '....': 'H', '..': 'I',
           '.---': 'J', '-.-': 'K', '.-..': 'L',
           '--': 'M', '-.': 'N', '---': 'O',
           '.--.': 'P', '--.-': 'Q', '.-.': 'R',
           '...': 'S', '-': 'T', '..-': 'U',
           '...-': 'V', '.--': 'W', '-..-': 'X',
           '-.--': 'Y', '--..': 'Z', ' ': '\t'}


def encode_to_morse():
    text = input().upper().split()
    for word in text:
        print(" ".join([morse[s] for s in word]), end='', sep=' ')


def decode_from_morse():
    text = input().split(' ')
    for word in text:
        print(" ".join([letters[word]]), end='', sep=' ')


def main():
    print('Здравствуйте! Хотите ли вы раскодировать или закодировать текст?')
    a = input()
    while a != 'да' and a != 'Да' and a != 'нет' and a != 'Нет':
        print('Здравствуйте! Хотите ли вы раскодировать или закодировать текст?')
        a = input()
        if a == 'нет' or a == 'Нет':
            break
    if a == 'да' or a == 'Да':
        print('Если вы хотите закодировать, введите 1. Если вы хотите раскодировать, введите 2.'
              ' Если вы хотите закончить, введите 3.')
        b = int(input())
        while b != 1 and b != 2 and b != 3:
            print('Если вы хотите закодировать, введите 1. Если вы хотите раскодировать, введите 2.'
                  ' Если вы хотите закончить, введите 3.')
            b = int(input())
            if b == 3:
                break
        if b == 1:
            return encode_to_morse()
        elif b == 2:
            return decode_from_morse()


main()
