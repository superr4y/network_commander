import os, sys, shutil, time
sys.path.append(os.path.abspath('../'))
import subprocess as sp

from tkinter import *
import tkinter.ttk as ttk
from Gui.NetworkTreeView import NetworkTreeView

class CommanderFrame(Frame):
    def __init__(self, master, tree):
        super(CommanderFrame, self).__init__(master)

        Label(self, text='Network Tree View', bg='green',
              font=('Helvetica', 16)).grid(row=0, column=0,
                      sticky=W+E)

        self.ntv = NetworkTreeView(self, tree, self)
        self.ntv.grid(row=1, column=0, rowspan=3)

        #self.rowconfigure(3, minsize=20)
        

        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=1, column=1, rowspan=3, sticky=N+S)
        self.scrollbar.config(command=self.ntv.yview)
       
        
        # info panel
        Label(self, text='Info Panel', bg='green', # image=self.icon,
              font=('Helvetica', 16)).grid(row=0, column=1, columnspan=4, 
                     sticky=N+S+W+E )
        kwargs = {'bg': 'white', 'width':30, 'anchor': 'w'}
        info_panel = Frame(self)
        info_panel.grid(row=1, column=2, columnspan=3, sticky=N+S+W+E)

        self.ip_info = Label(info_panel, text='ip_info', **kwargs)
        self.state_info = Label(info_panel, text='state_info', **kwargs)
        self.obj_info = Label(info_panel, text='obj_info', **kwargs)
        self.ip_info.grid(row=1, column=0)
        self.state_info.grid(row=2, column=0)
        self.obj_info.grid(row=3, column=0)

        # control buttons
        bt_panel = Frame(self)
        bt_panel.grid(row=2, column=2, sticky=W+E)

        start_bt = Button(bt_panel, text='start', command=self.start)
        stop_bt  = Button(bt_panel, text='stop', command=self.stop)
        gen_bt   = Button(bt_panel, text='gen data', command=self.gen_data)
        gen_stop_bt = Button(bt_panel, text='stop gen', comman=self.stop_gen_data)

        start_bt.grid(row=0, column=0, sticky=W+E)
        stop_bt.grid(row=0, column=1, sticky=W+E)
        gen_bt.grid(row=1, column=0, sticky=W+E)
        gen_stop_bt.grid(row=1, column=1, sticky=W+E)
        
        

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

    def gen_data(self):
        sp.Popen('python /home/user/bin/nlxcm/nlxcm.py gen_data', shell=True)

    def stop_gen_data(self):
        sp.Popen('kill $(ps aux | grep -v grep | grep "python gen_data.py" | awk \'{print $2}\')', shell=True)
