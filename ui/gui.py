# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.create_input()
        self.create_output()
        self.create_controls()

    def create_input(self):
        # variables
        self.p_type = tk.StringVar()
        self.p_type.set("Custom")
        self.p_type.trace_add("write", self.p_type_update)
        self.p_temp = tk.IntVar()
        self.p_temp.set(295)
        self.p_hydro = tk.IntVar()
        self.p_hydro.set(70)
        self.p_grav = tk.DoubleVar()
        self.p_grav.set(1.0)

        self.in_f = tk.Frame(self, bd=3)
        self.in_f.grid(row=0, column=0)

        self.planet_f = tk.LabelFrame(self.in_f, text="Planet", padx=5, pady=5)
        self.planet_f.grid(row=0, column=0)

        tk.Label(self.planet_f, text="Planet Type:").grid(row=0, column=0)
        self.in_p_type = tk.OptionMenu(self.planet_f, self.p_type,
                                       "Custom", "Earthlike", "Gas Giant")
        self.in_p_type.grid(row=0, column=1)

        tk.Label(self.planet_f, text="Temperature (Kelvin):").grid(row=1, column=0)
        self.in_p_temp = tk.Entry(self.planet_f, textvariable=self.p_temp)
        self.in_p_temp.grid(row=1, column=1)

        tk.Label(self.planet_f, text="Hydrographic Coverage (%): ").grid(row=2, column=0)
        self.in_p_hydro = tk.Entry(self.planet_f, textvariable=self.p_hydro)
        self.in_p_hydro.grid(row=2, column=1)

        tk.Label(self.planet_f, text="Gravity (G): ").grid(row=3, column=0)
        self.in_p_grav = tk.Entry(self.planet_f, textvariable=self.p_grav)
        self.in_p_grav.grid(row=3, column=1)

    def create_output(self):
        self.out_f = tk.Frame(self, bd=3, relief=tk.SUNKEN)
        self.out_f.grid(row=0, column=1)

        self.out_text = tk.Text(self.out_f)
        self.out_text.grid(row=0, column=0)

    def create_controls(self):
        self.controls = tk.Frame(self, bd=3)
        self.controls.grid(row=1, columnspan=2)

        tk.Label(self.controls,
                 text="Number of Species to Generate:").grid(row=0, column=0)
        self.in_num = tk.Scale(self.controls, from_=1)
        self.in_num.grid(row=0, column=1)

        self.gen_button = tk.Button(self.controls, text="Generate!",
                                    command=self.species_gen)
        self.gen_button.grid(row=0, column=2)

    def p_type_update(self, *args):
        print("p_type_update Callback: ", args)
        value = self.p_type.get()
        if value in ["Custom", "Gas Giant"]:
            self.in_p_temp.config(state=tk.NORMAL)
            self.in_p_hydro.config(state=tk.NORMAL)
            self.in_p_grav.config(state=tk.NORMAL)
        elif value == "Earthlike":
            self.in_p_temp.config(state=tk.NORMAL)
            self.in_p_hydro.config(state=tk.NORMAL)
            self.in_p_grav.config(state=tk.NORMAL)
            self.p_temp.set(295)
            self.p_hydro.set(70)
            self.p_grav.set(1.0)
            self.in_p_temp.config(state=tk.DISABLED)
            self.in_p_hydro.config(state=tk.DISABLED)
            self.in_p_grav.config(state=tk.DISABLED)

    def species_gen(self):
        text = self.p_type.get()
        self.out_text.config(state=tk.NORMAL)
        self.out_text.delete(1.0, tk.END)
        for _ in range(self.in_num.get()):
            self.out_text.insert(tk.END, text)
            self.out_text.insert(tk.END, "\n")
        self.out_text.config(state=tk.DISABLED)


def run_gui():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    run_gui()
