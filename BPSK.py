import numpy as np
import math


def binary_phase_shift_keying_modulator(bitstream, bit_rate):
    total_time = len(bitstream) / bit_rate
    sampling_frequency = (len(bitstream) * 100) / total_time
    carrier_frequency = sampling_frequency/20
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
    return modulated_wave, sine_wave, cosine_wave


def binary_phase_shift_keying_demodulator(received_message, base_one, base_zero, window_size):
    demodulated_signal_base_one = np.multiply(received_message, base_one)
    demodulated_signal_base_zero = np.multiply(received_message, base_zero)
    bit_count = int(demodulated_signal_base_one.size / window_size)
    received_bits = ""
    for i in range(0, bit_count):
        bit_one_signal = demodulated_signal_base_one[i * window_size:(i + 1) * window_size]
        bit_zero_signal = demodulated_signal_base_zero[i * window_size:(i + 1) * window_size]
        signal_one_integral = np.trapz(bit_one_signal)
        signal_zero_integral = np.trapz(bit_zero_signal)
        if signal_one_integral > signal_zero_integral:
            received_bits += "1"
        else:
            received_bits += "0"
    return received_bits
