# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk
import random
import copy

import aliengen.planetinfo as planet
import aliengen.species as species
import aliengen.tables as tables


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_variables()
        self.create_widgets()

    def create_variables(self):
        self.p_type = tk.StringVar()
        self.p_type.set("Custom")
        self.p_type.trace_add("write", self.trace_p_type)
        self.p_temp = tk.IntVar()
        self.p_temp.set(295)
        self.p_hydro = tk.IntVar()
        self.p_hydro.set(70)
        self.p_grav = tk.DoubleVar()
        self.p_grav.set(1.0)
        self.sapience = tk.StringVar()
        self.sapience.set("Possible")
        self.p_variation = tk.BooleanVar()
        self.p_variation.set(False)
        self.chem_bas = tk.StringVar()
        self.chem_bas.set("")
        self.hab_type = tk.StringVar()
        self.hab_type.set("")
        self.hab_type.trace_add("write", self.trace_hab_type)
        self.habitat = tk.StringVar()
        self.habitat.set("")
        self.habitat.trace_add("write", self.trace_habitat)
        self.troph = tk.StringVar()
        self.troph.set("")

    def create_widgets(self):
        self.create_input()
        self.create_output()
        self.create_controls()

    def create_input(self):
        self.in_f = tk.Frame(self, bd=3)
        self.in_f.grid(row=0, column=0)

        self.create_input_planet()

        sap_f = tk.LabelFrame(self.in_f, text="Sapience")
        sap_f.grid(row=1, column=0, sticky=tk.NSEW)
        tk.Radiobutton(sap_f, text="Possible", variable=self.sapience,
                       value="Possible").grid(row=0, column=0)
        tk.Radiobutton(sap_f, text="Sapient", variable=self.sapience,
                       value="Sapient").grid(row=1, column=0)
        tk.Radiobutton(sap_f, text="Nonsapient", variable=self.sapience,
                       value="Nonsapient").grid(row=2, column=0)

        per_f = tk.LabelFrame(self.in_f, text="Personality")
        per_f.grid(row=1, column=1, sticky=tk.NSEW)
        tk.Radiobutton(per_f, text="Biology-Based", variable=self.p_variation,
                       value=False).grid(row=0, column=0)
        tk.Radiobutton(per_f, text="More Varied", variable=self.p_variation,
                       value=True).grid(row=1, column=0)

        lbl_chem = tk.Label(self.in_f, text="Chemical Basis:")
        lbl_chem.grid(row=2, column=0)
        tbl_chem = [""] + tables.ui_chemical_basis
        self.in_chem_bas = tk.OptionMenu(self.in_f, self.chem_bas, *tbl_chem)
        self.in_chem_bas.grid(row=2, column=1)

        lbl_habtype = tk.Label(self.in_f, text="Habitat Type:")
        lbl_habtype.grid(row=3, column=0)
        tbl_habtype = [""] + tables.ui_hab_type
        tbl_habtype.remove("Gas Giant")
        self.in_habtype = tk.OptionMenu(self.in_f, self.hab_type, *tbl_habtype)
        self.in_habtype.grid(row=3, column=1)

        lbl_habitat = tk.Label(self.in_f, text="Habitat:")
        lbl_habitat.grid(row=4, column=0)
        tbl_habitat = [""] + tables.ui_habitat
        self.in_habitat = tk.OptionMenu(self.in_f, self.habitat, *tbl_habitat)
        self.in_habitat.grid(row=4, column=1)

        lbl_troph = tk.Label(self.in_f, text="Trophic Level:")
        lbl_troph.grid(row=5, column=0)
        tbl_troph = [""] + tables.ui_trophic_level
        self.in_troph = tk.OptionMenu(self.in_f, self.troph, *tbl_troph)
        self.in_troph.grid(row=5, column=1)

    def create_output(self):
        self.out_f = tk.Frame(self, bd=3, relief=tk.SUNKEN)
        self.out_f.grid(row=0, column=1)

        self.out_scroll = tk.Scrollbar(self.out_f)
        self.out_scroll.grid(row=0, column=1, sticky=tk.NS)

        self.out_text = tk.Text(self.out_f, yscrollcommand=self.out_scroll.set)
        self.out_text.grid(row=0, column=0)

        self.out_scroll.config(command=self.out_text.yview)

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

    def create_input_planet(self):
        self.planet_f = tk.LabelFrame(self.in_f, text="Planet", padx=5, pady=5)
        self.planet_f.grid(row=0, column=0, columnspan=2)

        tk.Label(self.planet_f, text="Planet Type:").grid(row=0, column=0)
        self.in_p_type = tk.OptionMenu(self.planet_f, self.p_type,
                                       "Custom", "Earthlike", "Gas Giant")
        self.in_p_type.grid(row=0, column=1)

        lbl_p_temp = tk.Label(self.planet_f, text="Temperature (Kelvin):")
        lbl_p_temp.grid(row=1, column=0)
        self.in_p_temp = tk.Entry(self.planet_f, textvariable=self.p_temp)
        self.in_p_temp.grid(row=1, column=1)

        lbl_p_hydro = tk.Label(self.planet_f,
                               text="Hydrographic Coverage (%): ")
        lbl_p_hydro.grid(row=2, column=0)
        self.in_p_hydro = tk.Entry(self.planet_f, textvariable=self.p_hydro)
        self.in_p_hydro.grid(row=2, column=1)

        lbl_p_grav = tk.Label(self.planet_f, text="Gravity (G): ")
        lbl_p_grav.grid(row=3, column=0)
        self.in_p_grav = tk.Entry(self.planet_f, textvariable=self.p_grav)
        self.in_p_grav.grid(row=3, column=1)

        self.in_p_random = tk.Button(self.planet_f, text="Randomize",
                                     command=self.p_randomize)
        self.in_p_random.grid(row=4, column=1)

    def trace_p_type(self, *args):
        # print("trace_p_type Callback: ", args)
        value = self.p_type.get()
        if value == "Earthlike":
            self.in_p_temp.config(state=tk.NORMAL)
            self.in_p_hydro.config(state=tk.NORMAL)
            self.in_p_grav.config(state=tk.NORMAL)
            self.p_temp.set(295)
            self.p_hydro.set(70)
            self.p_grav.set(1.0)
            self.in_p_temp.config(state=tk.DISABLED)
            self.in_p_hydro.config(state=tk.DISABLED)
            self.in_p_grav.config(state=tk.DISABLED)
            self.in_p_random.config(state=tk.DISABLED)
        elif value == "Gas Giant":
            self.hab_type.set("Gas Giant")
            self.in_habtype.config(state=tk.DISABLED)
            self.chem_bas.set("Hydrogen-Based")
            self.in_chem_bas.config(state=tk.DISABLED)
        if value != "Earthlike":
            self.in_p_temp.config(state=tk.NORMAL)
            self.in_p_hydro.config(state=tk.NORMAL)
            self.in_p_grav.config(state=tk.NORMAL)
            self.in_p_random.config(state=tk.NORMAL)
        if value != "Gas Giant":
            self.in_habtype.config(state=tk.NORMAL)
            if self.hab_type.get() == "Gas Giant":
                self.hab_type.set("")
            self.in_chem_bas.config(state=tk.NORMAL)
            self.chem_bas.set("")

    def p_randomize(self):
        self.p_temp.set(random.randint(260, 350))
        self.p_hydro.set(random.randint(0, 100))
        self.p_grav.set(round(random.uniform(0, 6), 3))

    def trace_hab_type(self, *args):
        value = self.hab_type.get()
        menu = self.in_habitat["menu"]
        menu.delete(0, "end")
        if value in ["Water", "Gas Giant"]:
            table = [""] + tables.ui_hab_water
        elif value == "Land":
            table = [""] + tables.ui_hab_land
        else:
            table = [""] + tables.ui_habitat
        for hab in table:
            menu.add_command(label=hab,
                             command=tk._setit(self.habitat, hab))
        if self.habitat.get() not in table:
            self.habitat.set("")

    def trace_habitat(self, *args):
        value = self.habitat.get()
        if self.hab_type.get() != "Gas Giant":
            if value in tables.ui_hab_land:
                self.hab_type.set("Land")
                self.in_habtype.config(state=tk.DISABLED)
            elif value in tables.ui_hab_water:
                self.hab_type.set("Water")
                self.in_habtype.config(state=tk.DISABLED)
            else:
                self.in_habtype.config(state=tk.NORMAL)

    def species_gen(self):
        in_planet = self.gen_planet()
        in_species = self.load_species(in_planet)
        text_planet = in_planet.planet_output()

        lead_z = len(str(self.in_num.get() - 1))

        self.out_text.config(state=tk.NORMAL)
        self.out_text.delete(1.0, tk.END)
        self.out_text.insert(tk.END, "=" * 40)
        self.out_text.insert(tk.END, "\nPlanet Info:\n")
        self.out_text.insert(tk.END, "=" * 40)
        self.out_text.insert(tk.END, "\n")
        self.out_text.insert(tk.END, text_planet)
        self.out_text.insert(tk.END, "\n")
        self.out_text.insert(tk.END, "=" * 40)
        self.out_text.insert(tk.END, "\n")
        for k in range(self.in_num.get()):
            out_species = copy.deepcopy(in_species)
            out_species.generate()
            self.out_text.insert(tk.END,
                                 "Species {}:\n".format(str(k).zfill(lead_z)))
            text_species = out_species.output_text_basic()
            self.out_text.insert(tk.END, text_species)
            self.out_text.insert(tk.END, "\n")
            self.out_text.insert(tk.END, "=" * 40)
            self.out_text.insert(tk.END, "\n")

        self.out_text.config(state=tk.DISABLED)

    def gen_planet(self):
        in_planet = planet.PlanetInfo()
        in_planet.type = self.p_type.get()
        in_planet.temp = int(self.p_temp.get())
        in_planet.hydro = int(self.p_hydro.get())
        in_planet.gravity = float(self.p_grav.get())
        in_planet.generate()

        return in_planet

    def load_species(self, in_planet):
        in_species = species.Species(in_planet)
        sapience = self.sapience.get()
        if sapience == "Possible":
            in_species.sapient = False
            in_species.possible_sapient = True
        elif sapience == "Sapient":
            in_species.sapient = True
            in_species.possible_sapient = True
        elif sapience == "Nonsapient":
            in_species.sapient = False
            in_species.possible_sapient = False
        in_species.p_variation = self.p_variation.get()
        if self.chem_bas.get():
            in_species.chemical_basis = self.chem_bas.get()
        else:
            in_species.chemical_basis = None
        if self.hab_type.get():
            in_species.habitat_type = self.hab_type.get()
        else:
            in_species.habitat_type = None
        if self.habitat.get():
            in_species.habitat = self.habitat.get()
        if self.troph.get():
            in_species.trophic_level = self.troph.get()

        return in_species


def run_gui():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    run_gui()
