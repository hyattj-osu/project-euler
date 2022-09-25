import binascii

def main():


    cipher = []
    with open("./p59/p059_cipher.txt", 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            split_line = line.strip().split(',')
            cipher.append([ int(n) for n in split_line ])
    cipher_nums = cipher[0]

    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                keys = [ a, b, c ]
                key_index = 0
                deciphered = []
                sum = 0
                for character in cipher_nums:
                    xor = bin(character ^ keys[key_index])
                    n = int(xor, 2)
                    sum += n
                    deciphered.append(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

                    key_index += 1
                    if key_index > 2:
                        key_index = 0
                # if 'and' in deciphered
                deciphered_joined = ''.join(deciphered)
                if 'reciprocarum' in deciphered_joined:
                    print(deciphered_joined)
                    print(f'sum: {sum}')

    print(deciphered)
    return()

if __name__ == "__main__":
    main()