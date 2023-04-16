import numpy as np
import pandas as pd
import plotly.express as px
import math


def binary_phase_shift_keying_modulator(bitstream, bit_rate, carrier_frequency):
    total_time = len(bitstream) / bit_rate
    seconds = np.linspace(0, total_time, len(bitstream) * 100)
    sine_wave = np.sin(2 * math.pi * carrier_frequency * seconds)
    cosine_wave = np.cos(2 * math.pi * carrier_frequency * seconds)
    modulated_wave = [0] * len(seconds)
    window_size = int(len(seconds) / len(bitstream))
    for i in range(0, len(bitstream)):
        if "1" in bitstream[i]:
            modulated_wave[i * window_size:(i + 1) * window_size] = sine_wave[i * window_size:(i + 1) * window_size]
        else:
            modulated_wave[i * window_size:(i + 1) * window_size] = cosine_wave[i * window_size:(i + 1) * window_size]
    modulated_wave = np.array(modulated_wave)
    return modulated_wave, cosine_wave, window_size,seconds


def binary_phase_shift_keying_demodulator(received_message, reference_signal, window_size,time):
    demodulated_signal = np.multiply(received_message, reference_signal)
    bit_count = int(demodulated_signal.size / window_size)
    received_bits = ""
    for i in range(0, bit_count):
        bit_signal = demodulated_signal[i * window_size:(i + 1) * window_size]
        signal_integral = np.trapz(bit_signal)
        if signal_integral > .25:
            received_bits += "1"
        else:
            received_bits += "0"
    return received_bits


message_signal, reference_signal, window_size,time = binary_phase_shift_keying_modulator("1010101010", 10, 20)
received_message=binary_phase_shift_keying_demodulator(message_signal, reference_signal, window_size,time)
print('hi')
