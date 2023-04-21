import numpy as np
import math


def binary_phase_shift_keying_modulator(bitstream, bit_rate):
    # Calculate the energy of the signal
    signal_energy = 1

    # Calculate the amplitude of the sinusoid
    sinusoid_amplitude = np.sqrt(signal_energy * 2 * bit_rate)

    # Calculate the amplitude of the basis function
    basis_function_amplitude = np.sqrt(2 * bit_rate)

    # Calculate the total time of the signal
    total_time = len(bitstream) / bit_rate

    # Calculate the sampling frequency of the signal
    sampling_frequency = bit_rate * 10

    # Calculate the carrier frequency of the signal
    carrier_frequency = sampling_frequency / 20

    # Generate a time axis for the signal
    seconds = np.linspace(0, total_time, int(sampling_frequency * total_time))

    # Generate a sinusoidal wave for a bit value of 1
    one_symbol = sinusoid_amplitude * np.sin(2 * math.pi * carrier_frequency * seconds)

    # Generate a sinusoidal wave for a bit value of 0
    zero_symbol = -1 * sinusoid_amplitude * np.sin(2 * math.pi * carrier_frequency * seconds)

    # Generate a basis function wave
    basis_function = basis_function_amplitude * np.sin(2 * math.pi * carrier_frequency * seconds)

    # Create an empty modulated wave array
    modulated_wave = np.zeros(len(seconds))

    # Calculate the window size for each bit
    window_size = int(len(seconds) / len(bitstream))

    # Modulate each bit
    for i, bit in enumerate(bitstream):
        # If the bit is 1, add the one symbol wave to the modulated wave
        if bit == '1':
            modulated_wave[i * window_size:(i + 1) * window_size] = one_symbol[i * window_size:(i + 1) * window_size]
        # If the bit is 0, add the zero symbol wave to the modulated wave
        else:
            modulated_wave[i * window_size:(i + 1) * window_size] = zero_symbol[i * window_size:(i + 1) * window_size]

    # Return the modulated wave and the basis function
    return modulated_wave, basis_function


def binary_phase_shift_keying_demodulator(received_message, base_one, window_size):
    # Demodulate the signal by multiplying it with the two carrier waves
    demodulated_signal_base_one = np.multiply(received_message, base_one)
    demodulated_signal_base_zero = np.multiply(received_message, -1 * base_one)
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
