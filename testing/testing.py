from scipy.fftpack import fft
import numpy as np
import librosa.display
import librosa

from pydub import AudioSegment

dictionary = {'EH': 133.6862206923443, 'K': 115.41681757952966, 'S': 166.3766182986707, 'L': 246.24666602711073, 'AH': 550.9053733200344, 'M': 163.75147076461985, 'EY': 64.22858384983478, 'SH': 135.25021599927993, 'N': 67.85560738344809, 'P': 51.2815473440188, 'OY': 61.862942546575546, 'T': 223.9305821258729, 'OW': 153.13722949769465, 'Z': 120.17002626981548, 'W': 167.5091249640809, 'D': 230.00239979309444, 'B': 57.08598756681616, 'V': 150.97755339586604, 'IH': 169.0366257795551,
              'HH': 399.70197167172057, 'AE': 9.786848284547453, 'AA': 143.30905102852168, 'R': 153.70890200491695, 'AW': 95.68533144146848, 'AY': 118.64637180566885, 'ER': 129.40138649488117, 'F': 87.55752520824709, 'IY': 210.91308102765103, 'AO': 38.79238385649154, 'Y': 10.970079382986441, 'UW': 593.3626115779267, 'G': 46.327043296902, 'NG': 46.967571218986194, 'TH': 33.972669932758336, 'DH': 311.4802923015342, 'UH': 83.82096180510632, 'CH': 105.37202805634627, 'ZH': 468.3467434419365, 'JH': 29.776896400153408}

ids = dictionary.values()


filename = input("Enter audio file name to predict input with: ")
parseName = "./recordings/test/"+filename+".wav"

audio, sr = librosa.load(parseName)
audioseg = AudioSegment.from_wav(parseName)

duration = (1/sr)*len(audio)


kf = []
c = 0
for i in range(5):
    temp=[]
    c += float(duration/5)
    if i==0:
        temp.append(0)
    else:
        temp2=kf[-1]
        temp.append(temp2[-1])
    temp.append(c)
    kf.append(temp)


start = " "
word = ""

j=1

for i in kf:
    start=i[0]*1000
    end = i[1]*1000  # pydub works in millisec
    audio_chunk = audioseg[start:end]
    nextParser="./recordings/test/test_chunks/audio_test_chunk_{}.wav".format(j)
    audio_chunk.export( nextParser, format="wav")

    audio_process, sr = librosa.load(nextParser)
    ft = np.fft.fft(audio_process)
    mag_spec = np.array(np.abs(ft))
    comp = max(mag_spec)
    pred = min(ids, key=lambda x: abs(x-comp))
    for k, v in dictionary.items():
        if v == pred:
            word += k
            word+=" "
    j+=1


print("\nPredicted phoenetic sequence: ")
print(word)
