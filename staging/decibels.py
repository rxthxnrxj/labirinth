import librosa
import numpy as np


filename = input("Enter audio file name to create model with: ")
parseName = "./recordings/"+filename+".wav"


x, sr = librosa.load(parseName)

# frequency
n_fft = 2048
# short term fourier transform. Time domain to frequency domain
s = librosa.stft(x, n_fft, hop_length=n_fft//2)
print(s.shape)

print("STFT Results: ")
print(s)

# convert to db to find the optimal value
# spectral input from stft to db using the formula: 20 * log10(amp / amp_ref)
# here, done using library

dec = librosa.amplitude_to_db(np.abs(s), ref=np.max)

print("Decibel array: ", abs(dec))


print(len(dec))

count = 0
for i in abs(dec):
    if max(i) < 80:
        count += 1

print(count)
print("Highest decibel noticed: ", np.max(abs(dec)))

nonMute = librosa.effects.split(x, top_db=30)
print("Non mute locations in the provided audio: ", nonMute)


def displayTime(startFrame, endFrame):
    return np.round(startFrame/sr, 3), np.round(endFrame/sr, 3)


timestamp = []

print("Time frames of nonMute audio: ")
for i in nonMute:
    temp = []
    a, b = displayTime(i[0], i[1])
    temp.append(a)
    temp.append(b)
    timestamp.append(temp)

print(timestamp)
print(len(timestamp))
