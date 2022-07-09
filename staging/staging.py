from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play


filename = input("Enter audio file name to create model with: ")
parseName = "./recordings/"+filename+".wav"

sound_file = AudioSegment.from_wav(parseName)


if sound_file:
    print("-- Successfully fetched audio --")

print("\nPlaying the audio clip... ")
play(sound_file)

audio_chunks = split_on_silence(sound_file,
                                # must be silent for at least half a second
                                min_silence_len=100,
                                silence_thresh=0
                                )


for i, chunk in enumerate(audio_chunks):

    out_file = "./recordings/chunks/chunk{0}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")
