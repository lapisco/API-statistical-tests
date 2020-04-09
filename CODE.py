# interface gráfica para testes estatísticos
from tkinter import *
# from tkFile import askopenfilename
from tkinter import ttk
from tkinter import filedialog
import statistical_tests as st
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
import numpy as np


class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()


    def init_window(self):
        self.master.title("Statistical Tests")
        self.pack(fill=BOTH,expand=1)
        self.configure(bg="black")




        load = Image.open("lapisco_logo.png")
        # rows,cols = load.shape[:2]
        # img = img.resize((rows/2, hsize), Image.ANTIALIAS)
        # load = load.resize(rows/2,cols/2)
        # img = Image.open(x)
        img = load.resize((300, 230), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.pack(fill=BOTH)

        # render = ImageTk.PhotoImage(load)
        # img = Label(self, image=render)
        # img.image = render
        # img.place(x=0, y=0)

        # photo = PhotoImage(file="/home/adriell/Documentos/TKinter_tests/lapisco_logo.png")
        # photoimage = photo.subsample(1, 2)
        # logo_button=Button(self,text ="click",image = photoimage,compound = LEFT)
        # logo_button.place(x=40,y=40)


        # color1 = 'green'
        # color2 = 'red'
        # global val1,val2
        # val1=None
        # val2=None
        path_file1 = Button(self,text="file1",command = self.filechoose1,bg="blue",foreground = 'white')
        path_file1.place(x=30,y=230)
        path_file2 = Button(self, text="file2",command=self.filechoose2,bg="blue",foreground = 'white')
        path_file2.place(x=90, y=230)
        example = Button(self, text="example",command = self.show_example,bg = "orange",foreground = 'white')
        example.place(x=30, y=270)
        exit = Button(self,text="Exit",command =self.Client_exit,bg ="red",foreground = 'white' )
        exit.place(x=250,y=280)
        # if (val1 != 0)and(val2!=0):
        #     color = color2
        # else:
        #     color =color1
        run=Button(self,text="run test",command = self.setalpha,bg="green",foreground = 'white')
        run.place(x=230,y=240)


    def Client_exit(self):
        exit()

    def filechoose1(self):
        Tk().withdraw()
        global filename1
        filename1 = filedialog.askopenfilename()
        print(filename1)
        return filename1
    def filechoose2(self):
        Tk().withdraw()
        global filename2
        filename2 = filedialog.askopenfilename()
        print(filename2)
        return filename2


    def show_example(self):
        img=cv2.imread("example.png")
        cv2.imshow("example_arq",img)
        cv2.waitKey(300)
        # plt.close()




    def setalpha(self):  # new window definition
        setalp = Toplevel(root)
        setalp.title('set alpha')
        setalp.geometry("300x100")
        setalp.resizable(0, 0)
        Label(setalp, text="Set Alpha Value after click on run test",fg = "red").grid(row=0)
        setalp.configure(bg="black")

        global e1
        # global tagg
        # tagg=2
        e1 = Entry(setalp)
        e1.grid(row=0, column=1)
        # test=int(e1)
        Button(setalp,text='show alpha value',command=self.show_alpha,bg = "blue",fg = "white").grid(row=3,column=0,sticky=W,pady=4)
        # Button(setalp, text='close_window', command=setalp.destroy).grid(row=4, column=0, sticky=W, pady=4)
        Button(setalp, text='run test', command=self.newWindow,bg = "green", fg = "white").grid(row=4, column=0, sticky=W, pady=4)
        # run = Button(self, text="run test", command=self.newWindow)
        # Label(setalp, text="after choosing the alpha value click on run test").grid(row=5)
        # run.place(x=160, y=160)

    def show_alpha(self):
        # print('alpha value:{}%'.format(e1.get()))
        rt = Tk()
        T = Text(rt, height=2, width=15)
        T.pack()
        T.insert(END,'alpha value:{}%'.format(e1.get()) )
        mainloop()


    def run_kolmogorov(self):
        st.kolmogorov(str(filename1), str(filename2), e1.get(), False)



    def run_T_student(self):
        st.studentst(str(filename1), str(filename2), e1.get(), False)

    def run_Friedman(self):
        st.friedman(str(filename1), str(filename2), e1.get(), False)

    def run_Bartlett(self):
        st.bartlett_test(str(filename1), str(filename2), e1.get(), False)

    def run_Levene(self):
        st.levene_test(str(filename1), str(filename2), e1.get(), False)

    def run_man_whitney(self):
        st.Mann_Whitney_test(str(filename1), str(filename2), e1.get(), False)

    def run_Ranksmus(self):
        st.ranksums_test(str(filename1), str(filename2), e1.get(), False)




    def newWindow(self):  # new window definition
        newwin = Toplevel(root)
        newwin.title('New Window')
        newwin.geometry("300x280")
        newwin.resizable(0, 0)
        newwin.configure(bg="black")

        display1 = Label(newwin, text="chose the statistical test!",fg="red")
        display1.pack()


        button1 = Button(newwin, text="Komolgorov", command=self.run_kolmogorov,bg = "blue",fg = "white")
        button1.place(x=30, y=75, width=100, height=25)

        button2 = Button(newwin, text="T-Student", command=self.run_T_student,bg = "blue",fg = "white")
        button2.place(x=180, y=75, width=100, height=25)

        button3 = Button(newwin, text="Friedman", command=self.run_Friedman,bg = "blue",fg = "white")
        button3.place(x=30, y=125, width=100, height=25)

        button4 = Button(newwin, text="Bartlett", command=self.run_Bartlett,bg = "blue",fg = "white")
        button4.place(x=180, y=125, width=100, height=25)

        button5 = Button(newwin, text="Levene", command=self.run_Levene,bg = "blue",fg = "white")
        button5.place(x=30, y=175, width=100, height=25)

        button6 = Button(newwin, text="Man Whitney", command=self.run_man_whitney,bg = "blue",fg = "white")
        button6.place(x=180, y=175, width=100, height=25)

        button7 = Button(newwin, text="Ranksmus", command=self.run_Ranksmus,bg = "blue",fg = "white")
        button7.place(x=105, y=225, width=100, height=25)








root=Tk()
# root.configure(bg="black")
root.geometry("300x300")
app=Window(root)
root.mainloop()
