from pydub import AudioSegment

filename = input("Enter audio file name to create model with: ")
parseName = "./recordings/"+filename+".wav"


audio = AudioSegment.from_wav(parseName)

ts=[[1.068, 2.067], [2.902, 3.181], [3.228, 3.344], [4.087, 4.621], [5.457, 6.153], [6.943, 7.732], [8.591, 9.543], [10.217, 10.82], [11.331, 12.167], [12.794, 13.653], [14.582, 15.418], [16.231, 17.252], [18.344, 19.18], [19.969, 20.643], [21.455, 22.314], [22.825, 23.87], [24.358, 25.17], [25.681, 26.657], [27.051, 27.841], [28.375, 29.234], [29.698, 30.674], [31.347, 32.369], [32.926, 33.437], [33.53, 33.692], [34.249, 34.853], [35.48, 36.409], [36.943, 37.895], [38.568, 39.311], [39.869, 40.588], [41.262, 42.191], [42.794, 43.236], [43.282, 43.584], [43.63, 43.746], [44.397, 44.977], [45.79, 46.533], [47.09, 48.112], [48.623, 49.691], [50.527, 51.084], [51.711, 52.245], [52.338, 52.431], [53.22, 53.731], [53.824, 53.917], [54.66, 55.519], [56.169, 57.191], [57.887, 59.025]]

parser=1

for i in ts:
    start=i[0]*1000
    end=i[1]*1000
    audio_chunk=audio[start:end]
    audio_chunk.export( "./recordings/chunks/chunk_{}.wav".format(parser), format="wav")
    parser+=1

print("COMPLETED")

# list_of_timestamps = [ 10, 20, 30, 40, 50 ,60, 70, 80, 90 ] #and so on in *seconds*`

# start = ""
# for  idx,t in enumerate(list_of_timestamps):
#     #break loop if at last element of list
#     if idx == len(list_of_timestamps):
#         break

#     end = t * 1000 #pydub works in millisec
#     print "split at [ {}:{}] ms".format(start, end)
#     audio_chunk=audio[start:end]
#     audio_chunk.export( "./recordings/chunks/audio_chunk_{}.wav".format(end), format="wav")

#     start = end * 1000 #pydub works in millisec`
