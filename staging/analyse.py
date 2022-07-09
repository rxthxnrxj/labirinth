import librosa
import librosa.display

import matplotlib.pyplot as plt
import scipy.fftpack as sf
import scipy.signal as sig

from scipy.fftpack import fft 

import numpy as np

filename = input("Enter audio file name to create model with: ")
parseName = "./recordings/"+filename+".wav"

audio, sr = librosa.load(parseName)

sample_duration = 1/sr

print(sr, sample_duration)

plt.plot(audio)
plt.ylim(-1,1)
plt.title("Input audio signal")
plt.show()

# Spectral Analysis---------------------


def plot_mag_spectrum(signal, title, sr, freq_ratio=0.1):
    ft = np.fft.fft(signal)
    mag_spec = np.abs(ft)
    print("FFT result:", mag_spec)
    plt.figure(figsize=(15, 5))

    frequency = np.linspace(0, sr, len(mag_spec))
    no_freq_bins = int(len(frequency)*freq_ratio)

    plt.plot(frequency, mag_spec)
    plt.xlabel("Frequency")
    plt.title(title)

    plt.show()

    plt.plot(frequency[:no_freq_bins], mag_spec[:no_freq_bins])
    plt.xlabel("Frequency")
    plt.title(title+"- Nyquist")

    plt.show()


plot_mag_spectrum(audio, "Frequency plot ", sr)


# print(np.round(sample_duration,6))


# Calculating duration--------------------
# duration=sample_duration*len(audio)
# print("Duration of audio: ",np.round(duration,3),"sec")


# Plotting waveform-----------------------------------------
# plt.figure(figsize=(15, 10))

# plt.subplot(1,1,1)
# librosa.display.waveplot(audio)
# plt.title("Input audio: ")
# plt.ylim(-1,1)

# plt.subplot(2,2,1)
# plt.plot(audio_f)
# plt.title("FFT")
# plt.ylim(-1,1)

# plt.show()


# FRAME_SIZE=512
# HOP_LENGTH=256

# def amp_env(signal, frame_size, hop_length):
#     amplitude_envelope=[]

#     for i in range(0, len(signal), hop_length):
#         current_frame_amp_env=max(signal[i:i+frame_size])
#         amplitude_envelope.append(current_frame_amp_env)

#     return np.array(amplitude_envelope)


# res=amp_env(audio, FRAME_SIZE, HOP_LENGTH)

# print(len(res))
