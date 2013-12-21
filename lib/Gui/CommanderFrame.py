import os, sys, shutil
sys.path.append(os.path.abspath('../'))

from tkinter import *
import tkinter.ttk as ttk
from Gui.NetworkTreeView import NetworkTreeView

class CommanderFrame(Frame):
    def __init__(self, master, tree):
        super(CommanderFrame, self).__init__(master)

        ntv = NetworkTreeView(self, tree)
        ntv.pack(side=LEFT)
        
        attach_bt = Button(self, text='attach', command=ntv.attach)
        attach_bt.pack(side=RIGHT)
        
        
        
def main():


    tree = {
        'lxc_0': {'da_0': 'TorDA', 'container': 'Lxc_0'},
        'lxc_1': {'da_1': 'TorDA', 'container': 'Lxc_1'}
    }

    root = Tk()
    frame = CommanderFrame(root, tree)
    frame.pack()


if __name__ == '__main__':
    main()
