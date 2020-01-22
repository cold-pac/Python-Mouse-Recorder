import _tkinter #low level interface to Tk, should never be used directly
import tkinter #public interface

# print(tkinter._test())

root = tkinter.Tk() #the root widget, must be created before any other widgets

w = tkinter.Label(root, text = "Hello World") #Label widget, a child to the root widget
#Label widget can display text, icon or image
w.pack() #calling the pack method on the Label widget

root.mainloop() #tkinter event loop
#program will stay in the event loop until we close the window 
