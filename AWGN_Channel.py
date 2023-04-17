from random import gauss


# Define a function for simulating the effect of an additive white Gaussian noise channel on a transmitted message
def additive_white_gaussian_noise_channel(transmitted_message, signal_to_noise_ratio_db):
    # Converting the SNR from DB to Watts
    signal_to_noise_ratio = 10 ** (signal_to_noise_ratio_db / 10)

    # Calculate the standard deviation of the noise using the given signal-to-noise ratio
    noise_stddev = 1 / signal_to_noise_ratio

    # Generate Gaussian noise with zero mean and calculated standard deviation
    noise = [gauss(0.0, noise_stddev) for i in range(len(transmitted_message))]

    # Initialize a list to store the received message
    received_message = [0] * len(transmitted_message)

    # Add noise to the transmitted message to simulate the effect of the AWGN channel
    for i in range(0, len(transmitted_message)):
        received_message[i] = transmitted_message[i] + noise[i]

    # Return the received message
    return received_message
