import numpy as np
import Random_Bit_Generator as Rand
import plotly.express as px
import pandas as pd
import BPSK

random_message = Rand.random_bit_generator(100)
modulated_message, base_func_1, base_func_0 = BPSK.binary_phase_shift_keying_modulator(random_message,100)
window_size=int(modulated_message.size/len(random_message))
demodulated_message=BPSK.binary_phase_shift_keying_demodulator(modulated_message, base_func_1, base_func_0,window_size)
errors=sum(1 for a, b in zip(random_message, demodulated_message) if a != b)
index_array=[]
for i in range(0,modulated_message.size):
    index_array.append(i)
index_array=np.array(index_array)
df=pd.DataFrame(modulated_message)
df.columns=['Modulated']
df['X']=index_array
df['One_Base']=np.multiply(base_func_1,modulated_message)
df['Zero_Base']=np.multiply(base_func_0,modulated_message)
df['Carrier']=base_func_0
fig=px.line(data_frame=df,
        x='X',
        y='Modulated')
fig.show()
fig=px.line(data_frame=df,
            x='X',
            y='One_Base')
fig.show()
fig=px.line(data_frame=df,
            x='X',
            y='Zero_Base')
fig.show()
fig=px.line(data_frame=df,
            x='X',
            y='Carrier')
fig.show()
print('hi')
