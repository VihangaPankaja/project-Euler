""" 
    Each character on a computer is assigned a unique code and the preferred standard is 
    ASCII (American Standard Code for Information Interchange). 
    For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to ASCII, 
    then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that 
    using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text message, 
    and the key is made up of random bytes. The user would keep the encrypted message and the encryption 
    key in different locations, and without both "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
    If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
    The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.
    txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, 
?   decrypt the message and find the sum of the ASCII values in the original text.
"""


from itertools import cycle, product


def XOR_decrypt(message, *password):
    return [i ^ j for i, j in zip(message, cycle(password))]    # apply xor with characters of message and password


def decrypt(message: list[int]) -> list[int]:
    a = []
    for key in product(range(97, 123), repeat=3):       # try all 3 simple letter long combinations
        decrypted =  XOR_decrypt(message, *key)
        
        score =  sum([97 <= i <= 122 or 65<= i <= 90 or i == 32 for i in decrypted])    # contains English letters or whitespace
        a.append((score, decrypted))
        
    a = sorted(a, key=lambda x: x[0], reverse=True)     # sort in descending order according to score
    return a[0][1]                                      # return the best scored decryption


if __name__ == "__main__":
    with open('files/p059_cipher.txt', 'r') as file:
        file = file.read().split(',')
        
    message = decrypt(list(map(int, file)))
    print(sum(message))
    