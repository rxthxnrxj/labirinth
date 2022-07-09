## Lab(i)rinth

Conversations are key to exchange of thoughts, ideas and listening to each other. We cannot imagine a life without conversing. But not everyone is gifted with that comfort. Whatever we speak, can be divided into fundamental phonetics that make up the overall sound of any basic word.  And each phonetic is mapped with a particular frequency an individual is able to vibrate at. But, as said earlier, few people, for example, autistic people, try pronouncing words in their own range of frequencies which does not satisfy the levels required for an actual pronunciation. 

So, our aim was to create an aid for this problem statement.  We collected the universal words and their respective phonetics and proceeded to filter out only the unique phonetics present. Now, a context implementing all the phonetics with day-to-day words was created.

The person is now required to record (which is also in-built in code) by pronouncing all the words in the specified order. We get this and use further techniques like STFT, FFT, Threshold filtering to map their frequency to that respective phonetic. Thus, in the future, when an unknown audio input of the partially dumb person is given, the word they’re actually trying to pronounce can be predicted with this process and its phonetic representation is displayed.

## Concepts:
1.	STFT (Short Time Fourier Transform): As the input given to the system is a sequence of words all together. We have to first split the sequence into words into chunks of audio and later separate out the phonetic associated with it. For this, STFT is used to determine the sinusoidal frequency of local sections
    1.1 The procedure for computing STFTs is to divide a longer time signal into shorter segments of equal length and then compute the Fourier transform separately on each shorter segment.
2. Filtering: The spectral input from STFT is later fed into a function that calculated the decibels from the amplitude using the formula: dB = 20 * log10(amplitude)
    2.1 Further, non-mute areas are identified and filtered into timestamps by dividing the timeframe with sampling rate.
3.  Down Sampling: The number of samples of a audio file is reduced without losing the features of it’s originality. 
    3.1 Down sampling is done to speed up the following FFT process by reducing the number of samples
4.	FFT (Fast Fourier Transform): Using FFT, the audio signal which we have as chunks, only the phonetic part is split and FFT is applied over that time domain signal. After FFT, the time domain signal is now obtained in frequency domain which does justice to the process of predicting.
    4.1	Now, the fundamental frequency of the resultant FFT is calculated and mapped to the respective phonetic it’s supposed to represent
    4.2	x[K]=∑n=0N−1x[n]WnkN (library was used for implementation)
5.	Thresholding: Once the mapping is done, for the working of this system, any test audio of the person is given as an input, where Thresholding is performed to only find the significant parts of the input and further work on this result.
