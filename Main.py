import Random_Bit_Generator as Rand
import matplotlib.pyplot as plt
import BPSK

random_message = Rand.random_bit_generator(100)
modulated_message, base_func_1, base_func_0 = BPSK.binary_phase_shift_keying_modulator(random_message,10,20)
window_size=int(modulated_message.size/len(random_message))
demodulated_message=BPSK.binary_phase_shift_keying_demodulator(modulated_message, base_func_1, base_func_0,window_size)

print('hi')
