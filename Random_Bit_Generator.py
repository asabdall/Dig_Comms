import random


def random_bit_generator(message_size):
    bitstream = ""
    for i in range(0, message_size):
        random_decimal = random.random()
        if random_decimal > .5:
            added_bit = "1"
        else:
            added_bit = "0"
        bitstream += added_bit
    return bitstream


random_bitstream = random_bit_generator(100)
print('hi')
