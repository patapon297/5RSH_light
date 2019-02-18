import pyaudio
import sys
import wave

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 7

def record():

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=False,
                    frames_per_buffer=chunk)

    print "* recording"
    frames = []

    for i in range(0, 44100 / chunk * RECORD_SECONDS):
        data = stream.read(chunk)
        frames.append(data)
        # check for silence here by comparing the level with 0 (or some threshold) for
        # the contents of data.
        # then write data or not to a file

    print "* done"

    stream.stop_stream()
    stream.close()
    p.terminate()

    waveFile = wave.open("test.wav", 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()