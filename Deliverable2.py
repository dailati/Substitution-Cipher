import string

def decryptedmessage(cipherText):
    alphabet = list(string.ascii_uppercase)
    english_freq = {
        'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28,
        'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61,
        'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11,
        'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
    }

    freq = []
    for letter in alphabet:
        freq.append(cipherText.upper().count(letter))

    total_chars = sum(freq)
    freq_percentage = [round((count / total_chars) * 100, 2) for count in freq]

    for i, letter in enumerate(alphabet):
        print(letter, ':', freq_percentage[i], '% Expected: ', english_freq[letter],'%')

ciphered_text = input(print("Enter the ciphered text: "))
decryptedmessage(ciphered_text)