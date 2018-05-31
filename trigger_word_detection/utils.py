import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
from pydub import AudioSegment

# Calculate and plot spectrogram for a wav audio file
def gen_spectrogram(wav_file):

    rate, data =  wavfile.read(wav_file)

    nfft = 200 # Length of each window segment
    fs = 8000 # Sampling frequencies
    noverlap = 120 # Overlap between windows

    nchannels = data.ndim

    if nchannels == 1:
        pxx, freqs, bins, im = plt.specgram(data, nfft, fs, noverlap = noverlap)
    elif nchannels == 2:
        pxx, freqs, bins, im = plt.specgram(data[:,0], nfft, fs, noverlap = noverlap)
    return pxx

# Load raw audio files for speech synthesis
def load_raw_audio():

    trigger_words = []
    backgrounds = []
    non_trigger_words = []

    for filename in os.listdir("./data/raw/trigger_words"):
        if filename.endswith("wav"):
            trigger_word = AudioSegment.from_wav("./data/raw/trigger_words/"+filename)
            trigger_words.append(trigger_word)

    for filename in os.listdir("./data/raw/backgrounds"):
        if filename.endswith("wav"):
            background = AudioSegment.from_wav("./data/raw/backgrounds/"+filename)
            backgrounds.append(background)

    for filename in os.listdir("./data/raw/non_trigger_words"):
        if filename.endswith("wav"):
            non_trigger_word = AudioSegment.from_wav("./data/raw/non_trigger_words/"+filename)
            non_trigger_words.append(non_trigger_word)

    return trigger_words, non_trigger_words, backgrounds
