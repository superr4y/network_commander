from tkinter import *
import tkinter.ttk as ttk
import subprocess as sp


class NetworkTreeView(ttk.Treeview):
    def __init__(self, master, tree):
        super(NetworkTreeView, self).__init__(master)

        self.tree = tree

        network = self.insert('', 'end', text='network', open=True)
        for k, v in tree.items():
            text = k
            lxc_node = self.insert(network, 'end', text=text, open=False)
            for kk, vv in v.items():
                if kk == 'container':
                    continue
                self.insert(lxc_node, 'end', text=kk, open=False)
                


    def get_selected_container(self):
        k = self.item(self.focus())['text']
        return self.tree[k]['container']

    def attach(self):
        node = self.get_selected_container()
        cmd = node.attach(execute=False)
        sp.Popen('gnome-terminal -e "{0}"'.format(cmd), shell=True)
        #sp.Popen('gnome-terminal -e "{0}"'.format('bash'), shell=True)
        




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


        
