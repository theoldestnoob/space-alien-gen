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
        self.p_type = tk.StringVar(value="Custom")
        self.p_type.trace_add("write", self.trace_p_type)
        self.p_temp = tk.IntVar(value=295)
        self.p_hydro = tk.IntVar(value=70)
        self.p_grav = tk.DoubleVar(value=1.0)
        self.sapience = tk.StringVar(value="Possible")
        self.p_variation = tk.StringVar(value="Bio")
        self.chem_bas = tk.StringVar(value="")
        self.hab_type = tk.StringVar(value="")
        self.hab_type.trace_add("write", self.trace_hab_type)
        self.habitat = tk.StringVar(value="")
        self.habitat.trace_add("write", self.trace_habitat)
        self.troph = tk.StringVar(value="")
        self.loco_a = tk.StringVar(value="")
        self.size_class = tk.StringVar(value="")
        # TODO: fix this so volume and mass can be empty
        self.size_vol = tk.DoubleVar(value=0.0)
        self.size_mass = tk.DoubleVar(value=0.0)
        self.symm = tk.StringVar(value="")
        self.sides = tk.StringVar(value="")
        self.tail = tk.StringVar(value="")
        self.skel = tk.StringVar(value="")
        self.skin_t = tk.StringVar(value="")
        self.skin = tk.StringVar(value="")
        self.breath = tk.StringVar(value="")
        self.temp = tk.StringVar(value="")
        self.grow = tk.StringVar(value="")
        self.sex = tk.StringVar(value="")
        self.gest = tk.StringVar(value="")
        self.gest_s = tk.StringVar(value="")
        self.repro = tk.StringVar(value="")
        self.sense_prim = tk.StringVar(value="")
        self.sense_v = tk.StringVar(value="")
        self.sense_h = tk.StringVar(value="")
        self.sense_to = tk.StringVar(value="")
        self.sense_ta = tk.StringVar(value="")
        self.sense_sp = tk.StringVar(value="")
        self.int = tk.StringVar(value="")
        self.mate = tk.StringVar(value="")
        self.social = tk.StringVar(value="")
        self.cha = tk.IntVar(value=0)
        self.con = tk.IntVar(value=0)
        self.ego = tk.IntVar(value=0)
        self.gre = tk.IntVar(value=0)
        self.ima = tk.IntVar(value=0)
        self.pla = tk.IntVar(value=0)

    def create_widgets(self):
        self.create_input()
        self.create_output()
        self.create_controls()

    def create_input(self):
        self.in_f = tk.Frame(self, bd=3)
        self.in_f.grid(row=0, column=0)

        self.create_input_planet()

        sap_f = tk.LabelFrame(self.in_f, text="Sapience")
        sap_f.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)
        tk.Radiobutton(sap_f, text="Possible", variable=self.sapience,
                       value="Possible").grid(row=0, column=0)
        tk.Radiobutton(sap_f, text="Sapient", variable=self.sapience,
                       value="Sapient").grid(row=0, column=1)
        tk.Radiobutton(sap_f, text="Nonsapient", variable=self.sapience,
                       value="Nonsapient").grid(row=0, column=2)

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

        lbl_loco_a = tk.Label(self.in_f, text="Primary Locomotion:")
        lbl_loco_a.grid(row=6, column=0)
        tbl_loco_a = [""] + tables.ui_locomotion
        self.in_loco_a = tk.OptionMenu(self.in_f, self.loco_a, *tbl_loco_a)
        self.in_loco_a.grid(row=6, column=1)

        lbl_size_c = tk.Label(self.in_f, text="Size Class:")
        lbl_size_c.grid(row=7, column=0)

        lbl_size_vol = tk.Label(self.in_f, text="Volume:")
        lbl_size_vol.grid(row=8, column=0)

        lbl_size_mass = tk.Label(self.in_f, text="Mass:")
        lbl_size_mass.grid(row=9, column=0)

        lbl_symm = tk.Label(self.in_f, text="Symmetry:")
        lbl_symm.grid(row=10, column=0)

        lbl_sides = tk.Label(self.in_f, text="Sides:")
        lbl_sides.grid(row=11, column=0)

        lbl_tail = tk.Label(self.in_f, text="Tail Feature:")
        lbl_tail.grid(row=12, column=0)

        lbl_skel = tk.Label(self.in_f, text="Skeleton:")
        lbl_skel.grid(row=13, column=0)

        lbl_skin_t = tk.Label(self.in_f, text="Skin Type:")
        lbl_skin_t.grid(row=14, column=0)

        lbl_skin = tk.Label(self.in_f, text="Skin:")
        lbl_skin.grid(row=15, column=0)

        lbl_breath = tk.Label(self.in_f, text="Breathing:")
        lbl_breath.grid(row=16, column=0)

        lbl_temp = tk.Label(self.in_f, text="Temperature Regulation:")
        lbl_temp.grid(row=17, column=0)

        lbl_grow = tk.Label(self.in_f, text="Growth Pattern:")
        lbl_grow.grid(row=18, column=0)

        lbl_sex = tk.Label(self.in_f, text="Sexes:")
        lbl_sex.grid(row=19, column=0)

        lbl_gest = tk.Label(self.in_f, text="Gestation:")
        lbl_gest.grid(row=20, column=0)

        lbl_gest_s = tk.Label(self.in_f, text="Special Gestation:")
        lbl_gest_s.grid(row=21, column=0)

        lbl_repro = tk.Label(self.in_f, text="Reproductive Strategy:")
        lbl_repro.grid(row=22, column=0)

        lbl_sen_p = tk.Label(self.in_f, text="Primary Sense:")
        lbl_sen_p.grid(row=23, column=0)

        lbl_sen_v = tk.Label(self.in_f, text="Vision:")
        lbl_sen_v.grid(row=24, column=0)

        lbl_sen_h = tk.Label(self.in_f, text="Hearing:")
        lbl_sen_h.grid(row=25, column=0)

        lbl_sen_to = tk.Label(self.in_f, text="Touch:")
        lbl_sen_to.grid(row=26, column=0)

        lbl_sen_ta = tk.Label(self.in_f, text="Taste/Smell:")
        lbl_sen_ta.grid(row=27, column=0)

        lbl_sen_s = tk.Label(self.in_f, text="Special Senses:")
        lbl_sen_s.grid(row=28, column=0)

        lbl_int = tk.Label(self.in_f, text="Intelligence:")
        lbl_int.grid(row=29, column=0)

        lbl_mat = tk.Label(self.in_f, text="Mating Behavior:")
        lbl_mat.grid(row=30, column=0)

        lbl_soc = tk.Label(self.in_f, text="Socal Organization:")
        lbl_soc.grid(row=31, column=0)

        self.create_input_personality()

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

    def create_input_personality(self):
        pers_f = tk.LabelFrame(self.in_f, text="Personality",
                               padx=5, pady=5)
        pers_f.grid(row=32, column=0, columnspan=2, sticky=tk.NSEW)

        tk.Radiobutton(pers_f, text="Biology-Based", variable=self.p_variation,
                       value="Bio").grid(row=0, column=0)
        tk.Radiobutton(pers_f, text="More Varied", variable=self.p_variation,
                       value="Vary").grid(row=0, column=1)
        tk.Radiobutton(pers_f, text="Custom", variable=self.p_variation,
                       value="Custom").grid(row=0, column=2)

        lbl_cha = tk.Label(pers_f, text="Chauvinism:")
        lbl_cha.grid(row=1, column=0)

        lbl_con = tk.Label(pers_f, text="Concentration:")
        lbl_con.grid(row=2, column=0)

        lbl_ego = tk.Label(pers_f, text="Egoism:")
        lbl_ego.grid(row=3, column=0)

        lbl_gre = tk.Label(pers_f, text="Gregariousness:")
        lbl_gre.grid(row=1, column=2)

        lbl_ima = tk.Label(pers_f, text="Imagination:")
        lbl_ima.grid(row=2, column=2)

        lbl_pla = tk.Label(pers_f, text="Playfulness:")
        lbl_pla.grid(row=3, column=2)

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
        p_vary = self.p_variation.get()
        if p_vary == "Bio":
            in_species.p_variation = False
        elif p_vary == "Vary":
            in_species.p_variation = True
        elif p_vary == "Custom":
            # load in custom personality values here
            in_species.p_variation = True
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
        if self.loco_a.get():
            in_species.locomotion = [self.loco_a.get()]

        return in_species


def run_gui():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    run_gui()
