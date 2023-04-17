# Import required modules
import Random_Bit_Generator as Rand
import BPSK
import AWGN_Channel as AWGN

# Define the size of the message to be sent
message_size = 1000

# Generate a random message of given size
random_message = Rand.random_bit_generator(message_size)

# Define the number of bits per second to be used in BPSK modulation
bits_per_second = 100

# Define the carrier frequency to be used in BPSK modulation
carrier_frequency = 2000

# Modulate the message using binary phase shift keying (BPSK) modulation
modulated_message, base_func_1, base_func_0 = BPSK.binary_phase_shift_keying_modulator(random_message, bits_per_second
                                                                                       , carrier_frequency)

# Determine the window size for demodulation
window_size = int(modulated_message.size / len(random_message))

# Define the signal-to-noise ratio in DB for the AWGN channel
signal_to_noise_ratio_db = -0

# Simulate the effect of the AWGN channel on the modulated message
received_message = AWGN.additive_white_gaussian_noise_channel(modulated_message, signal_to_noise_ratio_db)

# Demodulate the message using BPSK demodulation and the base functions
demodulated_message = BPSK.binary_phase_shift_keying_demodulator(received_message, base_func_1, base_func_0,
                                                                 window_size)

# Count the number of errors between the original and demodulated messages
errors = sum(1 for a, b in zip(random_message, demodulated_message) if a != b)

# Print the number of errors between the original and demodulated messages
print(f"Number of errors: {errors}")
