import librosa
import librosa.display
import IPython
import IPython.display as ipd
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns

audio_data = 'Капли_тест1.wav'
drop_value = 0.03
sr_value = 22050
duration_value = None # 25 drops in first 15 seconds
min_interval = 0.4
max_interval = 0.7
y, sr = librosa.load(audio_data, sr=sr_value, duration=duration_value)
z = y.copy()
intervals = []
drop_times = []
# print(len(y))
count = 0
print('Analizing...')
for i in range(len(y)):
    if y[i] > drop_value:
        time = i/sr
        drop_times.append(time)
        # minutes = (int(time)) // 60
        # print(minutes)
        # seconds = time - minutes * 60
        # count += 1
        # print(count)
        # print(str(count) + '.', 'time = ' + str(time), i,  y[i])
        # print(time, i,  y[i])
    # else:
        # z[i] = 0
plt.figure(figsize=(14, 5))
# ipd.Audio(audio_data)
librosa.display.waveshow(y, sr=sr)
# librosa.display.waveshow(z, sr=sr)
count = 0
for i in range(len(drop_times)):
    if i == 0:
        continue
    intervals.append(drop_times[i] - drop_times[i-1])
with open('data.csv', 'w') as f:
    for i in range(len(intervals)):
        if intervals[i] > min_interval and intervals[i] < max_interval:
            count += 1
            f.write(str(intervals[i]) + '\n')
            print(str(count) + '.', intervals[i])

# n_fft = 2048
# ft = np.abs(librosa.stft(y[:n_fft], hop_length = n_fft+1))
# plt.plot(ft)
# plt.title('Spectrum')
# plt.xlabel('Frequency Bin')
# plt.ylabel('Amplitude')
plt.show()

