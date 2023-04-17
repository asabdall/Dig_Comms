import numpy as np
import math


def binary_phase_shift_keying_modulator(bitstream, bit_rate,carrier_frequency):
    # Compute total time for the bitstream
    total_time = len(bitstream) / bit_rate
    # Compute sampling frequency
    sampling_frequency = carrier_frequency*20
    # Generate time array with sufficient samples
    seconds = np.linspace(0, total_time, int(sampling_frequency*total_time))
    # Generate sine and cosine waves for the carrier frequency
    sine_wave = np.sin(2 * math.pi * carrier_frequency * seconds)
    cosine_wave = np.cos(2 * math.pi * carrier_frequency * seconds)
    # Initialize modulated_wave with zeros
    modulated_wave = [0] * len(seconds)
    # Compute window size
    window_size = int(len(seconds) / len(bitstream))
    # For each bit in the bitstream, modulate the wave
    for i in range(0, len(bitstream)):
        if "1" in bitstream[i]:
            modulated_wave[i * window_size:(i + 1) * window_size] = sine_wave[i * window_size:(i + 1) * window_size]
        else:
            modulated_wave[i * window_size:(i + 1) * window_size] = cosine_wave[i * window_size:(i + 1) * window_size]
    # Convert modulated_wave to a numpy array
    modulated_wave = np.array(modulated_wave)
    # Return modulated wave, and the two carrier waves
    return modulated_wave, sine_wave, cosine_wave


def binary_phase_shift_keying_demodulator(received_message, base_one, base_zero, window_size):
    # Demodulate the signal by multiplying it with the two carrier waves
    demodulated_signal_base_one = np.multiply(received_message, base_one)
    demodulated_signal_base_zero = np.multiply(received_message, base_zero)
    # Compute number of bits in the received message
    bit_count = int(demodulated_signal_base_one.size / window_size)
    # Initialize received_bits
    received_bits = ""
    # For each bit, compute the signal integral for both carrier waves, and choose the bit accordingly
    for i in range(0, bit_count):
        bit_one_signal = demodulated_signal_base_one[i * window_size:(i + 1) * window_size]
        bit_zero_signal = demodulated_signal_base_zero[i * window_size:(i + 1) * window_size]
        signal_one_integral = np.trapz(bit_one_signal)
        signal_zero_integral = np.trapz(bit_zero_signal)
        if signal_one_integral > signal_zero_integral:
            received_bits += "1"
        else:
            received_bits += "0"
    # Return the received bits
    return received_bits
