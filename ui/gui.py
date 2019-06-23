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
        self.pack()
        self.create_variables()
        self.create_widgets()
        self.master.geometry("1028x540")
        self.winfo_toplevel().title("space-alien-gen")

    def create_variables(self):
        self.p_type = tk.StringVar(value="Custom")
        self.p_type.trace_add("write", self.trace_p_type)
        self.p_temp = tk.StringVar(value="295")
        self.p_hydro = tk.StringVar(value="70")
        self.p_grav = tk.StringVar(value="1.0")
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
        self.size_vol = tk.StringVar(value="")
        self.size_vol.trace_add("write", self.trace_size_vol)
        self.size_mass = tk.StringVar(value="")
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
        self.create_input_frame()
        self.create_output_frame()

    def create_input_frame(self):
        # set up canvas for scrolling region
        self.canvas_in = tk.Canvas(self)
        vbar_in = tk.Scrollbar(self)
        vbar_in.config(command=self.canvas_in.yview)
        self.canvas_in.config(yscrollcommand=vbar_in.set)
        self.canvas_in.pack(side=tk.LEFT, fill=tk.Y)
        vbar_in.pack(side=tk.LEFT, fill=tk.Y)

        # set up frame for input
        self.f_in = tk.LabelFrame(self.canvas_in, text="Input", bd=3,
                                  padx=3, pady=3)

        planet_f = self.create_in_planet_f(self.f_in)
        planet_f.grid(row=0, column=0, columnspan=2)

        bas_f = self.create_in_basic_f(self.f_in)
        bas_f.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        size_f = self.create_in_size_f(self.f_in)
        size_f.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)

        body_f = self.create_in_bodyplan_f(self.f_in)
        body_f.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)

        meta_f = self.create_in_metabolism_f(self.f_in)
        meta_f.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)

        repro_f = self.create_in_reproduction_f(self.f_in)
        repro_f.grid(row=5, column=0, columnspan=2, sticky=tk.NSEW)

        sense_f = self.create_in_senses_f(self.f_in)
        sense_f.grid(row=6, column=0, columnspan=2, sticky=tk.NSEW)

        int_f = self.create_in_intel_f(self.f_in)
        int_f.grid(row=7, column=0, columnspan=2, sticky=tk.NSEW)

        soc_f = self.create_in_social_f(self.f_in)
        soc_f.grid(row=8, column=0, columnspan=2, sticky=tk.NSEW)

        pers_f = self.create_in_personality_f(self.f_in)
        pers_f.grid(row=9, column=0, columnspan=2, sticky=tk.NSEW)

        # create input window and resize canvas to allow for scrolling
        self.canvas_in.create_window(0, 0, anchor=tk.NW, window=self.f_in)
        self.canvas_in.update()
        x, y, w, h = self.canvas_in.bbox(tk.ALL)
        self.canvas_in.config(scrollregion=(x, y, w, h))
        self.canvas_in.config(width=w, height=h)

    def create_output_frame(self):
        # set up canvas for scrolling region
        self.canvas_out = tk.Canvas(self)
        vbar_out = tk.Scrollbar(self)
        vbar_out.config(command=self.canvas_out.yview)
        self.canvas_out.config(yscrollcommand=vbar_out.set)
        self.canvas_out.pack(side=tk.LEFT, fill=tk.Y)
        vbar_out.pack(side=tk.LEFT, fill=tk.Y)

        # create output frame
        self.f_out = tk.LabelFrame(self, text="Output", bd=3)
        self.f_out.pack(side=tk.LEFT, fill=tk.Y)

        self.f_txt = tk.Frame(self.f_out, bd=3, relief=tk.SUNKEN)
        self.f_txt.grid(row=0, column=0)

        self.out_scroll = tk.Scrollbar(self.f_txt)
        self.out_scroll.grid(row=0, column=1, sticky=tk.NS)

        self.out_txt = tk.Text(self.f_txt, yscrollcommand=self.out_scroll.set)
        self.out_txt.config(height=24)
        self.out_txt.grid(row=0, column=0)

        self.out_scroll.config(command=self.out_txt.yview)

        self.f_ctrl = tk.Frame(self.f_out, bd=3)
        self.f_ctrl.grid(row=1, column=0)

        tk.Label(self.f_ctrl,
                 text="Number of Species to Generate:").grid(row=1, column=0)
        self.in_num = tk.Scale(self.f_ctrl, from_=1)
        self.in_num.grid(row=1, column=1)

        self.gen_button = tk.Button(self.f_ctrl, text="Generate!",
                                    command=self.species_gen)
        self.gen_button.grid(row=1, column=2)

        # create output window and resize canvas to allow for scrolling
        self.canvas_out.create_window(0, 0, anchor=tk.NW, window=self.f_out)
        self.canvas_out.update()
        x, y, w, h = self.canvas_out.bbox(tk.ALL)
        self.canvas_out.config(scrollregion=(x, y, w, h))
        self.canvas_out.config(width=w, height=h)

    def create_in_planet_f(self, parent):
        planet_f = tk.LabelFrame(parent, text="Planet", padx=5, pady=5)

        tk.Label(planet_f, text="Planet Type:").grid(row=0, column=0)
        self.in_p_type = tk.OptionMenu(planet_f, self.p_type,
                                       "Custom", "Earthlike", "Gas Giant")
        self.in_p_type.grid(row=0, column=1)

        lbl_p_temp = tk.Label(planet_f, text="Temperature (Kelvin):")
        lbl_p_temp.grid(row=1, column=0)
        self.in_p_temp = tk.Entry(planet_f, textvariable=self.p_temp)
        self.in_p_temp.grid(row=1, column=1)

        lbl_p_hydro = tk.Label(planet_f, text="Hydrographic Coverage (%): ")
        lbl_p_hydro.grid(row=2, column=0)
        self.in_p_hydro = tk.Entry(planet_f, textvariable=self.p_hydro)
        self.in_p_hydro.grid(row=2, column=1)

        lbl_p_grav = tk.Label(planet_f, text="Gravity (G): ")
        lbl_p_grav.grid(row=3, column=0)
        self.in_p_grav = tk.Entry(planet_f, textvariable=self.p_grav)
        self.in_p_grav.grid(row=3, column=1)

        self.in_p_random = tk.Button(planet_f, text="Randomize",
                                     command=self.p_randomize)
        self.in_p_random.grid(row=4, column=1)

        return planet_f

    def create_in_basic_f(self, parent):
        bas_f = tk.LabelFrame(parent, text="Basic", padx=5, pady=5)
        bas_f.grid_columnconfigure(1, weight=1)

        lbl_chem = tk.Label(bas_f, text="Chemical Basis:")
        lbl_chem.grid(row=0, column=0, sticky=tk.W)
        tbl_chem = [""] + tables.ui_chemical_basis
        self.in_chem_bas = tk.OptionMenu(bas_f, self.chem_bas, *tbl_chem)
        self.in_chem_bas.grid(row=0, column=1)

        hab_f = self.create_in_habitat_f(bas_f)
        hab_f.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        lbl_troph = tk.Label(bas_f, text="Trophic Level:")
        lbl_troph.grid(row=2, column=0, sticky=tk.W)
        tbl_troph = [""] + tables.ui_trophic_level
        self.in_troph = tk.OptionMenu(bas_f, self.troph, *tbl_troph)
        self.in_troph.grid(row=2, column=1)

        return bas_f

    def create_in_habitat_f(self, parent):
        hab_f = tk.Frame(parent)
        # hab_f.grid_columnconfigure(0, weight=1)
        hab_f.grid_columnconfigure(1, weight=1)
        hab_f.grid_columnconfigure(2, weight=1)

        lbl_habtype = tk.Label(hab_f, text="Habitat:")
        lbl_habtype.grid(row=0, column=0, sticky=tk.W)
        tbl_habtype = [""] + tables.ui_hab_type
        tbl_habtype.remove("Gas Giant")
        self.in_habtype = tk.OptionMenu(hab_f, self.hab_type, *tbl_habtype)
        self.in_habtype.grid(row=0, column=1)

        tbl_habitat = [""] + tables.ui_habitat
        self.in_habitat = tk.OptionMenu(hab_f, self.habitat, *tbl_habitat)
        self.in_habitat.grid(row=0, column=2)

        return hab_f

    def create_in_habitat_f_old(self, parent):
        hab_f = tk.LabelFrame(parent, text="Habitat")
        hab_f.grid_columnconfigure(0, weight=1)
        hab_f.grid_columnconfigure(1, weight=1)

        lbl_habtype = tk.Label(hab_f, text="Type:")
        lbl_habtype.grid(row=0, column=0)
        tbl_habtype = [""] + tables.ui_hab_type
        tbl_habtype.remove("Gas Giant")
        self.in_habtype = tk.OptionMenu(hab_f, self.hab_type, *tbl_habtype)
        self.in_habtype.grid(row=1, column=0)

        lbl_habitat = tk.Label(hab_f, text="Habitat:")
        lbl_habitat.grid(row=0, column=1)
        tbl_habitat = [""] + tables.ui_habitat
        self.in_habitat = tk.OptionMenu(hab_f, self.habitat, *tbl_habitat)
        self.in_habitat.grid(row=1, column=1)

        return hab_f

    def create_in_size_f(self, parent):
        size_f = tk.LabelFrame(parent, text="Size", padx=5, pady=5)
        size_f.columnconfigure(0, weight=1)
        size_f.columnconfigure(1, weight=1)

        lbl_size_c = tk.Label(size_f, text="Size Class:")
        lbl_size_c.grid(row=0, column=0)

        tbl_sizec = [""] + tables.ui_size_class
        self.in_size_c = tk.OptionMenu(size_f, self.size_class, *tbl_sizec)
        self.in_size_c.grid(row=0, column=1)
        '''
        tk.Radiobutton(size_f, text="Any", variable=self.size_class,
                       value="").grid(row=0, column=1)
        tk.Radiobutton(size_f, text="Small", variable=self.size_class,
                       value="Small").grid(row=0, column=2)
        tk.Radiobutton(size_f, text="Human-Scale", variable=self.size_class,
                       value="Human-Scale").grid(row=0, column=3)
        tk.Radiobutton(size_f, text="Large", variable=self.size_class,
                       value="Large").grid(row=1, column=2)
        tk.Radiobutton(size_f, text="Huge", variable=self.size_class,
                       value="Huge").grid(row=1, column=3, sticky=tk.W)
        '''
        lbl_size_vol = tk.Label(size_f, text="Volume (yards):")
        lbl_size_vol.grid(row=2, column=0)
        self.in_size_v = tk.Entry(size_f, textvariable=self.size_vol)
        self.in_size_v.grid(row=2, column=1)
        lbl_size_mass = tk.Label(size_f, text="Mass (pounds):")
        lbl_size_mass.grid(row=3, column=0)
        self.in_size_m = tk.Entry(size_f, textvariable=self.size_mass)
        self.in_size_m.grid(row=3, column=1)

        return size_f

    def create_in_bodyplan_f(self, parent):
        body_f = tk.LabelFrame(parent, text="Body Plan", padx=5, pady=5)

        lbl_loco_a = tk.Label(body_f, text="Primary Locomotion:")
        lbl_loco_a.grid(row=0, column=0)
        tbl_loco_a = [""] + tables.ui_locomotion
        self.in_loco_a = tk.OptionMenu(body_f, self.loco_a, *tbl_loco_a)
        self.in_loco_a.grid(row=0, column=1)

        lbl_symm = tk.Label(body_f, text="Symmetry:")
        lbl_symm.grid(row=1, column=0)

        lbl_sides = tk.Label(body_f, text="Sides:")
        lbl_sides.grid(row=2, column=0)

        lbl_tail = tk.Label(body_f, text="Tail Feature:")
        lbl_tail.grid(row=3, column=0)

        lbl_skel = tk.Label(body_f, text="Skeleton:")
        lbl_skel.grid(row=4, column=0)

        lbl_skin_t = tk.Label(body_f, text="Skin Type:")
        lbl_skin_t.grid(row=5, column=0)

        lbl_skin = tk.Label(body_f, text="Skin:")
        lbl_skin.grid(row=6, column=0)

        return body_f

    def create_in_metabolism_f(self, parent):
        meta_f = tk.LabelFrame(parent, text="Metabolism", padx=5, pady=5)

        lbl_breath = tk.Label(meta_f, text="Breathing:")
        lbl_breath.grid(row=0, column=0)

        lbl_temp = tk.Label(meta_f, text="Temperature Regulation:")
        lbl_temp.grid(row=1, column=0)

        lbl_grow = tk.Label(meta_f, text="Growth Pattern:")
        lbl_grow.grid(row=2, column=0)

        return meta_f

    def create_in_reproduction_f(self, parent):
        repro_f = tk.LabelFrame(parent, text="Reproduction", padx=5, pady=5)

        lbl_sex = tk.Label(repro_f, text="Sexes:")
        lbl_sex.grid(row=0, column=0)

        lbl_gest = tk.Label(repro_f, text="Gestation:")
        lbl_gest.grid(row=1, column=0)

        lbl_gest_s = tk.Label(repro_f, text="Special Gestation:")
        lbl_gest_s.grid(row=2, column=0)

        lbl_repro = tk.Label(repro_f, text="Reproductive Strategy:")
        lbl_repro.grid(row=3, column=0)

        return repro_f

    def create_in_senses_f(self, parent):
        sense_f = tk.LabelFrame(parent, text="Senses", padx=5, pady=5)

        lbl_sen_p = tk.Label(sense_f, text="Primary Sense:")
        lbl_sen_p.grid(row=0, column=0)

        lbl_sen_v = tk.Label(sense_f, text="Vision:")
        lbl_sen_v.grid(row=1, column=0)

        lbl_sen_h = tk.Label(sense_f, text="Hearing:")
        lbl_sen_h.grid(row=2, column=0)

        lbl_sen_to = tk.Label(sense_f, text="Touch:")
        lbl_sen_to.grid(row=3, column=0)

        lbl_sen_ta = tk.Label(sense_f, text="Taste/Smell:")
        lbl_sen_ta.grid(row=4, column=0)

        lbl_sen_s = tk.Label(sense_f, text="Special Senses:")
        lbl_sen_s.grid(row=5, column=0)

        return sense_f

    def create_in_intel_f(self, parent):
        int_f = tk.LabelFrame(parent, text="Intelligence", padx=5, pady=5)

        lbl_sap = tk.Label(int_f, text="Sapience:")
        lbl_sap.grid(row=0, column=0)

        tk.Radiobutton(int_f, text="Possible", variable=self.sapience,
                       value="Possible").grid(row=0, column=1)
        tk.Radiobutton(int_f, text="Sapient", variable=self.sapience,
                       value="Sapient").grid(row=0, column=2)
        tk.Radiobutton(int_f, text="Nonsapient", variable=self.sapience,
                       value="Nonsapient").grid(row=0, column=3)

        lbl_int = tk.Label(int_f, text="Intelligence:")
        lbl_int.grid(row=1, column=0, columnspan=2)

        return int_f

    def create_in_sapience_f(self, parent):
        sap_f = tk.LabelFrame(parent, text="Sapience")

        tk.Radiobutton(sap_f, text="Possible", variable=self.sapience,
                       value="Possible").grid(row=0, column=0)
        tk.Radiobutton(sap_f, text="Sapient", variable=self.sapience,
                       value="Sapient").grid(row=0, column=1)
        tk.Radiobutton(sap_f, text="Nonsapient", variable=self.sapience,
                       value="Nonsapient").grid(row=0, column=2)

        return sap_f

    def create_in_social_f(self, parent):
        soc_f = tk.LabelFrame(parent, text="Social", padx=5, pady=5)

        lbl_mat = tk.Label(soc_f, text="Mating Behavior:")
        lbl_mat.grid(row=0, column=0)

        lbl_soc = tk.Label(soc_f, text="Socal Organization:")
        lbl_soc.grid(row=1, column=0)

        return soc_f

    def create_in_personality_f(self, parent):
        pers_f = tk.LabelFrame(parent, text="Personality",
                               padx=5, pady=5)

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

        return pers_f

    def p_randomize(self):
        self.p_temp.set(random.randint(260, 350))
        self.p_hydro.set(random.randint(0, 100))
        self.p_grav.set(round(random.uniform(0, 6), 3))

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

    def trace_size_vol(self, *args):
        if not self.size_vol.get():
            self.in_size_c.config(state=tk.NORMAL)
        else:
            value = float(self.size_vol.get())
            if 0.0 < value <= 0.4:
                self.size_class.set("Small")
                self.in_size_c.config(state=tk.DISABLED)
            elif value <= 4:
                self.size_class.set("Human-Scale")
                self.in_size_c.config(state=tk.DISABLED)
            elif value <= 20:
                self.size_class.set("Large")
                self.in_size_c.config(state=tk.DISABLED)
            else:
                self.size_class.set("Huge")
                self.in_size_c.config(state=tk.DISABLED)

    def species_gen(self):
        if self.check_input():
            in_planet = self.gen_planet()
            in_species = self.load_species(in_planet)
            text_planet = in_planet.planet_output()

            self.out_txt.config(state=tk.NORMAL)
            self.out_txt.delete(1.0, tk.END)
            self.out_txt.insert(tk.END, "=" * 40)
            self.out_txt.insert(tk.END, "\nPlanet Info:\n")
            self.out_txt.insert(tk.END, "=" * 40)
            self.out_txt.insert(tk.END, "\n")
            self.out_txt.insert(tk.END, text_planet)
            self.out_txt.insert(tk.END, "\n")
            self.out_txt.insert(tk.END, "=" * 40)
            self.out_txt.insert(tk.END, "\n")
            for k in range(self.in_num.get()):
                out_species = copy.deepcopy(in_species)
                out_species.generate()
                self.out_txt.insert(tk.END,
                                    "Species {}:\n".format(str(k)))
                text_species = out_species.output_text_basic()
                self.out_txt.insert(tk.END, text_species)
                self.out_txt.insert(tk.END, "\n")
                self.out_txt.insert(tk.END, "=" * 40)
                self.out_txt.insert(tk.END, "\n")
            self.out_txt.config(state=tk.DISABLED)

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
        if self.size_class.get():
            in_species.size_class = self.size_class.get()
        if self.size_vol.get():
            in_species.size_volume = float(self.size_vol.get())
        if self.size_mass.get():
            in_species.size_mass = float(self.size_mass.get())

        return in_species

    def check_input(self):
        errstr = ""
        if not self.p_temp.get().isdigit():
            errstr = "Error! Planet Temperature must be Integer!\n"
            errstr += "You entered: {}".format(self.p_temp.get())
        elif not self.p_hydro.get().isdigit():
            errstr = "Error! Planet Hydrographic Coverage must be Integer!\n"
            errstr += "You entered: {}".format(self.p_hydro.get())
        elif not self.p_grav.get().replace(".", "", 1).isdigit():
            errstr = "Error! Planet Gravity must be Number!\n"
            errstr += "You entered: {}".format(self.p_grav.get())
        elif (self.size_vol.get()
                and not self.size_vol.get().replace(".", "", 1).isdigit()):
            errstr = "Error! Volume must be Number!\n"
            errstr += "You entered: {}".format(self.size_vol.get())
        elif (self.size_mass.get()
                and not self.size_mass.get().replace(".", "", 1).isdigit()):
            errstr = "Error! Mass must be Number!\n"
            errstr += "You entered: {}".format(self.size_mass.get())
        if errstr:
            self.out_txt.config(state=tk.NORMAL)
            self.out_txt.delete(1.0, tk.END)
            self.out_txt.insert(tk.END, errstr)
            self.out_txt.config(state=tk.DISABLED)
            return False
        return True


def run_gui():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    run_gui()
