from tkinter import *
import tkinter.ttk as ttk
import subprocess as sp
import re


class NetworkTreeView(ttk.Treeview):
    def __init__(self, master, tree, info_frame):
        super(NetworkTreeView, self).__init__(master)

        self.tree = tree
        self.info_frame = info_frame

        

        self.menu = Menu(self, tearoff=0)
        #self.menu.add_command(label='update', command=self.info_frame.info_update)
        self.menu.add_command(label='attach', command=self.attach_terminal)
        self.menu.add_command(label='wireshark', command=self.attach_wireshark)

        self.bind('<Button-3>', self.popup)
        self.bind('<ButtonRelease-1>', self.info_frame.info_update)

        self.icon = PhotoImage(file='/home/user/bin/network_commander/lib/Gui/tor.gif')
        self.icon = self.icon.subsample(5)


        network = self.insert('', 'end', text='network', open=True)
        for k, v in tree.items():
            text = k# + str(v['container'].commanders[0])
            pos = int(re.search(r'\d+', text).group(), 10)
            lxc_node = self.insert(network, pos, text=text, image=self.icon, open=False)

            for kk, vv in v.items():
                if kk == 'container':
                    continue
                self.insert(lxc_node, 'end', text=kk, open=False)
                


    def get_selected_container(self):
        try:
            k = self.item(self.focus())['text']
            return self.tree[k]['container']
        except KeyError as e:
            return None
    
    def xauth_sucker(self, node):
        # Get the cookie from ~/.Xauthority
        out = sp.Popen('su user -c "xauth list"', shell=True, stdout=sp.PIPE,
                       stdin=sp.PIPE).communicate(b'\n')
        out = out[0].decode(encoding='utf-8')
        cookie = re.search(r'MIT-MAGIC-COOKIE-1\s+(\S+)', out).group(1)
        
        # Set the cookie while attached to container
        cmd = '{0} -- su user -c "xauth add $DISPLAY . {1}"'.format(
            node.attach(execute=False), cookie)
        print(cmd)
        sp.Popen(cmd, shell=True, stdin=sp.PIPE).communicate(b'\n')
        
        # Share .Xauthority with root for wireshark,...
        sp.Popen('cp /home/user/.Xauthority /root/', shell=True)

        

    def attach_terminal(self):
        node = self.get_selected_container()
        cmd = node.attach(execute=False)
        # xterm -bg black -fg white  -e "su user; bash/"
        self.xauth_sucker(node)
        
        cmd = '{0} -- xterm -bg black -fg white -e "cd {1}; su user; bash"'.format(
            cmd, node.env['home_dir'])
        sp.Popen(cmd, shell=True)
    
    def attach_wireshark(self):
        node = self.get_selected_container()
        self.xauth_sucker(node)
        cmd = node.attach(execute=False)
        sp.Popen('{0} -- "wireshark"'.format(cmd), shell=True)
        
    def popup(self, event):
        if self.get_selected_container(): # is container selected?
            self.menu.tk_popup(event.x_root, event.y_root, 0)
    
    

def main():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    label = Label(frame, text='w0000t')
    label.pack() 

    tree = {
        'lxc_0': {'da_0': 'TorDA', 'container': 'Lxc_0'},
        'lxc_1': {'da_1': 'TorDA', 'container': 'Lxc_1'}
    }

    ntv = NetworkTreeView(frame, tree)
    ntv.pack()

    bt = Button(frame, text='attach', command=ntv.attach)
    bt.pack()


if __name__ == '__main__':
    main()


        
