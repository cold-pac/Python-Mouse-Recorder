from pynput.mouse import *
import time
import pickle
import math 
import threading

mouse = Controller()

time.sleep(1)

mouse_movements = []

def gFunc():
    while mouse.position[1] < 725:
        mouse_movements.append(mouse.position)
        time.sleep(0.01)

get_mouse_pos = threading.Thread(target = gFunc) #the thread's target is executed when the thread starts
get_mouse_pos.daemon = True #will exit once all processes are finished, Listener thread is also a daemon
get_mouse_pos.start()


def on_move(x, y):
    if mouse.position[1] >= 725:
        # Stop listener
        return False #OK so returning False stops a listener

def on_click(x, y, button, pressed):
    mouse_movements.append([button, pressed])

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=None) as listener:
    listener.join()

time.sleep(1) #sleep for 1 second(s)

filename = 'mouse_recording_output_file'
outfile = open(filename, 'wb')
pickle.dump(mouse_movements, outfile)
outfile.close()

