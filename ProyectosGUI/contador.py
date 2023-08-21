from tkinter import *
from tkinter import ttk


class Program():
    def __init__(self) -> None:
        self.window = Tk()
        self.window.geometry("430x100")
        self.window.title("ContCreciente")
        self.window.resizable(0,0)
        self.createWidgets()
        self.window.mainloop()
    
    def count_sum(self):
        self.count = self.num_inp.get()
        self.count = int(self.count)
        self.count+=1
        self.num_inp.config(state=NORMAL)
        self.num_inp.delete(0,END)
        self.num_inp.insert(0, self.count)
        self.num_inp.config(state="readonly")
    
    def count_sub(self):
        self.count = self.num_inp.get()
        self.count = int(self.count)
        self.count-=1
        self.num_inp.config(state=NORMAL)
        self.num_inp.delete(0,END)
        self.num_inp.insert(0, self.count)
        self.num_inp.config(state="readonly")
    
    def count_reset(self):
        self.num_inp.config(state=NORMAL)
        self.num_inp.delete(0,END) 
        self.num_inp.insert(0,0)
        self.num_inp.config(state="readonly")

        

    def createWidgets(self):
        self.cont_lab = ttk.Label(self.window, text="Contador")
        self.cont_lab.grid(row=0, column=0, pady=30, padx=10)

        self.num_inp = ttk.Entry(self.window, width=10)
        self.num_inp.insert(0, 0)
        self.num_inp.config(state="readonly")
        self.num_inp.grid(row=0, column=1,pady=30, padx=5)

        self.add_button = ttk.Button(self.window,text="Count Up")
        self.add_button.grid(row=0,column=3,pady=30,padx=5)
        self.add_button.config(command=self.count_sum)

        self.sub_button = ttk.Button(self.window,text="Count Down")
        self.sub_button.grid(row=0,column=4,pady=30,padx=5)
        self.sub_button.config(command=self.count_sub)

        self.reset_button = ttk.Button(self.window,text="Reset", command=self.count_reset)
        self.reset_button.grid(row=0,column=5,pady=30,padx=5)


def main():
    App = Program()


if __name__ == '__main__':
    main()
