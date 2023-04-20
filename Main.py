# Import required modules
import Random_Bit_Generator as Rand
import BPSK
import AWGN_Channel as AWGN


def simulate_communication_system(message_size, symbol_size, bitrate, signal_to_noise_ratio_db):
    # Generate a random message of given size
    random_message = Rand.random_bit_generator(message_size, symbol_size)

    # Modulate the message using binary phase shift keying (BPSK) modulation
    modulated_message, base_func_1= BPSK.binary_phase_shift_keying_modulator(random_message, bitrate)

    # Determine the window size for demodulation
    window_size = int(modulated_message.size / len(random_message))

    # Simulate the effect of the AWGN channel on the modulated message
    received_message = AWGN.additive_white_gaussian_noise_channel(modulated_message, signal_to_noise_ratio_db)

    # Demodulate the message using BPSK demodulation and the base functions
    demodulated_message = BPSK.binary_phase_shift_keying_demodulator(received_message, base_func_1,window_size)

    # Count the number of errors between the original and demodulated messages
    errors = sum(1 for a, b in zip(random_message, demodulated_message) if a != b)

    # Print the number of errors between the original and demodulated messages
    print(f"Bit Error Rate: {errors / message_size}")


simulate_communication_system(message_size=10000, symbol_size=1, bitrate=1, signal_to_noise_ratio_db=0)
