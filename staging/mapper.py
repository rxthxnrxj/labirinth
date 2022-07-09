import librosa
import numpy as np
import os
from pydub import AudioSegment
from pydub.playback import play

ph_dict_first={}
ph_dict_last={}

phoenetics=['EH', 'K', 'S', 'L', 'AH', 'M', 'EY', 'SH', 'N', 'P', 'OY', 'T', 'OW', 'Z', 'W', 'D', 'B', 'V', 'IH', 'HH', 'AE', 'AA', 'R', 'AW', 'AY', 'ER', 'F', 'IY', 'AO', 'Y', 'UW', 'G', 'NG', 'TH', 'DH', 'UH', 'CH', 'ZH', 
'JH']

j=0


# for root, dirs, files in os.walk('./recordings/chunks/'):
#     for file in files:
#         print(os.path.join(root, file))


for root, dirs, files in os.walk('./recordings/chunks/'):
    for file in files:
        print(j,"----------")
        parseName=os.path.join(root, file)
        
        audio = AudioSegment.from_wav(parseName)
        end=0.150*1000
        audio_chunk=audio[0:end]
        nextParser="./recordings/chunk_split/audio_chunk_split_{}.wav".format(j)
        audio_chunk.export( nextParser, format="wav")

        print("Playing audio chunk: ", j)
        play(audio_chunk)

        audio_process, sr = librosa.load(nextParser)
        ft = np.fft.fft(audio_process)
        mag_spec = np.array(np.abs(ft))
        ph_dict_first[phoenetics[j]]=max(mag_spec)
        j+=1

print("Final array: ", ph_dict_first)

# for i in audio_chunks:
#     parseName=os.path(i)
#     audio, sr = librosa.load(parseName)
#     ft = np.fft.fft(audio)
#     mag_spec = np.abs(ft)
#     ph_dict_first[phoenetics[j]]=np.gcd(mag_spec)
