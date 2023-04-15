import numpy as np
import math


def binary_phase_shift_keying_modulator(bitstream, bit_rate, carrier_frequency):
    total_time = len(bitstream) / bit_rate
    seconds = np.linspace(0, total_time, 10 * bit_rate)
    sine_wave = np.sin(2 * math.pi * carrier_frequency * seconds)
    cosine_wave = np.cos(2 * math.pi * carrier_frequency * seconds)
    modulated_wave=[0]*len(seconds)
    for i in range(0,len(seconds)):

    print('hi')


binary_phase_shift_keying_modulator("1010101010", 100, 2000)