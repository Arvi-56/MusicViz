import os
import aubio
import numpy as num
import pyaudio
import sys
import matplotlib.pyplot as plt
import warnings
import webbrowser

#How I dealt with annowing error
warnings.simplefilter("ignore", DeprecationWarning)
#sets the directory
path="/Users/ahks/Desktop/Schooled/Code2/Big Project"
os.chdir(path)
print (os.getcwd())
#launches visualizer
webbrowser.open('file://' + os.path.realpath("yall.html"))

# Some constants for setting the PyAudio and the
# Aubio.
BUFFER_SIZE             = 2048
CHANNELS                = 1
FORMAT                  = pyaudio.paFloat32
METHOD                  = "default"
SAMPLE_RATE             = 44100
HOP_SIZE                = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME    = HOP_SIZE

def main(args):
    #sets the first values to 0
    target = open('target.txt', 'w')
    target.write("0.0 0.000000\n")
    target.close()
    #creates counter to restrict how long the loop goes
    counter=0
    # Initiating PyAudio object.
    pA = pyaudio.PyAudio()
    # Open the microphone stream.
    mic = pA.open(format=FORMAT, channels=CHANNELS,
        rate=SAMPLE_RATE, input=True,
        frames_per_buffer=PERIOD_SIZE_IN_FRAME)

    # Initiating Aubio's pitch detection object.
    pDetection = aubio.pitch(METHOD, BUFFER_SIZE,
        HOP_SIZE, SAMPLE_RATE)
    # Set unit.
    pDetection.set_unit("Hz")
    # Frequency under -40 dB will considered
    # as a silence.
    pDetection.set_silence(-40)

    # loop!
    while counter<1000:
        # Always listening to the microphone.
        data = mic.read(PERIOD_SIZE_IN_FRAME)
        # Convert into number that Aubio understand.
        samples = num.fromstring(data,
            dtype=aubio.float_type)
        # Finally get the pitch.
        pitch = pDetection(samples)[0]
        # Compute the energy (volume)
        # of the current frame.
        volume = num.sum(samples**2)/len(samples)
        # Format the volume output so it only
        # displays at most six numbers behind 0.
        volume = "{:6f}".format(volume)
        # Finally print the pitch and the volume.
        output = print(str(pitch) + " " + str(volume))
        #writes and ovwerwrites to text file real-time
        target = open('target.txt', 'w')
        target.write(str(pitch) + " " + str(volume)+"\n")
        #target.flush()
        #target = open("yall.html").read().format(radius=volume)
        target.close()
        counter=counter+1
# plt.show()
if __name__ == "__main__": main(sys.argv)
