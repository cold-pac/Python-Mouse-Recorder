from pynput.mouse import *
import time
import pickle
import threading
import os.path

mouse = Controller()

time.sleep(1)

mouse_movements = []


def gFunc():
    while mouse.position[0] < 1120 or mouse.position[1] < 725:
        mouse_movements.append(mouse.position)
        time.sleep(0.001)


get_mouse_pos = threading.Thread(target=gFunc)  # the thread's target is executed when the thread starts
get_mouse_pos.daemon = True  # will exit once all processes are finished, Listener thread is also a daemon
get_mouse_pos.start()


def on_move(x, y):
    if mouse.position[0] >= 1120 and mouse.position[1] >= 725:
        # Stop listener
        return False  # OK so returning False stops a listener


def on_click(x, y, button, pressed):
    mouse_movements.append([button, pressed])


# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=None) as listener:
    listener.join()

time.sleep(1)  # sleep for 1 second(s)

filename = 'most_recent_mouse_recording'
outfile = open(filename, 'wb')
pickle.dump(mouse_movements, outfile)
outfile.close()

filename2 = 'recording_storage'

if os.path.isfile(filename2):
    print("recording storage file already exists")
    infile = open(filename2, 'rb')
    recording_library = pickle.load(infile)
    infile.close()
    print("this is the recording library before insertion {}".format(recording_library))
    print("recording library keys {}".format(recording_library.keys()))
    recording_library[str(len(recording_library.keys()))] = mouse_movements
    print("this is the recording library after insertion {}".format(recording_library))
    print("recording library keys {}".format(recording_library.keys()))
    outfile2 = open(filename2, 'wb')
    pickle.dump(recording_library, outfile2)
    outfile2.close()
else:
    print("file doesn't exist yet")
    recording_library = {}
    recording_library['0'] = mouse_movements
    outfile2 = open(filename2, 'wb')
    pickle.dump(recording_library, outfile2)
    outfile2.close()
