import inflect
from bitstring import ConstBitStream

def generate_codebook_sequences(bits):
    book = {"Numerical Positions": [1, 2],
            "Subsequences": ["0", "1"],
            "Numerical Representations": ["NA", "NA"],
            "Binary Encoded Blocks": ["NA", "NA"]
            }
    leftover_bits = bits
    i = 1
    while len(leftover_bits) > 0:
        subsequence = leftover_bits[0:i]
        if subsequence in book["Subsequences"]:
            i = i + 1
        else:
            book["Numerical Positions"].append(len(book["Numerical Positions"]) + 1)
            book["Subsequences"].append(subsequence)
            book["Numerical Representations"].append("NA")
            book["Binary Encoded Blocks"].append("NA")
            leftover_bits = leftover_bits[i:]
            i = 1
        if i > len(leftover_bits):
            break
    return book


def generate_numerical_representations(book):
    for i in range(2, len(book["Subsequences"])):
        for j in range(0, i):
            k = i - j - 1
            if book["Subsequences"][i][0:len(book["Subsequences"][i]) - 1] == book["Subsequences"][k]:
                book["Numerical Representations"][i] = str(book["Numerical Positions"][k])
        if book["Subsequences"][i][len(book["Subsequences"][i]) - 1] == "0":
            book["Numerical Representations"][i] += "1"
        else:
            book["Numerical Representations"][i] += "2"
    return book


def generate_binary_encoded_blocks(book):
    max_size = 0
    for i in range(2, len(book["Numerical Representations"])):
        first_digit = int(book["Numerical Representations"][i][0:len(book["Numerical Representations"][i]) - 1])
        binary_first_digit = bin(first_digit)[2:]
        if len(binary_first_digit) > max_size:
            max_size = len(binary_first_digit)
    max_size += 1
    for i in range(2, len(book["Numerical Representations"])):
        first_digit_binary = bin(int(book["Numerical Representations"][i][0:len(
            book["Numerical Representations"][i]) - 1]))[2:]
        second_digit_binary = bin(int(book["Numerical Representations"][i][len(
            book["Numerical Representations"][i]) - 1]))[2:]
        book["Binary Encoded Blocks"][i] = first_digit_binary + second_digit_binary
        book["Binary Encoded Blocks"][i] = book["Binary Encoded Blocks"][i].zfill(max_size)
    return book


def generate_compressed_bitstream(bits, book):
    new_bits = bits
    for i in range(0, len(book["Subsequences"])):
        k = len(book["Subsequences"]) - i - 1
        p = inflect.engine()
        new_bits = new_bits.replace(book["Subsequences"][k], p.number_to_words(k))
    for i in range(0, len(book["Subsequences"])):
        if i > 1:
            new_bits = new_bits.replace(p.number_to_words(i), book["Binary Encoded Blocks"][i])
        elif i == 0:
            new_bits = new_bits.replace(p.number_to_words(i), "0")
        elif i == 1:
            new_bits = new_bits.replace(p.number_to_words(i), "1")
    return new_bits
# read file
b = ConstBitStream(filename="C:\Users\hamad\Desktop\error.txt")
bit_sequence = b.bin
codebook = generate_codebook_sequences(bit_sequence)
codebook = generate_numerical_representations(codebook)
codebook = generate_binary_encoded_blocks(codebook)
new_bit_stream = generate_compressed_bitstream(bit_sequence, codebook)
original_length=len(bit_sequence)
new_length=len(new_bit_stream)
print('go')
