from tkinter import *
import tkinter.ttk as ttk

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack()

        #self.quit_bt = Button(self, text='quite', 
        #                      command=self.quit)
        #self.quit_bt.pack(side=LEFT)

        #self.hello_bt = Button(self, text='hello', command=self.hello)
        #self.hello_bt.pack(side=LEFT)

        self.tree = ttk.Treeview(self)
        self.tree.pack()
        root_node = self.tree.insert('', 'end', text='root', open=True)
        self.tree.insert(root_node, 'end', text='child', open=False)

        self.start_bt = Button(self, text='start', command=self.hello)
        self.start_bt.pack()

    def hello(self):
        node = self.tree.focus()
        print(self.tree.item(node))

root = Tk()

app = App(root)
#root.mainloop()
