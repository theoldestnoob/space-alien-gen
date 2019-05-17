'''
Created on Dec 14, 2018

@author: willh
'''

import random
import aliengen.tables as tables
import aliengen.dice as dice


class Species():
    '''
    classdocs
    '''

    def __init__(self, world):
        '''
        Constructor
        '''
        self.planet = world
        self.sapient = False
        self.possible_sapient = True
        self.chemical_basis = ""
        self.habitat_type = ""
        self.habitat = ""
        self.trophic_type = ""
        self.trophic_subtype = ""
        self.trophic_level = []
        self._is_herbivore = False
        self._is_carnivore = False
        self._is_autotroph = False
        self.locomotion = []
        self._is_flying = False
        self.size_class = ""
        self.size_volume = 0
        self.size_mass = 0
        self.size_weight = 0
        self.stat_st = 0
        self.stat_move_walk = 0
        self.body_symmetry = ""
        self.body_sides = 0
        self.body_segments = 0
        self.body_limbs = 0
        self.body_tail = ""
        self.body_manip = ""
        self.body_skel = ""
        self.skin_type = ""
        self.skin_detail = ""
        self.breathing = ""
        self.temperature_regulation = ""
        self.growth_pattern = ""
        self.sexes = ""
        self.gestation = ""
        self.gestation_special = ""
        self.reproductive_strat = ""
        self.sense_primary = ""
        self.sense_vision = ""
        self.sense_hearing = ""
        self.sense_touch = ""
        self.sense_tastesmell = ""
        self.sense_specials = []
        self.comms_a = ""
        self.comms_b = ""
        self.intelligence = ""
        self.stat_iq = 0
        self.mating = ""
        self.social_organization = ""
        self.p_more_variation = True
        self.p_chauvinism = 0
        self.p_concentration = 0
        self.p_curiosity = 0
        self.p_egoism = 0
        self.p_empathy = 0
        self.p_gregariousness = 0
        self.p_imagination = 0
        self.p_suspicion = 0
        self.p_playfulness = 0
        self.p_chauvinism_trait = ""
        self.p_concentration_trait = ""
        self.p_curiosity_trait = ""
        self.p_egoism_trait = ""
        self.p_empathy_trait = ""
        self.p_gregariousness_trait = ""
        self.p_imagination_trait = ""
        self.p_suspicion_trait = ""
        self.p_playfulness_trait = ""

    def change_planet(self, world):
        '''
        Set a new species planet.
        '''
        self.planet = world

    def clear_attributes(self):
        '''
        Set all species attributes except planet to blank or default values.
        '''
        self.sapient = False
        self.possible_sapient = True
        self.chemical_basis = ""
        self.habitat_type = ""
        self.habitat = ""
        self.trophic_type = ""
        self.trophic_subtype = ""
        self.trophic_level = []
        self._is_herbivore = False
        self._is_carnivore = False
        self._is_autotroph = False
        self.locomotion = []
        self._is_flying = False
        self.size_class = ""
        self.size_volume = 0
        self.size_mass = 0
        self.size_weight = 0
        self.stat_st = 0
        self.stat_move_walk = 0
        self.body_symmetry = ""
        self.body_sides = 0
        self.body_segments = 0
        self.body_limbs = 0
        self.body_tail = ""
        self.body_manip = ""
        self.body_skel = ""
        self.skin_type = ""
        self.skin_detail = ""
        self.breathing = ""
        self.temperature_regulation = ""
        self.growth_pattern = ""
        self.sexes = ""
        self.gestation = ""
        self.gestation_special = ""
        self.reproductive_strat = ""
        self.sense_primary = ""
        self.sense_vision = ""
        self.sense_hearing = ""
        self.sense_touch = ""
        self.sense_tastesmell = ""
        self.sense_specials = []
        self.comms_a = ""
        self.comms_b = ""
        self.intelligence = ""
        self.stat_iq = 0
        self.mating = ""
        self.social_organization = ""
        self.p_more_variation = True
        self.p_chauvinism = 0
        self.p_concentration = 0
        self.p_curiosity = 0
        self.p_egoism = 0
        self.p_empathy = 0
        self.p_gregariousness = 0
        self.p_imagination = 0
        self.p_suspicion = 0
        self.p_playfulness = 0
        self.p_chauvinism_trait = ""
        self.p_concentration_trait = ""
        self.p_curiosity_trait = ""
        self.p_egoism_trait = ""
        self.p_empathy_trait = ""
        self.p_gregariousness_trait = ""
        self.p_imagination_trait = ""
        self.p_suspicion_trait = ""
        self.p_playfulness_trait = ""

    def reroll(self):
        '''
        Randomly generate all species attributes,
        regardless of previous user input.
        '''
        self._gen_chemical_basis_planet()
        # self._gen_chemical_basis_table()
        self._gen_habitat_type()
        self._gen_habitat()
        self._gen_trophic_level()
        self._gen_trophic_flags()
        # self._gen_locomotion()
        self._gen_locomotion_primary()
        self._gen_locomotion_secondary()
        self._gen_locomotion_flags()
        self._gen_size_class()
        self._gen_size_volume()
        self._gen_size_mass()
        self._gen_size_weight()
        self._gen_stat_st()
        self._gen_stat_move()
        self._gen_body_symmetry()
        self._gen_body_sides()
        self._gen_body_limbs()
        self._gen_body_tail()
        self._gen_bodyplan()
        self._gen_skin()
        self._gen_breathing()
        self._gen_temperature_regulation()
        self._gen_growth()
        self._gen_sexes()
        self._gen_gestation()
        self._gen_reproductive_strat()
        self._gen_senses()
        self._gen_intelligence()
        self._gen_personality()

    def generate(self):
        '''
        Generate all species attributes that have default / empty values.
        '''
        if self.chemical_basis == "":
            self._gen_chemical_basis_planet()
        if self.habitat_type == "":
            self._gen_habitat_type()
        if self.habitat == "":
            self._gen_habitat()
        self._gen_trophic_level()
        self._gen_trophic_flags()
        self._gen_locomotion_primary()
        self._gen_locomotion_secondary()
        self._gen_locomotion_flags()
        self._gen_size_class()
        self._gen_size_volume()
        self._gen_size_mass()
        self._gen_size_weight()
        self._gen_stat_st()
        self._gen_stat_move()
        self._gen_body_symmetry()
        self._gen_body_sides()
        self._gen_body_limbs()
        self._gen_body_tail()
        self._gen_bodyplan()
        self._gen_skin()
        self._gen_breathing()
        self._gen_temperature_regulation()
        self._gen_growth()
        self._gen_sexes()
        self._gen_gestation()
        self._gen_reproductive_strat()
        self._gen_senses()
        self._gen_intelligence()
        self._gen_personality()

    def output_text_basic(self):
        '''
        Output all species attributes in a structured but crude manner.
        '''
        print("Species Output:")
        print(" Chemical Basis: {}".format(self.chemical_basis))
        print(" Habitat: ", end="")
        print(self.habitat_type, end=" - ")
        print(self.habitat)
        print("  Trophic Levels: {}".format(self.trophic_level))
        print(" Locomotion: {}".format(self.locomotion))
        print(" Size: {}".format(self.size_class))
        print("  Volume: {:.5f} yards".format(self.size_volume))
        print("  Mass: {:.5f} lbs".format(self.size_mass))
        print("  Weight: {:.5f} lbs".format(self.size_weight))
        print("  ST: {:.2f}".format(self.stat_st))
        print("  Move (Walking): {:.2f}".format(self.stat_move_walk))
        print(" Body Plan:")
        print("  Symmetry: {}".format(self.body_symmetry))
        print("  Sides: {}".format(self.body_sides))
        print("  Segments: {}".format(self.body_segments))
        print("  Limbs: {}".format(self.body_limbs))
        print("  Tail: {}".format(self.body_tail))
        print("  Manipulators: {}".format(self.body_manip))
        print("  Skeleton: {}".format(self.body_skel))
        print("  Skin: {}, {}".format(self.skin_type, self.skin_detail))
        print(" Metabolism:")
        print("  Breathing: {}".format(self.breathing))
        print("  Temp. Regulation: {}".format(self.temperature_regulation))
        print("  Growth Pattern: {}".format(self.growth_pattern))
        print(" Reproduction:")
        print("  Sexes: {}".format(self.sexes))
        print("  Gestation: {}, {}".format(self.gestation,
                                           self.gestation_special))
        print("  Reproductive Strategy: {}".format(self.reproductive_strat))
        print(" Senses:")
        print("  Primary: {}".format(self.sense_primary))
        print("  Vision: {}".format(self.sense_vision))
        print("  Hearing: {}".format(self.sense_hearing))
        print("  Touch: {}". format(self.sense_touch))
        print("  Taste/Smell: {}".format(self.sense_tastesmell))
        print("  Special: {}".format(self.sense_specials))
        print("  Primary Communication: {}".format(self.comms_a))
        print("  Secondary Communication: {}".format(self.comms_b))
        print(" Intelligence: {}".format(self.intelligence))
        print("  IQ: {}".format(self.stat_iq))
        print(" Mating Behavior: {}".format(self.mating))
        print(" Social Organization: {}".format(self.social_organization))
        print(" Personality:")
        print("  Chauvinism: {} ({})".format(self.p_chauvinism,
                                             self.p_chauvinism_trait))
        print("  Concentration: {} ({})".format(self.p_concentration,
                                                self.p_concentration_trait))
        print("  Curiosity: {} ({})".format(self.p_curiosity,
                                            self.p_curiosity_trait))
        print("  Egoism: {} ({})".format(self.p_egoism,
                                         self.p_egoism_trait))
        print("  Empathy: {} ({})".format(self.p_empathy,
                                          self.p_empathy_trait))
        print("  Gregariousness: {} ({})".format(self.p_gregariousness,
                                                 self.p_gregariousness_trait))
        print("  Imagination: {} ({})".format(self.p_imagination,
                                              self.p_imagination_trait))
        print("  Suspicion: {} ({})".format(self.p_suspicion,
                                            self.p_suspicion_trait))
        print("  Playfulness: {} ({})".format(self.p_playfulness,
                                              self.p_playfulness_trait))

    # Alien Creation I: GURPS Space pg. 140
    def _gen_chemical_basis_planet(self):

        chembas = ""
        temp = self.planet.get_temp_f()

        if self.planet.type == "Gas Giant":
            chembas = "Hydrogen-Based"
        elif temp < -249:
            chembas = "Hydrogen-Based"
        elif -99 < temp < -29:
            chembas = "Ammonia-Based"
        elif (self.planet.climate == "Cold"
              or self.planet.climate == "Chilly"
              or self.planet.climate == "Cool"):
            roll = random.randint(1, 5)
            if roll == 1:
                chembas = "Hydrocarbon-Based"
            elif roll == 5:
                chembas = "Chlorine-Based"
            else:
                chembas = "Water-Based"
        elif self.planet.climate == "Normal":
            roll = random.randint(1, 4)
            if roll == 4:
                chembas = "Chlorine-Based"
            else:
                chembas = "Water-Based"
        elif (self.planet.climate == "Warm"
              or self.planet.climate == "Tropical"
              or self.planet.climate == "Hot"):
            roll = random.randint(1, 5)
            if roll == 4:
                chembas = "Chlorine-Based"
            elif roll == 5:
                chembas = "Silicon/Sulfuric Acid"
            else:
                chembas = "Water-Based"
        elif self.planet.climate == "Infernal":
            if temp < 251:
                chembas = "Silicon/Sulfuric Acid"
            elif temp < 601:
                roll = random.randint(1, 2)
                if roll == 1:
                    chembas = "Silicon/Sulfuric Acid"
                else:
                    chembas = "Silicon/Liquid Sulfur"
            elif temp < 750:
                chembas = "Silicon/Liquid Sulfur"
            elif temp < 2500:
                chembas = "Silicon/Liquid Rock"
            elif temp > 4000:
                chembas = "Plasma"
        else:
            chembas = "Exotica"

        self.chemical_basis = chembas

    def _gen_chemical_basis_table(self):
        roll = dice.rolldie_zero(3, 6)
        chembas = tables.chemical_basis[roll]
        self.chemical_basis = chembas

    # Alien Creation II: GURPS Space pg. 143
    # TODO: Handle Habitat Types - Space-Dwelling, Planetary Interior
    def _gen_habitat_type(self):

        habtype = ""

        roll = dice.rolldie(1, 6)

        if self.planet.hydro < 11:
            roll -= 2
        elif self.planet.hydro < 51:
            roll -= 1
        elif self.planet.hydro > 79:
            roll += 1
        elif self.planet.hydro > 89:
            roll += 2

        if self.planet.type == "Gas Giant":
            habtype = "Gas Giant"
        elif roll > 3:
            habtype = "Water"
        else:
            habtype = "Land"

        self.habitat_type = habtype

    def _gen_habitat(self):

        habitat = ""

        if self.habitat_type == "Gas Giant":
            habitat = tables.hab_water[dice.rolldie_zero(3, 6)]
        elif self.habitat_type == "Water":
            if self.planet.hydro < 1:
                tab_nowater_land = ["Salt-Water Sea",
                                    "Fresh-Water Lake",
                                    "River/Stream"]
                habitat = tab_nowater_land[dice.rolldie_zero(1, 3)]
            else:
                habitat = tables.hab_water[dice.rolldie_zero(3, 6)]
        elif self.habitat_type == "Land":
            if self.planet.hydro > 99:
                habitat = "Island/Beach"
            else:
                habitat = tables.hab_land[dice.rolldie_zero(3, 6)]

        self.habitat = habitat

    # Alien Creation II: GURPS Space pg. 143
    def _gen_trophic_level(self):

        troph = []

        if self.possible_sapient is False:
            trophtable = tables.troph_ordinary
        else:
            trophtable = tables.troph_sapient

        troph.append(tables.troph_ordinary[dice.rolldie_zero(3, 6)])
        while "Combined" in troph:
            troph.clear()
            troph.append(trophtable[dice.rolldie_zero(3, 6)])
            troph.append(trophtable[dice.rolldie_zero(3, 6)])

        if len(troph) > 1:
            troph = list(set(troph))

        if ("Filter-Feeder" in troph
                and (self.habitat == "Arctic" or self.habitat == "Desert")):
            troph.remove("Filter-Feeder")
            troph.append("Trapping Carnivore")
        if "Autotroph" in troph:
            troph.remove("Autotroph")
            if self.habitat == "Deep-Ocean Vents":
                troph.append(tables.troph_auto[dice.rolldie_zero(1, 3) + 3])
            else:
                troph.append(tables.troph_auto[dice.rolldie_zero(1, 6)])

        self.trophic_level = troph

    def _gen_trophic_flags(self):

        is_herb = False
        is_carn = False
        is_auto = False

        if "Grazing/Browsing Herbivore" in self.trophic_level:
            is_herb = True
        elif "Gathering Herbivore" in self.trophic_level:
            is_herb = True
        elif "Filter-Feeder" in self.trophic_level:
            is_herb = True
        if "Pouncing Carnivore" in self.trophic_level:
            is_carn = True
        elif "Chasing Carnivore" in self.trophic_level:
            is_carn = True
        elif "Trapping Carnivore" in self.trophic_level:
            is_carn = True
        elif "Hijacking Carnivore" in self.trophic_level:
            is_carn = True
        elif "Omnivore" in self.trophic_level:
            is_carn = True
        elif "Scavenger" in self.trophic_level:
            is_carn = True
        if "Photosynthetic Autotroph" in self.trophic_level:
            is_auto = True
        elif "Chemosynthetic Autotroph" in self.trophic_level:
            is_auto = True
        elif "Exotic Autotroph" in self.trophic_level:
            is_auto = True

        self._is_herbivore = is_herb
        self._is_carnivore = is_carn
        self._is_autotroph = is_auto

    # Alien Creation III: GURPS Space pg. 149
    def _gen_locomotion_primary(self):

        loco = []

        roll = dice.rolldie_zero(2, 6)
        if ("Pouncing Carnivore" in self.trophic_level
                or "Chasing Carnivore" in self.trophic_level
                or "Omnivore" in self.trophic_level
                or "Gathering Herbivore" in self.trophic_level
                or "Scavenger" in self.trophic_level):
            roll += 1

        loco.append(tables.loco_primary[self.habitat][roll])

        self.locomotion = loco

    # Alien Creation III: GURPS Space pg. 149
    def _gen_locomotion_secondary(self):

        primary = self.locomotion[0]
        secondary = ""
        tertiary = ""

        if primary in tables.loco_primary_extra[self.habitat]:
            roll = dice.rolldie_zero(2, 6)
            if self.habitat_type == "Land":
                secondary = tables.loco_second_land[primary][roll]
                if (primary == "Winged Flight"
                        and (secondary in ("Climbing", "Swimming"))):
                    roll = dice.rolldie_zero(2, 6)
                    tertiary = tables.loco_second_land[secondary][roll]
            elif self.habitat_type == "Water":
                secondary = tables.loco_second_water[primary][roll]
                if secondary in tables.loco_second_extra[primary]:
                    roll = dice.rolldie_zero(2, 6)
                    tertiary = tables.loco_second_water[secondary][roll]

        loco = [primary, secondary, tertiary]
        loco = list(filter(None, loco))
        loco = list(dict.fromkeys(loco))

        self.locomotion = loco

    # Alien Creation III: GURPS Space pg. 149
    def _gen_locomotion_flags(self):

        is_fly = False

        if "Winged Flight" in self.locomotion:
            is_fly = True
        elif "Bouyant Flight" in self.locomotion:
            is_fly = True

        self._is_flying = is_fly

    # Alien Creation IV: GURPS Space pg. 151
    def _gen_size_class(self):

        size = ""

        roll = dice.rolldie(1, 6)
        if self.chemical_basis == "Magnetic":
            roll -= 4
        if self.habitat == "Space-Dewlling":
            roll += 3
        # TODO: should this be an elif so that space-dewlling doesn't get
        #   an extra +2 for 0 gravity? or should space-dwelling just get a +1
        #   so that the 0 gravity adds up to +3?
        if self.planet.gravity < 0.5:
            roll += 2
        elif self.planet.gravity <= 0.75:
            roll += 1
        elif 1.5 <= self.planet.gravity <= 2:
            roll -= 1
        elif self.planet.gravity > 2:
            roll -= 2
        if self.habitat_type == "Water":
            roll += 1
        if self.habitat in ("Open Ocean", "Banks", "Plains"):
            roll += 1
        elif self.habitat in ("Tropical Lagoon", "River/Stream",
                              "Island/Beach", "Desert", "Mountain"):
            roll -= 1
        if "Grazing/Browsing Herbivore" in self.trophic_level:
            roll += 1
        if "Parasite/Symbiont" in self.trophic_level:
            roll -= 4
        if "Slithering" in self.locomotion:
            roll -= 1
        if "Winged Flight" in self.locomotion:
            roll -= 3

        if roll <= 2:
            size = "Small"
        elif roll <= 4:
            size = "Human-Scale"
        else:
            roll = dice.rolldie(1, 6)
            if roll < 6:
                size = "Large"
            else:
                size = "Huge"

        self.size_class = size

    # Alien Creation IV: GURPS Space pg. 151
    def _gen_size_volume(self):

        volume = 0

        roll = dice.rolldie_zero(1, 6)
        if self.size_class == "Small":
            volume = tables.size_volume_small[roll]
        elif self.size_class == "Human-Scale":
            volume = tables.size_volume_human[roll]
        elif self.size_class == "Large":
            roll = dice.rolldie_zero(1, 5)
            volume = tables.size_volume_large[roll]
        elif self.size_class == "Huge":
            volume = dice.rolldie(2, 6) * 10

        if self.planet.gravity < 0.15:
            mult = 4.6
        elif self.planet.gravity < 0.25:
            mult = 2.9
        elif self.planet.gravity < 0.35:
            mult = 2.2
        elif self.planet.gravity < 0.45:
            mult = 1.8
        elif self.planet.gravity < 0.55:
            mult = 1.6
        elif self.planet.gravity < 0.65:
            mult = 1.4
        elif self.planet.gravity < 0.75:
            mult = 1.3
        elif self.planet.gravity < 0.85:
            mult = 1.2
        elif self.planet.gravity < 0.95:
            mult = 1.1
        elif self.planet.gravity < 1.125:
            mult = 1
        elif self.planet.gravity < 1.375:
            mult = 0.9
        elif self.planet.gravity < 1.75:
            mult = 0.75
        elif self.planet.gravity < 2.25:
            mult = 0.6
        elif self.planet.gravity < 3:
            mult = 0.5
        elif self.planet.gravity < 4.25:
            mult = 0.4
        else:
            mult = 0.3
        if not ((self.habitat_type == "Water"
                 and "Winged Flight" not in self.locomotion)
                or "Bouyant Flight" in self.locomotion):
            volume *= mult

        if self.chemical_basis == "Magnetic":
            volume /= 1000

        self.size_volume = volume

    # Alien Creation IV: GURPS Space pg. 151
    def _gen_size_mass(self):

        mass = 0
        volume = self.size_volume

        if self.chemical_basis == "Magnetic":
            volume *= 1000

        mass = ((self.size_volume / 2) ** 3) * 200

        if self.chemical_basis in ("Silicon/Sulfuric Acid",
                                   "Silicon/Liquid Sulfur",
                                   "Silicon/Liquid Rock"):
            mass *= 2
        elif self.chemical_basis in ("Hydrogen-Based", "Plasma"):
            mass /= 10
        if self.habitat == "Space-Dwelling":
            mass /= 5

        self.size_mass = mass

    # Alien Creation IV: GURPS Space pg. 151
    def _gen_size_weight(self):
        self.size_weight = self.size_mass * self.planet.gravity

    # Alien Creation IV: GURPS Space pg. 151
    def _gen_stat_st(self):
        self.stat_st = max(1, round(2 * (self.size_mass ** (1./3.))))

    # Alien Anatomy - Mobility - Walking: GURPS Space pg. 146
    def _gen_stat_move(self):
        walk = (((self.size_volume / 2) * self.planet.gravity) ** (1./2.)) * 5
        self.stat_move_walk = walk

    # Alien Creation V: GURPS Space pg. 154
    def _gen_body_symmetry(self):

        symmetry = ""

        roll = dice.rolldie_zero(2, 6)
        if ("Immobile" in self.locomotion
                or "Bouyant Flight" in self.locomotion
                or self.habitat_type == "Space-Dwelling"):
            roll += 1
        symmetry = tables.body_symmetry[roll]

        self.body_symmetry = symmetry

    # Alien Creation V: GURPS Space pg. 154
    def _gen_body_sides(self):

        sides = 0

        if self.body_symmetry == "Bilateral":
            sides = 2
        elif self.body_symmetry == "Trilateral":
            sides = 3
        elif self.body_symmetry == "Radial":
            sides = dice.rolldie(1, 6) + 3
        elif self.body_symmetry == "Spherical":
            roll = dice.rolldie_zero(1, 6)
            sides = (4, 6, 6, 8, 12, 20)[roll]

        self.body_sides = sides

    # Alien Creation V: GURPS Space pg. 154
    def _gen_body_limbs(self):

        segments = 0
        limbs = 0

        if self.body_symmetry == "Spherical":
            limbs = self.body_sides
        elif self.body_symmetry == "Asymmetric":
            limbs = dice.rolldie(2, 6) - 2
        else:
            roll = dice.rolldie(1, 6)

            if self.body_symmetry == "Trilateral":
                roll -= 1
            elif self.body_symmetry == "Radial":
                roll -= 2

            if roll == 2:
                segments = 1
                limbs = self.body_sides
            elif roll == 3:
                segments = 2
                limbs = self.body_sides * 2
            elif roll == 4:
                segments = dice.rolldie(1, 6)
                limbs = segments * self.body_sides
            elif roll == 5:
                segments = dice.rolldie(2, 6)
                limbs = segments * self.body_sides
            elif roll == 6:
                segments = dice.rolldie(3, 6)
                limbs = segments * self.body_sides

        self.body_segments = segments
        self.body_limbs = limbs

    # Alien Creation V: GURPS Space pg. 154
    def _gen_body_tail(self):

        tail = []

        roll = dice.rolldie(1, 6)
        if "Swimming" in self.locomotion:
            roll += 1

        if (self.body_symmetry != "Spherical"
                and roll >= 5):
            roll = dice.rolldie_zero(2, 6)
            tail.append(tables.body_tail_features[roll])
            while "Combination" in tail:
                tail.clear()
                roll1 = dice.rolldie_zero(1, 6) + 5
                roll2 = dice.rolldie_zero(1, 6) + 5
                tail.append(tables.body_tail_features[roll1])
                tail.append(tables.body_tail_features[roll2])
                tail = list(dict.fromkeys(tail))

        self.body_tail = tail

    # TODO: Separate into functions for
    #   manipulators, skeleton, wingspan
    def _gen_bodyplan(self):

        manipulators = ""
        manip_sets = 0
        manip_badgrip = 0
        manip_normaldx = 0
        manip_highdx = 0
        skeleton = ""

        # Manipulators
        if self.sapient is True:
            roll = dice.rolldie(1, 6) + 6
        else:
            roll = dice.rolldie(2, 6)
        if self.body_limbs == 2:
            roll -= 1
        if self.body_limbs > 6:
            roll += 2
        elif self.body_limbs > 4:
            roll += 1
        if "Winged Flight" in self.locomotion:
            roll -= 1
        if ((self.habitat == "Open Ocean"
             and "Swimming" in self.locomotion)
                or (self.habitat_type == "Gas Giant")):
            roll -= 2
        # TODO: Brachiator is NOT A THING, figure out how to deal with it
        if "Brachiator" in self.locomotion:
            roll += 2
        if "Gathering Herbivore" in self.trophic_level:
            roll += 1

        if (roll < 7 or self.body_limbs == 0):
            manipulators = "No Manipulators"
        elif roll < 8:
            manip_sets = 1
            manip_badgrip = 1
        elif roll < 9:
            manipulators = "Prehensile Tail or Trunk"
        elif roll < 10:
            manip_sets = 1
            manip_normaldx = 1
        elif roll < 11:
            manip_sets = 2
            if manip_sets > self.body_limbs:
                manip_sets = self.body_limbs
            for _ in range(manip_sets):
                roll = dice.rolldie(1, 6)
                if roll < 5:
                    manip_badgrip = manip_badgrip + 1
                else:
                    manip_normaldx = manip_normaldx + 1
        elif roll < 12:
            manip_sets = dice.rolldie(1, 6)
            if manip_sets > self.body_limbs:
                manip_sets = self.body_limbs
            for _ in range(manip_sets):
                roll = dice.rolldie(1, 6)
                if roll < 5:
                    manip_badgrip = manip_badgrip + 1
                else:
                    manip_normaldx = manip_normaldx + 1
        else:
            manip_sets = 2
            if manip_sets > self.body_limbs:
                manip_sets = self.body_limbs
            for _ in range(manip_sets):
                roll = dice.rolldie(1, 6)
                if roll < 5:
                    manip_normaldx = manip_normaldx + 1
                else:
                    manip_highdx = manip_highdx + 1

        if manipulators == "":
            manipulators = "{} Sets of Manipulators; ".format(manip_sets)
            manipulators += "{} Bad Grip, ".format(manip_badgrip)
            manipulators += "{} Normal DX, ".format(manip_normaldx)
            manipulators += "{} High DX".format(manip_highdx)

        # TODO: change function to return manipulator set numbers ???????
        #   got to be a better way to handle this

        # Skeleton
        roll = dice.rolldie_zero(2, 6)
        if self.size_class == "Human-Scale":
            roll += 1
        elif self.size_class == "Large":
            roll += 2
        if self.habitat_type == "Land":
            roll += 1
        if ("Immobile" in self.locomotion
                or "Slithering" in self.locomotion):
            roll -= 1
        if self.body_symmetry == "Asymmetric":
            roll -= 1
        if self.planet.gravity < 0.5:
            roll -= 1
        if self.planet.gravity > 1.25:
            roll += 1
        if roll < 0:
            roll = 0
        if roll > 14:
            roll = 14
        skeleton = tables.body_skeleton[roll]
        # TODO: deal with Combination skeletons?

        # TODO: Wingspan calculation

        self.body_manip = manipulators
        self.body_skel = skeleton

    # Alien Creation VI: GURPS Space pg. 157
    # TODO: Separate into functions for
    #   skin type, skin ??? I may be misreading these tables
    def _gen_skin(self):
        skincover = ""
        covertype = ""

        roll = dice.rolldie_zero(1, 6)
        if self.body_skel == "External skeleton":
            covertype = "Exoskeleton"
        else:
            covertype = tables.skin_covertype[roll]

        if covertype == "Skin":
            roll = dice.rolldie_zero(2, 6)
            if self.habitat == "Arctic":
                roll += 1
            if self.habitat == "Desert":
                roll -= 1
            if self.habitat_type == "Water":
                roll += 1
            if ("Gathering Herbivore" in self.trophic_level
                    or "Grazing/Browsing Herbivore" in self.trophic_level):
                roll += 1
            if self._is_flying:
                roll -= 5
            if roll < 0:
                roll = 0
            skincover = tables.skin_skin[roll]
            if skincover == "Blubber":
                roll = dice.rolldie(1, 6)
                skincover = "Blubber (DR 4, "
                skincover += "+{} Temperature Tolerance)".format(roll)
        elif covertype == "Scales":
            roll = dice.rolldie_zero(2, 6)
            if self.habitat == "Desert":
                roll += 1
            if ("Gathering Herbivore" in self.trophic_level
                    or "Grazing/Browsing Herbivore" in self.trophic_level):
                roll += 1
            if self._is_flying:
                roll -= 2
            if "Digging" in self.locomotion:
                roll -= 1
            if roll < 0:
                roll = 0
            skincover = tables.skin_scales[roll]
        elif covertype == "Fur":
            roll = dice.rolldie_zero(2, 6)
            if self.habitat == "Desert":
                roll -= 1
            if self.habitat == "Arctic":
                roll += 1
            if self._is_flying:
                roll -= 1
            if ("Gathering Herbivore" in self.trophic_level
                    or "Grazing/Browsing Herbivore" in self.trophic_level):
                roll += 1
            if roll < 0:
                roll = 0
            skincover = tables.skin_fur[roll]
        elif covertype == "Feathers":
            roll = dice.rolldie_zero(2, 6)
            if self.habitat == "Desert":
                roll -= 1
            if self.habitat == "Arctic":
                roll += 1
            if self._is_flying:
                roll += 1
            if roll < 0:
                roll = 0
            skincover = tables.skin_feathers[roll]
        elif covertype == "Exoskeleton":
            roll = dice.rolldie_zero(1, 6)
            if self.habitat_type == "Water":
                roll += 1
            if "Immobile" in self.locomotion:
                roll += 1
            if self._is_flying:
                roll -= 2
            if roll < 0:
                roll = 0
            skincover = tables.skin_exoskeleton[roll]

        self.skin_type = covertype
        self.skin_detail = skincover

    # Alien Creation VI: GURPS Space pg. 157
    def _gen_breathing(self):
        breathing = ""

        if self._is_flying:
            breathing = "Lungs"
        elif (self.habitat_type != "Water"
              and "Swimming" not in self.locomotion):
            breathing = "Lungs"
        elif self.habitat_type == "Gas Giant":
            breathing = "Lungs"
        elif self.habitat_type == "Space-Dwelling":
            breathing = "Doesn't Breathe (Space-Dwelling)"
        elif self.habitat == "Deep-Ocean Vents":
            breathing = "Doesn't Breathe (Gills)"
        else:
            roll = dice.rolldie(2, 6)
            if (self.habitat == "Arctic"
                    or self.habitat == "Swampland"
                    or self.habitat == "River/Stream"
                    or self.habitat == "Island/Beach"
                    or self.habitat == "Tropical Lagoon"):
                roll += 1
            if "Walking" in self.locomotion:
                roll += 1
            if (self._is_flying
                    or "Climbing" in self.locomotion):
                roll += 2
            if roll < 7:
                breathing = "Doesn't Breathe (Gills)"
            elif roll < 9:
                breathing = "Lungs (air-breathing), "
                breathing += "Doesn't Breathe (Oxygen Storage)"
            elif roll < 11:
                breathing = "Doesn't Breathe (Gills), "
                breathing += "Lungs or convertable organ"
            else:
                breathing = "Lungs"

        self.breathing = breathing

    # Alien Creation VI: GURPS Space pg. 157
    def _gen_temperature_regulation(self):
        temp_reg = ""

        roll = dice.rolldie(2, 6)

        if ("Lungs (air-breathing)" in self.breathing
                or self.breathing == "Lungs"):
            roll += 1
        elif "Doesn't Breathe (Gills)" in self.breathing:
            roll -= 1
        if self.size_class != "Small":
            roll += 1
        if self.habitat_type == "Land":
            roll += 1
            if (self.habitat == "Woodlands"
                    or self.habitat == "Mountain"):
                roll += 1
            elif self.habitat == "Arctic":
                roll += 2

        if roll < 5:
            temp_reg = "Cold-blooded (with disadvantage)"
        elif roll < 7:
            temp_reg = "Cold-blooded (no disadvantage)"
        elif roll < 8:
            temp_reg = "Partial regulation (temperature varies within limits)"
        elif roll < 10:
            temp_reg = "Warm-blooded"
        else:
            temp_reg = "Warm-blooded (with Metabolism Control 2)"

        self.temperature_regulation = temp_reg

    # Alien Creation VI: GURPS Space pg. 158
    def _gen_growth(self):
        growth_pattern = ""

        roll = dice.rolldie(2, 6)

        if self.body_skel == "External skeleton":
            roll -= 1
        if self.size_class == "Large":
            roll += 1
        if "Immobile" in self.locomotion:
            roll += 1

        if roll < 5:
            growth_pattern = "Metamorphosis"
        elif roll < 7:
            growth_pattern = "Molting"
        elif roll < 12:
            growth_pattern = "Continuous Growth"
        else:
            growth_pattern = "Unusual Growth Pattern "
            growth_pattern += "(adding segments, branching, etc.)"

        self.growth_pattern = growth_pattern

    # TODO: Lifespan, GURPS Space pg. 159

    # Alien Creation VII: GURPS Space pg. 161
    def _gen_sexes(self):
        sexes = ""

        def sexroll():
            sroll = dice.rolldie(2, 6)
            if "Immobile" in self.locomotion:
                sroll = sroll - 1
            if self.body_symmetry == "Asymmetric":
                sroll = sroll - 1
            if self._is_autotroph:
                sroll = sroll - 1
            return sroll

        roll = sexroll()
        if roll < 5:
            sexes = "Asexual Reproduction or Parthenogenesis"
        elif roll < 7:
            sexes = "Hermaphrodite"
        elif roll < 10:
            sexes = "Two"
        elif roll < 11:
            sexes = "Switching Between Male and Female"
        elif roll < 12:
            roll = dice.rolldie(1, 6)
            if roll < 4:
                sexes = "Three"
            elif roll < 6:
                sexes = "Four"
            else:
                sexes = str(dice.rolldie(2, 6))
        else:
            roll = sexroll()
            if roll < 5:
                sex1 = "Asexual Reproduction or Parthenogenesis"
            elif roll < 7:
                sex1 = "Hermaphrodite"
            elif roll < 10:
                sex1 = 2
            elif roll < 11:
                sex1 = "Switching Between Male and Female"
            else:
                roll = dice.rolldie(1, 6)
                if roll < 4:
                    sex1 = 3
                elif roll < 6:
                    sex1 = 4
                else:
                    sex1 = dice.rolldie(2, 6)
            roll = sexroll()
            if roll < 5:
                sex2 = "Asexual Reproduction or Parthenogenesis"
            elif roll < 7:
                sex2 = "Hermaphrodite"
            elif roll < 10:
                sex2 = 2
            elif roll < 11:
                sex2 = "Switching Between Male and Female"
            else:
                roll = dice.rolldie(1, 6)
                if roll < 4:
                    sex2 = 3
                elif roll < 6:
                    sex2 = 4
                else:
                    sex2 = dice.rolldie(2, 6)
            sexes = "Alternating/Conditional: {} & {}".format(sex1, sex2)

        self.sexes = sexes

    # Alien Creation VII: GURPS Space pg. 161
    def _gen_gestation(self):
        gest = ""
        gest_special = ""

        roll = dice.rolldie(2, 6)
        if (self.habitat_type == "Water"
                or "Swimming" in self.locomotion):
            roll -= 1
        if "Immobile" in self.locomotion:
            roll -= 2
        if "Warm-blooded" in self.temperature_regulation:
            roll += 1

        if roll < 7:
            gest = "Spawning/Pollinating"
        elif roll < 9:
            gest = "Egg-Laying"
        elif roll < 11:
            gest = "Live-Bearing"
        else:
            gest = "Live-Bearing with Pouch"

        roll = dice.rolldie(2, 6)
        if roll == 12:
            roll = dice.rolldie(1, 6)
            if roll < 2:
                gest_special = "Brood Parasite (raised by another species)"
            elif roll < 4:
                gest_special = "Parasitic Young (implanted in a host)"
            elif roll < 6:
                gest_special = "Cannibalistic Young (fatal to parent)"
            else:
                gest_special = "Cannibalistic Young (consume each other)"

        self.gestation = gest
        self.gestation_special = gest_special

    # Alien Creation VII: GURPS Space pg. 161
    def _gen_reproductive_strat(self):
        strat = ""

        roll = dice.rolldie(2, 6)
        if self.size_class == "Large":
            roll -= 1
        elif self.size_class == "Small":
            roll += 1
        if self.gestation == "Spawning/Pollinating":
            roll += 2

        if roll < 5:
            if self.gestation == "Spawning/Pollinating":
                strat = "Strong K-Strategy: 20 - 120 offspring, "
                strat += "extensive care after birth"
            else:
                strat = "Strong K-Strategy: 1 offspring, "
                strat += "extensive care after birth"
        elif roll < 7:
            litter_l = 1
            litter_h = 2
            if self.gestation == "Spawning/Pollinating":
                mult = 10 * dice.rolldie(2, 6)
                litter_l = litter_l * mult
                litter_h = litter_h * mult
            strat = "Moderate K-Strategy: {} - {} ".format(litter_l, litter_h)
            strat += "offspring per litter, extensive care after birth"
        elif roll < 8:
            litter_l = 1
            litter_h = 6
            if self.gestation == "Spawning/Pollinating":
                mult = 10 * dice.rolldie(2, 6)
                litter_l = litter_l * mult
                litter_h = litter_h * mult
            strat = "Median Strategy: {} - {} ".format(litter_l, litter_h)
            strat += "offspring per litter, moderate care after birth"
        elif roll < 10:
            litter_l = 2
            litter_h = 7
            if self.gestation == "Spawning/Pollinating":
                mult = 10 * dice.rolldie(2, 6)
                litter_l = litter_l * mult
                litter_h = litter_h * mult
            strat = "Moderate r-Strategy: {} - {} ".format(litter_l, litter_h)
            strat += "offspring per litter, some care after birth"
        else:
            litter_l = 2
            litter_h = 12
            if self.gestation == "Spawning/Pollinating":
                mult = 10 * dice.rolldie(2, 6)
                litter_l = litter_l * mult
                litter_h = litter_h * mult
            strat = "Strong r-Strategy: {} - {} ".format(litter_l, litter_h)
            strat += "offspring per litter, no care, +1 Short Lifespan"

        self.reproductive_strat = strat

    # Alien Creation VIII: GURPS Space pg. 164
    # TODO: Bundle senses into their own datastructure / class
    # TODO: Separate into functions for
    #   vision, hearing, touch, taste/smell, special senses,
    #   primary + secondary sense, communication channels
    def _gen_senses(self):
        primary = ""
        vision = ""
        hearing = ""
        touch = ""
        tastesmell = ""
        comms_a = ""
        comms_b = ""
        special = []

        sense_roll = {"Vision": 0,
                      "Hearing": 0,
                      "Touch": 0,
                      "Taste/Smell": 0}
        sense_comm = {"Vision": 0,
                      "Hearing": 0,
                      "Touch": 0,
                      "Taste/Smell": 0}

        # Primary Sense
        roll = dice.rolldie(3, 6)
        if self.habitat_type == "Water":
            roll -= 2
        if self._is_autotroph:
            roll += 2

        if roll < 8:
            primary = "Hearing"
        elif roll < 13:
            primary = "Vision"
        else:
            primary = "Touch and Taste"

        # Vision
        roll_v = dice.rolldie(3, 6)
        if primary == "Vision":
            roll_v = roll_v + 4
        if self.locomotion[0] == "Digging":
            roll_v = roll_v - 4
        if "Climbing" in self.locomotion:
            roll_v = roll_v + 2
        if self._is_flying:
            roll_v = roll_v + 3
        if "Immobile" in self.locomotion:
            roll_v = roll_v - 4
        if self.habitat == "Deep-Ocean Vents":
            roll_v = roll_v - 4
        if "Filter-Feeder" in self.trophic_level:
            roll_v = roll_v - 2
        if (self._is_carnivore
                or "Gathering Herbivore" in self.trophic_level):
            roll_v = roll_v + 2
        if self.habitat_type == "Space-Dwelling":
            if roll_v < 10:
                roll_v = 3

        if roll_v < 7:
            vision = "Blindness"
        elif roll_v < 8:
            vision = "Blindness (Can sense light and dark, -10%)"
        elif roll_v < 10:
            vision = "Bad Sight and Colorblindness"
        elif roll_v < 12:
            vision = "Bad Sight or Colorblindness"
        elif roll_v < 15:
            vision = "Normal Vision"
        else:
            vision = "Telescopic Vision 4"

        # Hearing
        roll_h = dice.rolldie(3, 6)
        if roll_v < 8:
            roll_h = roll_h + 2
        elif roll_v < 12:
            roll_h = roll_h + 1
        if self.habitat_type == "Water":
            roll_h = roll_h + 1
        if "Immobile" in self.locomotion:
            roll_h = roll_h - 4
        if self.habitat_type == "Space-Dwelling":
            roll_h = 0

        if roll_h < 7:
            hearing = "Deafness"
        elif roll_h < 8:
            hearing = "Hard of Hearing"
        elif roll_h < 11:
            hearing = "Normal Hearing"
        elif roll_h < 12:
            if (self.size_class == "Large"
                    or self.size_class == "Huge"):
                hearing = "Normal Hearing with extended range"
                hearing += " (Subsonic Hearing)"
            else:
                hearing = "Normal Hearing with extended range (Ultrahearing)"
        elif roll_h < 13:
            hearing = "Acute Hearing 4"
        elif roll_h < 14:
            hearing = "Acute Hearing 4 and either"
            hearing += " Subsonic Hearing or Ultrahearing"
        else:
            hearing = "Acute Hearing 4 with Ultrasonic Hearing and Sonar"

        # Touch
        roll_t = dice.rolldie(2, 6)
        if self.body_skel == "External skeleton":
            roll_t = roll_t - 2
        if self.habitat_type == "Water":
            roll_t = roll_t + 2
        if "Digging" in self.locomotion:
            roll_t = roll_t + 2
        if self._is_flying:
            roll_t = roll_t - 2
        if roll_v < 8:
            roll_t = roll_t + 2
        if "Trapping Carnivore" in self.trophic_level:
            roll_t = roll_t + 1
        if self.size_class == "Small":
            roll_t = roll_t + 1

        if roll_t < 3:
            touch = "Numb"
        elif roll_t < 5:
            touch = "-2 DX from poor sense of touch"
        elif roll_t < 7:
            touch = "-1 DX from poor sense of touch"
        elif roll_t < 9:
            touch = "Human-level touch"
        elif roll_t < 11:
            touch = "Acute Touch 4"
        else:
            touch = "Acute Touch 4 and either"
            touch += " Senstive Touch or Vibration Sense"

        # Taste/Smell
        roll_s = dice.rolldie(2, 6)
        if ("Chasing Carnivore" in self.trophic_level
                or "Gathering Herbivore" in self.trophic_level):
            roll_s = roll_s + 2
        if("Filter-Feeder" in self.trophic_level
           or "Trapping Carnivore" in self.trophic_level
           or self._is_autotroph):
            roll_s = roll_s - 2
        if self.sexes != "Asexual Reproduction or Parthenogenesis":
            roll_s = roll_s + 2
        if "Immobile" in self.locomotion:
            roll_s = roll_s - 4

        if roll_s < 4:
            tastesmell = "No Sense of Smell/Taste"
        elif roll_s < 6:
            tastesmell = "No Sense of Smell (can taste, -50%)"
        elif roll_s < 9:
            tastesmell = "Normal taste/smell"
        elif roll_s < 11:
            if self.habitat_type == "Water":
                tastesmell = "Acute Taste 4"
            else:
                tastesmell = "Acute Taste/Smell 4"
        else:
            if self.habitat_type == "Water":
                tastesmell = "Acute Taste 4 and Discriminatory Taste"
            else:
                tastesmell = "Acute Taste/Smell 4 and Discriminatory Smell"

        # Special Senses
        #  360 Vision
        if roll_v > 6:
            roll = dice.rolldie(2, 6)
            if (self.habitat == "Desert"
                    or self.habitat == "Plains"):
                roll += 1
            if ("Gathering Herbivore" in self.trophic_level
                    or "Grazing/Browsing Herbivore" in self.trophic_level):
                roll += 1
            if (self.body_symmetry == "Radial"
                    or self.body_symmetry == "Spherical"):
                roll += 1
            if roll > 10:
                special.append("360 Vision")

        #  Absolute Direction
        roll = dice.rolldie(2, 6)
        if self.habitat == "Open Ocean":
            roll += 1
        if self._is_flying:
            roll += 1
        if "Digging" in self.locomotion:
            roll += 1
        if roll > 10:
            special.append("Absolute Direction")

        #  Discriminatory Hearing
        if roll_h > 8:
            roll = dice.rolldie(2, 6)
            if roll_h > 13:
                roll += 2
            if roll > 10:
                special.append("Discriminatory Hearing")

        #  Peripheral Vision
        if roll_v > 6:
            roll = dice.rolldie(2, 6)
            if (self.habitat == "Plains"
                    or self.habitat == "Desert"):
                roll += 1
            if ("Gathering Herbivore" in self.trophic_level
                    or "Grazing/Browsing Herbivore" in self.trophic_level):
                roll += 2
            if roll > 9:
                special.append("Peripheral Vision")

        #  Night Vision 1d+3
        if roll_v > 6:
            roll = dice.rolldie(2, 6)
            if self.habitat_type == "Water":
                roll += 2
            if self._is_carnivore:
                roll += 2
            if roll > 10:
                nvroll = dice.rolldie(1, 6) + 3
                special.append("Night Vision {}".format(nvroll))

        #  Ultravision
        if (self.habitat_type != "Water"
                and self.chemical_basis != "Ammonia-Based"):
            roll = dice.rolldie(2, 6)
            if roll > 10:
                special.append("Ultravision")
                sense_roll["Ultravision"] = roll
                sense_comm["Ultravision"] = dice.rolldie(1, 6)

        #  Detect (Heat)
        if self.habitat_type != "Water":
            roll = dice.rolldie(2, 6)
            if self._is_carnivore:
                roll += 1
            if self.habitat == "Arctic":
                roll += 1
            if roll > 10:
                special.append("Detect (Heat)")
                sense_roll["Detect (Heat)"] = roll
                sense_comm["Detect (Heat)"] = dice.rolldie(1, 6)

        #  Detect (Electric Fields)
        if self.habitat_type == "Water":
            roll = dice.rolldie(2, 6)
            if self._is_carnivore:
                roll += 1
            if roll > 10:
                special.append("Detect (Electric Fields)")
                sense_roll["Detect (Electric Fields)"] = roll
                sense_comm["Detect (Electric Fields)"] = dice.rolldie(1, 6)

        #  Perfect Balance
        if self.habitat_type == "Land":
            roll = dice.rolldie(2, 6)
            if "Climbing" in self.locomotion:
                roll += 2
            if self.habitat == "Mountain":
                roll += 1
            if self.planet.gravity <= 0.5:
                roll -= 1
            elif self.planet.gravity >= 1.5:
                roll += 1
            if roll > 10:
                special.append("Perfect Balance")

        #  Scanning Sense (Radar)
        if (self.size_class != "Small"
                or self.habitat_type != "Water"):
            roll = dice.rolldie(2, 6)
            if self.habitat_type == "Space-Dwelling":
                roll += 2
            if roll > 10:
                special.append("Scanning Sense (Radar)")
                sense_roll["Scanning Sense (Radar)"] = roll
                sense_comm["Scanning Sense (Radar)"] = dice.rolldie(1, 6)

        # Communication
        sense_roll["Vision"] = roll_v
        sense_roll["Hearing"] = roll_h
        sense_roll["Touch"] = roll_t
        sense_roll["Taste/Smell"] = roll_s

        if roll_v > 9:
            sense_comm["Vision"] = dice.rolldie(1, 6)
        if roll_h > 8:
            if roll_h > 11:
                sense_comm["Hearing"] = dice.rolldie(1, 6) + 1
            else:
                sense_comm["Hearing"] = dice.rolldie(1, 6)
        if roll_t > 8:
            sense_comm["Touch"] = dice.rolldie(1, 6)
        if roll_s > 8:
            sense_comm["Taste/Smell"] = dice.rolldie(1, 6)

        # Primary Communication Channel
        maxvalue = max(sense_comm.values())
        if maxvalue == 0:
            comms_a = "None"
            comms_b = "None"
        else:
            sense_suba = {}
            sense_subb = {}
            for key, value in sense_comm.items():
                if value == maxvalue:
                    sense_suba[key] = sense_roll[key]
            maxsub = max(sense_suba.values())
            for key, value in sense_suba.items():
                if value == maxsub:
                    sense_subb[key] = sense_suba[key]
            comms_a = random.choice(list(sense_subb.keys()))
            del sense_comm[comms_a]

        # Secondary Communication Channel
        maxvalue = max(sense_comm.values())
        if maxvalue == 0:
            comms_b = "None"
        else:
            sense_suba = {}
            sense_subb = {}
            for key, value in sense_comm.items():
                if value == maxvalue:
                    sense_suba[key] = sense_roll[key]
            maxsub = max(sense_suba.values())
            for key, value in sense_suba.items():
                if value == maxsub:
                    sense_subb[key] = sense_suba[key]
            comms_b = random.choice(list(sense_subb.keys()))
            del sense_comm[comms_b]

        self.sense_primary = primary
        self.sense_vision = vision
        self.sense_hearing = hearing
        self.sense_touch = touch
        self.sense_tastesmell = tastesmell
        self.sense_specials = special
        self.comms_a = comms_a
        self.comms_b = comms_b

    # TODO: Separate into functions for
    #   _gen_intelligence, _gen_mating, _gen_social
    # Alien Creation IX: GURPS Space pg. 168
    def _gen_intelligence(self):

        intell = ""
        stat_iq = 0
        mating = ""
        social = ""

        # Intelligence
        #  Non-Sapient
        roll = dice.rolldie(2, 6)
        if ("Filter-Feeder" in self.trophic_level
                or "Grazing/Browsing Herbivore" in self.trophic_level
                or self._is_autotroph):
            roll -= 1
        if ("Gathering Herbivore" in self.trophic_level
                or "Omnivore" in self.trophic_level):
            roll += 1
        if self.size_class == "Small":
            roll -= 1
        if "Strong K-Strategy" in self.reproductive_strat:
            roll += 1
        elif "Strong r-Strategy" in self.reproductive_strat:
            roll -= 1
        # TODO: include lifespan modifier to roll, once it's in the
        #   generator at an earlier stage
        if roll < 4:
            intell = "Mindless"
            stat_iq = 0
        elif roll < 6:
            intell = "Preprogrammed (Cannot Learn)"
            stat_iq = 1
        elif roll < 9:
            intell = "Low Intelligence (Bestial)"
            stat_iq = dice.rolldie(1, 3)
        elif roll < 11:
            intell = "High Intelligence (Bestial)"
            stat_iq = dice.rolldie(1, 3) + 2
        else:
            intell = "Presapient"
            stat_iq = 5

        #  Possibly Sapient
        if self.possible_sapient is True:
            if roll > 12:
                intell = "Sapient"

        #  Definitely Sapient
        if self.sapient is True:
            intell = "Sapient"

        if intell == "Sapient":
            stat_iq = dice.rolldie(1, 6) + 5
            if ("Filter-Feeder" in self.trophic_level
                    or "Grazing/Browsing Herbivore" in self.trophic_level
                    or self._is_autotroph):
                stat_iq = stat_iq - 1
            if ("Gathering Herbivore" in self.trophic_level
                    or "Omnivore" in self.trophic_level):
                stat_iq = stat_iq + 1
            if self.size_class == "Small":
                stat_iq = stat_iq - 1
            if "Strong K-Strategy" in self.reproductive_strat:
                stat_iq = stat_iq + 1
            elif "Strong r-Strategy" in self.reproductive_strat:
                stat_iq = stat_iq - 1
            if stat_iq < 6:
                stat_iq = 6

        # Mating Behavior
        roll = dice.rolldie(2, 6)
        if self.sexes == "Hermaphrodite":
            roll -= 2
        if self.gestation == "Spawning/Pollinating":
            roll -= 1
        if self.gestation == "Live-Bearing":
            roll += 1
        if "Strong K-Strategy" in self.reproductive_strat:
            roll += 1
        elif "Strong r-Strategy" in self.reproductive_strat:
            roll -= 1

        if roll < 6:
            mating = "Mating only, no pair bond"
        elif roll < 8:
            mating = "Temporary pair bond"
        elif roll < 9:
            mating = "Permanent pair bond"
        elif roll < 11:
            mating = "Harem"
        else:
            mating = "Hive"

        # Social Organization
        if mating == "Hive":
            social = "Hive"
        else:
            roll = dice.rolldie(2, 6)
            if self._is_carnivore:
                roll -= 1
            if "Grazing/Browsing Herbivore" in self.trophic_level:
                roll += 1
            if (self.size_class == "Large"
                    or self.size_class == "Huge"):
                roll -= 1
            if mating == "Harem":
                roll += 1
            if mating == "Mating only, no pair bond":
                roll -= 1

            if roll < 7:
                social = "Solitary"
            elif roll < 9:
                social = "Pair-bonded"
            elif roll < 11:
                social = "Troop of 4 - 10 members"
            elif roll < 12:
                social = "Pack of 6 - 20 members"
            else:
                social = "Herd of 10+ members"

        self.intelligence = intell
        self.stat_iq = stat_iq
        self.mating = mating
        self.social_organization = social

    # Alien Creation X: GURPS Space pg. 169
    def _gen_personality(self):
        self._gen_p_chauvinism()
        self._gen_p_concentration()
        self._gen_p_curiosity()
        self._gen_p_egoism()
        self._gen_p_empathy()
        self._gen_p_gregariousness()
        self._gen_p_imagination()
        self._gen_p_suspicion()
        self._gen_p_playfulness()
        self._gen_p_traits_chauvinism()
        self._gen_p_traits_concentration()
        self._gen_p_traits_curiosity()
        self._gen_p_traits_egoism()
        self._gen_p_traits_empathy()
        self._gen_p_traits_gregariousness()
        self._gen_p_traits_imagination()
        self._gen_p_traits_suspicion()
        self._gen_p_traits_playfulness()

    def _gen_p_chauvinism(self):

        p_cha = 0

        if self.p_more_variation is True:
            p_cha = dice.roll_2d6_subtract()

        if (self._is_autotroph
                or "Filter-Feeder" in self.trophic_level):
            p_cha -= 1
        if ("Parasite/Symbiont" in self.trophic_level
                or "Scavenger" in self.trophic_level):
            p_cha -= 2
        if (self.social_organization == "Hive"
                or self.social_organization == "Troop of 4 - 10 members"
                or self.social_organization == "Pack of 6 - 20 members"):
            p_cha += 2
        if ("Asexual" in self.sexes
                or self.gestation == "Spawning/Pollinating"):
            p_cha -= 1
        if (self.social_organization == "Solitary"
                or self.social_organization == "Pair-bonded"):
            p_cha -= 1

        self.p_chauvinism = p_cha

    def _gen_p_concentration(self):

        p_con = 0

        if self.p_more_variation is True:
            p_con = dice.roll_2d6_subtract()

        if ("Pouncing Carnivore" in self.trophic_level
                or "Chasing Carnivore" in self.trophic_level):
            p_con += 1
        if self._is_herbivore:
            p_con -= 1
        if "Strong K-Strategy" in self.reproductive_strat:
            p_con += 1

        self.p_concentration = p_con

    def _gen_p_curiosity(self):

        p_cur = 0

        if self.p_more_variation is True:
            p_cur = dice.roll_2d6_subtract()

        if "Omnivore" in self.trophic_level:
            p_cur += 1
        if ("Grazing/Browsing Herbivore" in self.trophic_level
                or "Filter-Feeder" in self.trophic_level):
            p_cur -= 1
        if "Blindness" in self.sense_vision:
            p_cur -= 1
        if "Strong r-Strategy" in self.reproductive_strat:
            p_cur -= 1
        if "Strong K-Strategy" in self.reproductive_strat:
            p_cur += 1

        self.p_curiosity = p_cur

    def _gen_p_egoism(self):

        p_ego = 0

        if self.p_more_variation is True:
            p_ego = dice.roll_2d6_subtract()

        if self.social_organization == "Solitary":
            p_ego += 1
        if self.social_organization == "Hive":
            p_ego -= 1
        if "Strong K-Strategy" in self.reproductive_strat:
            p_ego += 1
        if "Strong r-Strategy" in self.reproductive_strat:
            p_ego -= 1

        self.p_egoism = p_ego

    def _gen_p_empathy(self):

        p_emp = 0

        if self.p_more_variation is True:
            p_emp = dice.roll_2d6_subtract()

        if "Chasing Carnivore" in self.trophic_level:
            p_emp += 1
        if (self._is_autotroph
                or "Filter-Feeder" in self.trophic_level
                or "Grazing/Browsing Herbivore" in self.trophic_level
                or "Scavenger" in self.trophic_level):
            p_emp -= 1
        if (self.social_organization == "Solitary"
                or self.social_organization == "Pair-bonded"):
            p_emp -= 1
        if (self.social_organization == "Troop of 4 - 10 members"
                or self.social_organization == "Pack of 6 - 20 members"):
            p_emp += 1
        if "Strong K-Strategy" in self.reproductive_strat:
            p_emp += 1

        self.p_empathy = p_emp

    def _gen_p_gregariousness(self):

        p_gre = 0

        if self.p_more_variation is True:
            p_gre = dice.roll_2d6_subtract()

        if ("Pouncing Carnivore" in self.trophic_level
                or "Scavenger" in self.trophic_level
                or "Filter-Feeder" in self.trophic_level
                or self._is_autotroph
                or self._is_herbivore):
            p_gre -= 1
        if (self.social_organization == "Solitary"
                or self.social_organization == "Pair-bonded"):
            p_gre -= 1
        if (self.social_organization == "Pack of 6 - 20 members"
                or self.social_organization == "Herd of 10+ members"):
            p_gre += 1
        if self.social_organization == "Hive":
            p_gre += 2
        if ("Asexual" in self.sexes
                or "Hermaphrodite" in self.sexes):
            p_gre -= 1
        if self.gestation == "Spawning/Pollinating":
            p_gre -= 1

        self.p_gregariousness = p_gre

    def _gen_p_imagination(self):

        p_ima = 0

        if self.p_more_variation is True:
            p_ima = dice.roll_2d6_subtract()

        if ("Pouncing Carnivore" in self.trophic_level
                or "Omnivore" in self.trophic_level
                or "Gathering Herbivore" in self.trophic_level):
            p_ima += 1
        if (self._is_autotroph
                or "Filter-Feeder" in self.trophic_level
                or "Grazing/Browsing Herbivore" in self.trophic_level):
            p_ima -= 1
        if "Strong K-Strategy" in self.reproductive_strat:
            p_ima += 1
        if "Strong r-Strategy" in self.reproductive_strat:
            p_ima -= 1

        self.p_imagination = p_ima

    def _gen_p_suspicion(self):

        p_sus = 0

        if self.p_more_variation is True:
            p_sus = dice.roll_2d6_subtract()

        if self._is_carnivore:
            p_sus -= 1
        if "Grazing/Browsing Herbivore" in self.trophic_level:
            p_sus += 1
        if "Blindness" in self.sense_vision:
            p_sus += 1
        if (self.size_class == "Large"
                or self.size_class == "Huge"):
            p_sus -= 1
        elif self.size_class == "Small":
            p_sus += 1
        if (self.social_organization == "Solitary"
                or self.social_organization == "Pair-bonded"):
            p_sus += 1

        self.p_suspicion = p_sus

    def _gen_p_playfulness(self):

        p_pla = 0

        if self.p_more_variation is True:
            p_pla = dice.roll_2d6_subtract()

        if "K-Strategy" in self.reproductive_strat:
            p_pla += 1
        if "Strong K-Strategy" in self.reproductive_strat:
            p_pla += 1
        if self.stat_iq > 1:
            p_pla += 1
        if self.social_organization == "Solitary":
            p_pla -= 1
        if self.stat_iq < 2:
            p_pla -= 3

        self.p_playfulness = p_pla

    def _gen_p_traits_chauvinism(self):

        t_cha = ""

        if self.p_chauvinism > 2:
            if self.p_suspicion > 1:
                t_cha = "Xenophobia"
            elif (self.p_empathy < 1 or self.p_suspicion > -1):
                t_cha = "Racial Intolerance"
            else:
                t_cha = "Chauvinistic (quirk)"
        elif self.p_chauvinism == 2:
            if (self.p_empathy < 1 or self.p_suspicion > -1):
                t_cha = "Racial Intolerance"
            else:
                t_cha = "Chauvinistic (quirk)"
        elif self.p_chauvinism == 1:
            if (self.p_empathy < 0 or self.p_suspicion > 0):
                t_cha = "Racial Intolerance"
            else:
                t_cha = "Chauvinistic (quirk)"
        elif self.p_chauvinism == 0:
            t_cha = "Normal"
        elif self.p_chauvinism == -1:
            t_cha = "Broad-Minded (quirk)"
        elif self.p_chauvinism == -2:
            if (self.p_suspicion < 0 and self.p_empathy > 0):
                t_cha = "Xenophilia (15)"
            else:
                t_cha = "Broad-minded (quirk)"
        elif self.p_chauvinism < -2:
            if (self.p_suspicion < 0 and self.p_empathy > 0):
                t_cha = "Xenophilia (9)"
            elif (self.p_suspicion < 0 or self.p_empathy > 0):
                t_cha = "Xenophilia (12)"
            else:
                t_cha = "Undiscriminating (quirk)"

        self.p_chauvinism_trait = t_cha

    def _gen_p_traits_concentration(self):

        t_con = ""

        if self.p_concentration > 2:
            t_con = "Single-Minded & (High Pain Threshold or one 5-pt Talent)"
        elif self.p_concentration == 2:
            t_con = "Single-Minded"
        elif self.p_concentration == 1:
            t_con = "Attentive (quirk)"
        elif self.p_concentration == 0:
            t_con = "Normal"
        elif self.p_concentration == -1:
            t_con = "Distractible (quirk)"
        elif self.p_concentration == -2:
            t_con = "Short Attention Span (12)"
        elif self.p_concentration < -2:
            t_con = "Short Attention Span (9)"

        self.p_concentration_trait = t_con

    def _gen_p_traits_curiosity(self):

        t_cur = ""

        if self.p_curiosity > 2:
            if (self.p_concentration < 1 or self.p_suspicion < 1):
                t_cur = "Curious (6)"
            else:
                t_cur = "Curious (9)"
        elif self.p_curiosity == 2:
            if self.p_concentration < 1:
                t_cur = "Curious (9)"
            else:
                t_cur = "Curious (12)"
        elif self.p_curiosity == 1:
            if self.p_concentration < 1:
                t_cur = "Curious (12)"
            else:
                t_cur = "Nosy (quirk)"
        elif self.p_curiosity == 0:
            t_cur = "Normal"
        elif self.p_curiosity == -1:
            t_cur = "Staid (quirk)"
        elif self.p_curiosity == -2:
            if self.p_suspicion < 0:
                t_cur = "Incurious (9)"
            else:
                t_cur = "Incurious (12)"
        elif self.p_curiosity < -2:
            t_cur = "Incurious (9)"

        self.p_curiosity_trait = t_cur

    def _gen_p_traits_egoism(self):

        t_ego = ""

        if self.p_egoism > 2:
            t_ego = "Selfish (9)"
        elif self.p_egoism == 2:
            if (self.p_suspicion > 0 or self.p_empathy < 0):
                t_ego = "Selfish (9)"
            else:
                t_ego = "Selfish (12)"
        elif self.p_egoism == 1:
            if (self.p_suspicion > 1 or self.p_empathy < -1):
                t_ego = "Selfish (9)"
            elif self.p_suspicion > 0:
                t_ego = "Selfish (12)"
            else:
                t_ego = "Proud (quirk)"
        elif self.p_egoism == 0:
            t_ego = "Normal"
        elif self.p_egoism == -1:
            t_ego = "Humble (quirk)"
        elif self.p_egoism == -2:
            if self.p_chauvinism > 1:
                t_ego = "Selfless (9)"
            else:
                t_ego = "Selfless (12)"
        elif self.p_egoism < -2:
            t_ego = "Selfless (6)"

        self.p_egoism_trait = t_ego

    def _gen_p_traits_empathy(self):

        t_emp = ""

        if self.p_empathy > 2:
            if self.p_gregariousness > 0:
                t_emp = "Empathy & Charitable (12)"
            else:
                t_emp = "Empathy"
        elif self.p_empathy == 2:
            t_emp = "Empathy (Sensitive)"
        elif self.p_empathy == 1:
            if (self.p_gregariousness > 0 and self.p_suspicion < 0):
                t_emp = "Sensitive"
            else:
                t_emp = "Responsive (quirk)"
        elif self.p_empathy == 0:
            t_emp = "Normal"
        elif self.p_empathy == -1:
            t_emp = "Oblivious"
        elif self.p_empathy == -2:
            t_emp = "Callous"
        elif self.p_empathy < -2:
            if self._is_carnivore:
                t_emp = "Low Empathy & Bloodlust (12)"
            else:
                t_emp = "Low Empathy"

        self.p_empathy_trait = t_emp

    def _gen_p_traits_gregariousness(self):

        t_gre = ""

        if self.p_gregariousness > 2:
            t_gre = "Gregarious"
        elif self.p_gregariousness == 2:
            t_gre = "Chummy"
        elif self.p_gregariousness == 1:
            t_gre = "Congenial (quirk)"
        elif self.p_gregariousness == 0:
            t_gre = "Normal"
        elif self.p_gregariousness == -1:
            t_gre = "Uncongenial (quirk)"
        elif self.p_gregariousness == -2:
            t_gre = "Loner (12)"
        elif self.p_gregariousness < -2:
            t_gre = "Loner (9)"

        self.p_gregariousness_trait = t_gre

    def _gen_p_traits_imagination(self):

        t_ima = ""

        if self.p_imagination < -2:
            t_ima = "Hidebound"
            self.stat_iq = max(0, self.stat_iq - 1)
        elif self.p_imagination == -2:
            t_ima = "Hidebound"
        elif self.p_imagination == -1:
            t_ima = "Dull (quirk)"
        elif self.p_imagination == 0:
            t_ima = "Normal"
        elif self.p_imagination > 0:
            if (self.p_concentration > -1 and self.p_egoism < 2):
                t_ima = "Versatile"
            else:
                t_ima = "Imaginative (quirk)"
            if (self.p_imagination > 1
                    and (self.p_egoism > 0 or self.p_concentration < 1)):
                t_ima += " & Dreamer (quirk)"
            if (self.p_imagination > 2 and self.p_empathy < 1):
                t_ima += " & Odious Racial Habit (Nonstop Idea Factory)"

        self.p_imagination_trait = t_ima

    def _gen_p_traits_suspicion(self):

        t_sus = ""

        if self.p_suspicion > 2:
            if self._is_herbivore:
                t_sus = "Fearfulness 2 & Cowardice"
            elif self._is_carnivore:
                t_sus = "Fearfulness 2 & Paranoia"
            else:
                t_sus = "Fearfulness 2"
        elif self.p_suspicion == 2:
            if self.p_curiosity < -2:
                t_sus = "Careful (quirk)"
            else:
                t_sus = "Fearfulness 1"
        elif self.p_suspicion == 1:
            if self.p_curiosity < -1:
                t_sus = "Normal"
            else:
                t_sus = "Careful (quirk)"
        elif self.p_suspicion == 0:
            t_sus = "Normal"
        elif self.p_suspicion == -1:
            t_sus = "Fearlessness 1"
        elif self.p_suspicion == -2:
            t_sus = "Fearlessness 2"
            if self.p_egoism > 1:
                t_sus += " & Overconfidence"
        elif self.p_suspicion < -2:
            if self.p_chauvinism < -2:
                t_sus = "Unfazeable"
            else:
                t_sus = "Fearlessness 3"
            if self.p_egoism > 0:
                t_sus += " & Overconfidence"

        self.p_suspicion_trait = t_sus

    def _gen_p_traits_playfulness(self):

        t_pla = ""

        if self.p_playfulness > 2:
            if "Overconfidence" in self.p_suspicion_trait:
                t_pla = "Trickster (12)"
            else:
                t_pla = "Compulsive Playfulness (9)"
        elif self.p_playfulness == 2:
            t_pla = "Compulsive Playfulness (12)"
        elif self.p_playfulness == 1:
            t_pla = "Playful (quirk)"
        elif self.p_playfulness == 0:
            t_pla = "Normal (occasionally playful)"
        elif self.p_playfulness == -1:
            t_pla = "Serious (quirk)"
        elif self.p_playfulness == -2:
            t_pla = "Odious Racial Habit (Wet Blanket)"
        elif self.p_playfulness < -2:
            t_pla = "No Sense of Humor"

        self.p_playfulness_trait = t_pla


if __name__ == '__main__':
    import planetinfo
    PLANET = planetinfo.PlanetInfo()
    ALIEN = Species(PLANET)
    ALIEN.reroll()
    ALIEN.output_text_basic()
