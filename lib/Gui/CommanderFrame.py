import os, sys, shutil, time
sys.path.append(os.path.abspath('../'))
import subprocess as sp

from tkinter import *
import tkinter.ttk as ttk
from Gui.NetworkTreeView import NetworkTreeView

class CommanderFrame(Frame):
    def __init__(self, master, tree):
        super(CommanderFrame, self).__init__(master, bg='cyan')

        Label(self, text='Network Tree View', bg='green',
              font=('Helvetica', 16)).grid(row=0, column=0)

        self.ntv = NetworkTreeView(self, tree, self)
        self.ntv.grid(row=1, column=0, )
        

        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(sticky=E)
        self.scrollbar.config(command=self.ntv.yview)
       
        
        # info panel
        Label(self, text='Info Panel', bg='green', # image=self.icon,
              font=('Helvetica', 16)).grid(row=0, column=1)
        kwargs = {'bg': 'white', 'width':30}
        info_panel = Frame(self)
        info_panel.grid(row=1, column=1, sticky=NW)

        self.ip_info = Label(info_panel, text='ip_info', **kwargs)
        self.state_info = Label(info_panel, text='state_info', **kwargs)
        self.obj_info = Label(info_panel, text='obj_info', **kwargs)
        self.ip_info.grid(row=1, column=0, sticky=W)
        self.state_info.grid(row=2, column=0, sticky=W)
        self.obj_info.grid(row=3, column=0, sticky=W)

        # control buttons
        start_bt = Button(self, text='start', command=self.start)
        stop_bt  = Button(self, text='stop', command=self.stop)
        start_bt.grid(row=2, column=1)
        stop_bt.grid(row=2, column=2)
        
        



    def info_update(self, *args):
        lxcc = self.ntv.get_selected_container()
        if lxcc:
            self.ip_info.configure(text=lxcc.env['ip'])

            state = 'running' if lxcc.exe._is_running() else 'stopped'
            self.state_info.configure(text=state)

            self.obj_info.configure(text=str(lxcc.commanders[0]))
            
        
    def start(self):
        '''
        TODO: this is just for testing
        '''
        sp.Popen('python /home/user/bin/nlxcm/nlxcm.py start', shell=True)

    def stop(self):
        '''
        TODO: same as start()
        '''
        sp.Popen('python /home/user/bin/nlxcm/nlxcm.py stop', shell=True)
