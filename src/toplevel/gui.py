import tkinter as tk
from class_dec import *

class GUI(tk.Tk):#class inherents tk to make things a bit easier
    def __init__(self):
        super().__init__()#python inheratence bullshit

        #setup window
        self.window()

        #frame decs
        title : tk.Frame = self.header()
        python: tk.Frame = self.python()
        c: tk.Frame = self.c()
        kotlin: tk.Frame = self.kotlin()
        control: tk.Frame = self.control()

        #packalot
        title.pack()
        python.pack()
        c.pack()
        kotlin.pack()
        control.pack(side = tk.BOTTOM)

    def window(self) -> None:
        self.geometry("400x400")
        self.title("74181 Emulator")
        self.configure(background= 'gray')

    def header(self) -> tk.Frame:
        title_frame: tk.Frame = tk.Frame(self)

        return title_frame

    def python(self) -> tk.Frame:
        python_frame = tk.Frame(self)

        name_label: tk.Label= tk.Label(python_frame, text="Python Time:")
        name_label.pack(side = tk.LEFT)

        time_label: tk.Label = tk.Label(python_frame, text= self.get_status(python))
        time_label.pack(side = tk.RIGHT)

        return python_frame

    def c(self) -> tk.Frame:
        c_frame = tk.Frame(self)

        name_label: tk.Label= tk.Label(c_frame, text="C Time:")
        name_label.pack(side = tk.LEFT)

        time_label: tk.Label = tk.Label(c_frame, text= self.get_status(c))
        time_label.pack(side = tk.RIGHT)

        return c_frame

    def kotlin(self) -> tk.Frame:
        kotlin_frame = tk.Frame(self)

        name_label: tk.Label= tk.Label(kotlin_frame, text="Kotlin Time:")
        name_label.pack(side = tk.LEFT)

        time_label: tk.Label = tk.Label(kotlin_frame, text= self.get_status(kotlin))
        time_label.pack(side = tk.RIGHT)

        return kotlin_frame

    def control(self) -> tk.Frame:
        control_frame: tk.Frame = tk.Frame(self)

        start_button: tk.Button = tk.Button(control_frame,text= "Start")
        start_button.pack(side = tk.RIGHT)

        return control_frame

    def get_status(self, lang_in: lang_info) -> str:

        if(lang_in.is_running == True):
            return "Currently Running"
        else:
            return str(lang_in.time)
