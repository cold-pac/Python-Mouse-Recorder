import time
from pynput.mouse import *
import pickle

mouse = Controller()

infile = open('mouse_recording_output_file', 'rb')
mouse_movements_copy = pickle.load(infile)
infile.close()

for y in mouse_movements_copy:
    if isinstance(y, tuple):
        mouse.position = y
        time.sleep(0.01)
    else:
        if y[1]:
            mouse.press(y[0])
        else:
            mouse.release(y[0])