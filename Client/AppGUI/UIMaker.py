from tkinter import *

def CreateFrame(parent, width, height, color, fix, packtype) :
    if(width == -1 or height == -1):
        frame = Frame(parent, relief = FLAT, bd = 0, bg = color)
        if width != -1:
            frame['width'] = width
        elif height != -1:
            frame['height'] = height
    else:
        frame = Frame(parent, relief = FLAT, width = width, height = height, bd = 0, bg = color)
    if(type == 'g') :
        if(fix):
            frame.grid_propagate(0)
        else:
            frame.grid_propagate(1)
    if(type == 'p') :
        if(fix):
            frame.pack_propagate(0)
    else:
            frame.pack_propagate(1)
    return frame

def CreateFixedFrame(parent, width, height, color, pack):
        frame = Frame(parent, bd = 0, bg = color)
        if width > 0 :
            frame['width'] = width
        if height > 0 :
            frame['height'] = height
        if pack == 'g' :
            frame.grid_propagate(0)
        if pack == 'p' :
            frame.pack_propagate(0)
        return frame

def PackFix(frame, side, fill, expand):
            frame.pack(side = side, fill = fill, expand = expand)
            frame.pack_propagate(0)
            return frame

def ImageLabel(parent, image, bg):
            return Label(parent, image = image, bg = bg, bd = 0)

def TextLabel(parent, text, font, col, bg):
            return Label(parent, text = text, font = font, fg = col, bg = bg, bd = 0)
