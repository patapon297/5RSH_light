import pyaudio
import sys
import wave
import cStringIO as StringIO

chunk = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
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
   
    for i in range(0, RATE / chunk * RECORD_SECONDS):      
        data = stream.read(chunk, exception_on_overflow = False)
        frames.append(data)

    # check for silence here by comparing the level with 0 (or some threshold) for
    # the contents of data.
    # then write data or not to a file

    print "* done"

    stream.stop_stream()
    stream.close()
    p.terminate()

    memory_file = StringIO.StringIO()
    waveFile = wave.open(memory_file, 'w')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(''.join(frames))
    waveFile.close()
    memory_file.close()
    return memory_file
