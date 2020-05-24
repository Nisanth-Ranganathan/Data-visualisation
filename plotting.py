
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from csv import *
import pandas as pd


#creating label
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Browse")
        self.geometry("200x200")
        self.labelFrame = LabelFrame(self, text="Open File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.Button()
    def Button(self):
        self.button = Button(self.labelFrame, text="Browse A File", command=self.fileDialog)
        self.button.grid(column=1, row=1)

    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir="/C", title="Select A File", filetype=
        (("csv files", "*.csv"), ("all files", "*.*")))
        self.label = Label(self.labelFrame, text="Choose The File")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)
        self.button = Button(self, text="Submit", command=self.widget)
        self.button.grid(column=0, row=4)


    def widget(self):

        # open file in read mode
        global column_names
        with open(self.filename, 'r') as read_obj:
            # pass the file object to DictReader() to get the DictReader object
            csv_dict_reader = DictReader(read_obj)
            # get column names from a csv file
            column_names = csv_dict_reader.fieldnames
            print(column_names)
        self.widget1()


    def widget1(self):
        self.widget=Tk()
        self.widget.title("Visualisation")
        self.widget.geometry("300x300")
        global tkvar
        global tzvar
        with open(self.filename, 'r') as read_obj:
            # pass the file object to DictReader() to get the DictReader object
            csv_dict_reader = DictReader(read_obj)
            # get column names from a csv file
            self.column_names = csv_dict_reader.fieldnames
        tkvar = StringVar(self.widget)
        choices = self.column_names
        tkvar.set(self.column_names[0])
        self.label3 = Label(self.widget, text="Xlabel")
        self.label3.grid(column=0, row=0, padx=5, pady=5)
        popupMenu = OptionMenu(self.widget, tkvar, *choices)
        popupMenu.config(width=20)
        popupMenu.grid(row=1, column=0,padx=5,pady=5)
        self.label4 = Label(self.widget, text="Ylabel")
        self.label4.grid(column=0, row=2, padx=5, pady=5)
        tzvar = StringVar(self.widget)
        tzvar.set(self.column_names[0])
        popupMenu1 = OptionMenu(self.widget, tzvar, *choices)
        popupMenu1.config(width=20)
        popupMenu1.grid(row=3, column=0, padx=5, pady=5)
        plotbutton=Button(self.widget,text="Plot",command=self.plot,width=15)
        plotbutton.grid(row=4,column=0)
    def plot(self):
        fig = plt.figure()
        df = pd.read_csv(self.filename)
        numbers = df[tkvar.get()]
        paths = df[tzvar.get()]
        plt.bar(numbers,paths )
        plt.xticks(rotation=90)

        savebutton = Button(self.widget, text="Save", command=self.Save, width=15)
        savebutton.grid(row=5, column=0, padx=5, pady=5)
        plt.show()
    def Save(self):
        self.filename1 = filedialog.asksaveasfilename(initialdir="/C", title="Select A File", filetype=
        (("png files", "*.png"), ("all files", "*.*")))
        plt.savefig(self.filename1, dpi=300, bbox_inches='tight',edgecolor='red')
        print(self.filename1)

root = Root()
root.mainloop()
