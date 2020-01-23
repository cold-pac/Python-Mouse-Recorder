import random
import time
from pynput.mouse import *
import pickle

mouse = Controller()

print("plays back a randomly selected recording from the recording library, infinite times")

infile = open('recording_storage', 'rb')
recording_library = pickle.load(infile)
infile.close()


time.sleep(1)

while True:
    random_index = str(random.randrange(0,len(recording_library.keys())))
    print(random_index)
    random_recording = recording_library[random_index]
    for y in random_recording:
        if isinstance(y, tuple):
            mouse.position = y
            time.sleep(0.001)
        else:
            if y[1]:
                mouse.press(y[0])
            else:
                mouse.release(y[0])