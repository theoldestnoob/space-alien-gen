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
        self.sapient = None
        self.possible_sapient = None
        self.chemical_basis = None
        self.habitat_type = None
        self.habitat = None
        self.trophic_level = None
        self._is_herbivore = None
        self._is_carnivore = None
        self._is_autotroph = None
        self.locomotion = None
        self._is_flying = None
        self.size_class = None
        self.size_volume = None
        self.size_mass = None
        self.size_weight = None
        self.stat_st = None
        self.stat_move_walk = None
        self.wingspan = None
        self.symmetry = None
        self.sides = None
        self.segments = None
        self.limbs = None
        self.tail = None
        self.manip = None
        self.manip_badgrip = None
        self.manip_normaldx = None
        self.manip_highdx = None
        self.manip_trunk = None
        self.skeleton = None
        self.skin_type = None
        self.skin = None
        self.breathing = None
        self.temperature_regulation = None
        self.growth_pattern = None
        self.sexes = None
        self.gestation = None
        self.gestation_special = None
        self.reproductive_strat = None
        self.reproductive_detail = None
        self.sense_roll = {}
        self.sense_comm = {}
        self.sense_primary = None
        self.sense_vision = None
        self.sense_hearing = None
        self.sense_touch = None
        self.sense_tastesmell = None
        self.sense_specials = None
        self.comms_a = None
        self.comms_b = None
        self.intelligence = None
        self.stat_iq = None
        self.mating = None
        self.social_organization = None
        self.p_more_variation = None
        self.p_chauvinism = None
        self.p_concentration = None
        self.p_curiosity = None
        self.p_egoism = None
        self.p_empathy = None
        self.p_gregariousness = None
        self.p_imagination = None
        self.p_suspicion = None
        self.p_playfulness = None
        self.p_chauvinism_trait = None
        self.p_concentration_trait = None
        self.p_curiosity_trait = None
        self.p_egoism_trait = None
        self.p_empathy_trait = None
        self.p_gregariousness_trait = None
        self.p_imagination_trait = None
        self.p_suspicion_trait = None
        self.p_playfulness_trait = None

    def generate(self):
        '''
        Generate all species attributes that have default / empty values.
        '''
        if self.sapient is None:
            self.sapient = False
        if self.possible_sapient is None:
            self.possible_sapient = True
        if self.p_more_variation is None:
            self.p_more_variation = True
        if self.chemical_basis is None:
            self._gen_chemical_basis_planet()
        if self.habitat_type is None:
            self._gen_habitat_type()
        if self.habitat is None:
            self._gen_habitat()
        if self.trophic_level is None:
            self._gen_trophic_level()
        if "Combination" in self.trophic_level:
            self._gen_trophic_level_combo()
        self._gen_trophic_filter()
        self._gen_trophic_flags()
        if self.locomotion is None:
            self._gen_locomotion_primary()
        self._gen_locomotion_secondary()
        self._gen_locomotion_flags()
        if self.size_class is None:
            self._gen_size_class()
        if self.size_volume is None:
            self._gen_size_volume()
        if self.size_mass is None:
            self._gen_size_mass()
        self._gen_size_weight()
        self._gen_stat_st()
        self._gen_stat_move()
        if self.symmetry is None:
            self._gen_symmetry()
        if self.sides is None:
            self._gen_sides()
        self._gen_limbs()
        if self.tail is None:
            self._gen_tail()
        if "Combination" in self.tail:
            self._gen_tail_combo()
        self._gen_manipulators()
        if self.skeleton is None:
            self._gen_skeleton()
        if "Combination" in self.skeleton:
            self._gen_skeleton_combo()
        if self.skin_type is None:
            self._gen_skin_type()
        if self.skin is None:
            self._gen_skin()
        if self.breathing is None:
            self._gen_breathing()
        if self.temperature_regulation is None:
            self._gen_temperature_regulation()
        if self.growth_pattern is None:
            self._gen_growth()
        if self.sexes is None:
            self._gen_sexes()
        if "Three or more" in self.sexes:
            self._gen_sex_three_or_more()
        if "Roll Twice" in self.sexes:
            self._gen_sex_roll_twice()
        if self.gestation is None:
            self._gen_gestation()
        if self.gestation_special is None:
            self._gen_gestation_special()
        if self.reproductive_strat is None:
            self._gen_reproductive_strat()
        if self.reproductive_detail is None:
            self._gen_reproductive_detail()
        self._gen_senses()
        if self.intelligence is None:
            self._gen_intelligence()
        if self.stat_iq is None:
            self._gen_stat_iq()
        if self.mating is None:
            self._gen_mating()
        if self.social_organization is None:
            self._gen_social()
        self._gen_personality()

    def output_text_basic(self):
        '''
        Output all species attributes in a structured but crude manner.
        '''
        outlist = [
            " Chemical Basis: {}".format(self.chemical_basis),
            " Habitat: {} - {}".format(self.habitat_type, self.habitat),
            " Trophic Levels: {}".format(self.trophic_level),
            " Locomotion: {}".format(self.locomotion),
            " Size: {}".format(self.size_class),
            "  Volume: {:.5f} yards".format(self.size_volume),
            "  Mass: {:.5f} lbs".format(self.size_mass),
            "  Weight: {:.5f} lbs".format(self.size_weight),
            "  ST: {:.2f}".format(self.stat_st),
            "  Move (Walking): {:.2f}".format(self.stat_move_walk),
            " Body Plan:",
            "  Symmetry: {}".format(self.symmetry),
            "  Sides: {}".format(self.sides),
            "  Segments: {}".format(self.segments),
            "  Limbs: {}".format(self.limbs),
            "  Tail: {}".format(self.tail),
            "  Manipulators: {}".format(self.manip),
            "   Bad Grip: {}".format(self.manip_badgrip),
            "   Normal DX: {}".format(self.manip_normaldx),
            "   High DX: {}".format(self.manip_highdx),
            "   Prehensile Trunk or Tail: {}".format(self.manip_trunk),
            "  Skeleton: {}".format(self.skeleton),
            "  Skin: {}".format(self.skin),
            # "  Wingspan: {}".format(self.wingspan),
            " Metabolism:",
            "  Breathing: {}".format(self.breathing),
            "  Temp. Regulation: {}".format(self.temperature_regulation),
            "  Growth Pattern: {}".format(self.growth_pattern),
            " Reproduction:",
            "  Sexes: {}".format(self.sexes),
            "  Gestation: {}".format(self.gestation),
            "   Special: {}".format(self.gestation_special),
            "  Reproductive Strategy: {}".format(self.reproductive_strat),
            "  Reproductive Detail: {}".format(self.reproductive_detail),
            " Senses:",
            "  Primary: {}".format(self.sense_primary),
            "  Vision: {}".format(self.sense_vision),
            "  Hearing: {}".format(self.sense_hearing),
            "  Touch: {}". format(self.sense_touch),
            "  Taste/Smell: {}".format(self.sense_tastesmell),
            "  Special: {}".format(self.sense_specials),
            "  Primary Communication: {}".format(self.comms_a),
            "  Secondary Communication: {}".format(self.comms_b),
            " Intelligence: {}".format(self.intelligence),
            "  IQ: {}".format(self.stat_iq),
            " Mating Behavior: {}".format(self.mating),
            " Social Organization: {}".format(self.social_organization),
            " Personality:",
            "  Chauvinism: {} ({})".format(self.p_chauvinism,
                                           self.p_chauvinism_trait),
            "  Concentration: {} ({})".format(self.p_concentration,
                                              self.p_concentration_trait),
            "  Curiosity: {} ({})".format(self.p_curiosity,
                                          self.p_curiosity_trait),
            "  Egoism: {} ({})".format(self.p_egoism,
                                       self.p_egoism_trait),
            "  Empathy: {} ({})".format(self.p_empathy,
                                        self.p_empathy_trait),
            "  Gregariousness: {} ({})".format(self.p_gregariousness,
                                               self.p_gregariousness_trait),
            "  Imagination: {} ({})".format(self.p_imagination,
                                            self.p_imagination_trait),
            "  Suspicion: {} ({})".format(self.p_suspicion,
                                          self.p_suspicion_trait),
            "  Playfulness: {} ({})".format(self.p_playfulness,
                                            self.p_playfulness_trait)
            ]

        outstr = "\n".join(outlist)

        return outstr

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
                                    "Fresh-Water Lakes",
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

        troph.append(trophtable[dice.rolldie_zero(3, 6)])

        self.trophic_level = troph

    def _gen_trophic_level_combo(self):

        if isinstance(self.trophic_level, str):
            troph = [self.trophic_level]
        else:
            troph = self.trophic_level

        if self.possible_sapient is False:
            trophtable = tables.troph_ordinary
        else:
            trophtable = tables.troph_sapient

        while "Combined" in troph:
            troph.clear()
            troph.append(trophtable[dice.rolldie_zero(3, 6)])
            troph.append(trophtable[dice.rolldie_zero(3, 6)])

        self.trophic_level = troph

    def _gen_trophic_filter(self):

        if isinstance(self.trophic_level, str):
            troph = [self.trophic_level]
        else:
            troph = self.trophic_level

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
        elif self.planet.gravity < 0.5:
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

        mult = 0
        for gravity, multiplier in tables.size_volume_gravity:
            if self.planet.gravity < gravity:
                mult = multiplier
                break
        if mult == 0:
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

    # TODO: make this function actually do something
    # Alien Anatomy - Mobility - Flying: GURPS Space pg. 148
    def _gen_wingspan(self):

        wingspan = 0

        self.wingspan = wingspan

    # Alien Creation V: GURPS Space pg. 154
    def _gen_symmetry(self):

        symmetry = ""
        sides = self.sides

        if sides is not None:
            if sides == 2:
                symmetry = "Bilateral"
            elif sides == 3:
                symmetry = "Trilateral"
            else:
                roll = dice.rolldie_zero(1, 6) + 7
                symmetry = tables.symmetry[roll]
        else:
            roll = dice.rolldie_zero(2, 6)
            if ("Immobile" in self.locomotion
                    or "Bouyant Flight" in self.locomotion
                    or self.habitat_type == "Space-Dwelling"):
                roll += 1
            symmetry = tables.symmetry[roll]

        self.symmetry = symmetry

    # Alien Creation V: GURPS Space pg. 154
    def _gen_sides(self):

        sides = 0

        if self.symmetry == "Bilateral":
            sides = 2
        elif self.symmetry == "Trilateral":
            sides = 3
        elif self.symmetry == "Radial":
            sides = dice.rolldie(1, 6) + 3
        elif self.symmetry == "Spherical":
            roll = dice.rolldie_zero(1, 6)
            sides = (4, 6, 6, 8, 12, 20)[roll]

        self.sides = sides

    # Alien Creation V: GURPS Space pg. 154
    def _gen_limbs(self):

        segments = 0
        limbs = 0

        if self.symmetry == "Spherical":
            limbs = self.sides
        elif self.symmetry == "Asymmetric":
            limbs = dice.rolldie(2, 6) - 2
        else:
            roll = dice.rolldie(1, 6)

            if self.symmetry == "Trilateral":
                roll -= 1
            elif self.symmetry == "Radial":
                roll -= 2

            if roll == 2:
                segments = 1
                limbs = self.sides
            elif roll == 3:
                segments = 2
                limbs = self.sides * 2
            elif roll == 4:
                segments = dice.rolldie(1, 6)
                limbs = segments * self.sides
            elif roll == 5:
                segments = dice.rolldie(2, 6)
                limbs = segments * self.sides
            elif roll == 6:
                segments = dice.rolldie(3, 6)
                limbs = segments * self.sides

        self.segments = segments
        self.limbs = limbs

    # Alien Creation V: GURPS Space pg. 154
    def _gen_tail(self):

        tail = []

        roll = dice.rolldie(1, 6)
        if "Swimming" in self.locomotion:
            roll += 1

        if (self.symmetry != "Spherical"
                and roll >= 5):
            roll = dice.rolldie_zero(2, 6)
            tail.append(tables.tail_features[roll])

        self.tail = tail

    def _gen_tail_combo(self):

        if isinstance(self.tail, str):
            tail = [self.tail]
        else:
            tail = self.tail

        while "Combination" in tail:
            tail.clear()
            roll1 = dice.rolldie_zero(1, 6) + 5
            roll2 = dice.rolldie_zero(1, 6) + 5
            tail.append(tables.tail_features[roll1])
            tail.append(tables.tail_features[roll2])
            tail = list(dict.fromkeys(tail))

        self.tail = tail

    # Alien Creation V: GURPS Space pg. 154
    def _gen_manipulators(self):

        manipulators = 0
        limb_sets = 0
        badgrip = 0
        normaldx = 0
        highdx = 0
        has_trunk = False

        check_badgrip = False
        check_highdx = False
        num_per_set = 0

        if self.symmetry in ("Asymmetric", "Spherical"):
            num_per_set = 1
        else:
            num_per_set = self.sides

        roll = self._gen_manip_roll()

        if roll == 8:
            # TODO: handle having a prehensile trunk or tail better
            #       maybe as part of the advantages/disadvantages refactor?
            has_trunk = True
            manipulators += 1
            roll = dice.rolldie(1, 6)
            if roll == 6:
                roll = self._gen_manip_roll()

        if roll == 7:
            limb_sets = 1
            badgrip = 1
        elif roll == 9:
            limb_sets = 1
            normaldx = 1
        elif roll == 10:
            limb_sets = 2
            check_badgrip = True
        elif roll == 11:
            limb_sets = dice.rolldie(1, 6)
            check_badgrip = True
        elif roll >= 12:
            limb_sets = dice.rolldie(1, 6)
            check_highdx = True

        limb_sets_max = int(self.limbs / num_per_set)
        if limb_sets > limb_sets_max:
            limb_sets = limb_sets_max

        if check_badgrip is True:
            for _ in range(limb_sets):
                roll = dice.rolldie(1, 6)
                if roll <= 4:
                    normaldx += 1
                else:
                    badgrip += 1
        elif check_highdx is True:
            for _ in range(limb_sets):
                roll = dice.rolldie(1, 6)
                if roll < 4:
                    normaldx += 1
                else:
                    highdx += 1

        manipulators += limb_sets * num_per_set
        badgrip *= num_per_set
        normaldx *= num_per_set
        highdx *= num_per_set

        self.manip = manipulators
        self.manip_badgrip = badgrip
        self.manip_normaldx = normaldx
        self.manip_highdx = highdx
        self.manip_trunk = has_trunk

    def _gen_manip_roll(self):

        if self.sapient is True:
            roll = dice.rolldie(1, 6) + 6
        else:
            roll = dice.rolldie(2, 6)
        if self.limbs == 2:
            roll -= 1
        elif 4 < self.limbs <= 6:
            roll += 1
        elif self.limbs > 6:
            roll += 2
        if "Winged Flight" in self.locomotion:
            roll -= 1
        if ((self.habitat == "Open Ocean"
             and "Swimming" in self.locomotion)
                or (self.habitat_type == "Gas Giant")):
            roll -= 2
        if "Gathering Herbivore" in self.trophic_level:
            roll += 1

        return roll

    # Alien Creation V: GURPS Space pg. 154
    def _gen_skeleton(self):

        skeleton = []

        roll = dice.rolldie_zero(2, 6)
        if self.size_class == "Human-Scale":
            roll += 1
        elif self.size_class in ("Large", "Huge"):
            roll += 2
        if self.habitat_type == "Land":
            roll += 1
        if self.locomotion in ("Immobile", "Slithering"):
            roll -= 1
        if self.symmetry == "Asymmetric":
            roll -= 1
        if self.planet.gravity < 0.5:
            roll -= 1
        if self.planet.gravity > 1.25:
            roll += 1
        roll = max(0, min(roll, 14))

        skeleton.append(tables.skeleton[roll])

        self.skeleton = skeleton

    def _gen_skeleton_combo(self):

        if isinstance(self.skeleton, str):
            skeleton = [self.skeleton]
        else:
            skeleton = self.skeleton

        while ("Combination" in skeleton
               or skeleton.count(skeleton[0]) > 1):
            skeleton.clear()
            roll1 = dice.rolldie_zero(1, 7) + 2
            roll2 = dice.rolldie_zero(1, 7) + 2
            skeleton.append(tables.skeleton[roll1])
            skeleton.append(tables.skeleton[roll2])

        self.skeleton = skeleton

    # TODO: separate descriptors + advantages/disadvantages
    # Alien Creation VI: GURPS Space pg. 157
    def _gen_skin_type(self):

        covertype = ""

        if "External" in self.skeleton:
            covertype = "Exoskeleton"
        else:
            roll = dice.rolldie_zero(1, 6)
            covertype = tables.skin_covertype[roll]

        self.skin_type = covertype

    def _gen_skin(self):
        covertype = self.skin_type
        skincover = ""

        if covertype == "Skin":
            skincover = self._gen_skin_skin()
        elif covertype == "Scales":
            skincover = self._gen_skin_scales()
        elif covertype == "Fur":
            skincover = self._gen_skin_fur()
        elif covertype == "Feathers":
            skincover = self._gen_skin_feathers()
        elif covertype == "Exoskeleton":
            skincover = self._gen_skin_exoskeleton()

        self.skin = skincover

    # TODO: separate descriptors + advantages/disadvantages
    def _gen_skin_skin(self):
        skin = ""

        roll = dice.rolldie_zero(2, 6)
        if self.habitat == "Arctic":
            roll += 1
        if self.habitat == "Desert":
            roll -= 1
        if self.habitat_type == "Water":
            roll += 1
        if self._is_herbivore:
            roll += 1
        if self._is_flying:
            roll -= 5
        if roll < 0:
            roll = 0
        skin = tables.skin_skin[roll]
        if skin == "Blubber":
            roll = dice.rolldie(1, 6)
            skin = "Blubber (DR 4, "
            skin += "+{} Temperature Tolerance)".format(roll)

        return skin

    # TODO: separate descriptors + advantages/disadvantages
    def _gen_skin_scales(self):
        skin = ""

        roll = dice.rolldie_zero(2, 6)
        if self.habitat == "Desert":
            roll += 1
        if self._is_herbivore:
            roll += 1
        if self._is_flying:
            roll -= 2
        if "Digging" in self.locomotion:
            roll -= 1
        if roll < 0:
            roll = 0
        skin = tables.skin_scales[roll]

        return skin

    # TODO: separate descriptors + advantages/disadvantages
    def _gen_skin_fur(self):
        skin = ""

        roll = dice.rolldie_zero(2, 6)
        if self.habitat == "Desert":
            roll -= 1
        if self.habitat == "Arctic":
            roll += 1
        if self._is_flying:
            roll -= 1
        if self._is_herbivore:
            roll += 1
        if roll < 0:
            roll = 0
        skin = tables.skin_fur[roll]

        return skin

    # TODO: separate descriptors + advantages/disadvantages
    def _gen_skin_feathers(self):
        skin = ""

        roll = dice.rolldie_zero(2, 6)
        if self.habitat == "Desert":
            roll -= 1
        if self.habitat == "Arctic":
            roll += 1
        if self._is_flying:
            roll += 1
        if roll < 0:
            roll = 0
        skin = tables.skin_feathers[roll]

        return skin

    # TODO: separate descriptors + advantages/disadvantages
    def _gen_skin_exoskeleton(self):
        skin = ""

        roll = dice.rolldie_zero(1, 6)
        if self.habitat_type == "Water":
            roll += 1
        if "Immobile" in self.locomotion:
            roll += 1
        if self._is_flying:
            roll -= 2
        if roll < 0:
            roll = 0
        skin = tables.skin_exoskeleton[roll]

        return skin

    # TODO: separate descriptors + advantages/disadvantages
    # Alien Creation VI: GURPS Space pg. 157
    def _gen_breathing(self):
        breathing = ""

        flight = ("Winged Flight", "Bouyant Flight")

        if set(self.locomotion).issubset(set(flight)):
            breathing = "Lungs"
        elif (self.habitat_type != "Water"
              and "Swimming" not in self.locomotion):
            breathing = "Lungs"
        elif self.habitat_type == "Space-Dwelling":
            breathing = "Doesn't Breathe (Space-Dwelling)"
        elif self.habitat == "Deep-Ocean Vents":
            breathing = "Doesn't Breathe (Gills)"
        else:
            roll = dice.rolldie(2, 6)
            if self.habitat in ("Arctic", "Swampland", "River/Stream",
                                "Island/Beach", "Tropical Lagoon"):
                roll += 1
            if "Walking" in self.locomotion:
                roll += 1
            if self._is_flying:
                roll += 2
            if roll <= 6:
                breathing = "Doesn't Breathe (Gills)"
            elif roll <= 8:
                breathing = "Lungs (air-breathing), "
                breathing += "Doesn't Breathe (Oxygen Storage)"
            elif roll <= 10:
                breathing = "Doesn't Breathe (Gills), "
                breathing += "Lungs (or convertable organ)"
            else:
                breathing = "Lungs"

        self.breathing = breathing

    # TODO: separate descriptors + advantages/disadvantages
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

        if roll <= 4:
            temp_reg = "Cold-blooded (with disadvantage)"
        elif roll <= 6:
            temp_reg = "Cold-blooded (no disadvantage)"
        elif roll == 7:
            temp_reg = "Partial regulation (temperature varies within limits)"
        elif roll <= 9:
            temp_reg = "Warm-blooded"
        else:
            temp_reg = "Warm-blooded (with Metabolism Control 2)"

        self.temperature_regulation = temp_reg

    # Alien Creation VI: GURPS Space pg. 158
    def _gen_growth(self):
        growth_pattern = ""

        roll = dice.rolldie(2, 6)

        if "External" in self.skeleton:
            roll -= 1
        if self.size_class in ("Large", "Huge"):
            roll += 1
        if "Immobile" in self.locomotion:
            roll += 1

        if roll <= 4:
            growth_pattern = "Metamorphosis"
        elif roll <= 6:
            growth_pattern = "Molting"
        elif roll <= 11:
            growth_pattern = "Continuous Growth"
        else:
            growth_pattern = "Unusual Growth Pattern "
            growth_pattern += "(adding segments, branching, etc.)"

        self.growth_pattern = growth_pattern

    # TODO: Lifespan, GURPS Space pg. 159

    # Alien Creation VII: GURPS Space pg. 161
    def _gen_sexes(self):
        sexes = ""

        roll = self._sex_roll()
        sexes = tables.sexes[roll]

        self.sexes = sexes

    def _gen_sex_three_or_more(self):
        sexes = self.sexes

        if sexes == "Three or more":
            sexes = self._sex_three_or_more()

        self.sexes = sexes

    def _gen_sex_roll_twice(self):
        sexes = self.sexes

        while "Roll Twice" in sexes:
            roll = self._sex_roll()
            sex1 = tables.sexes[roll]
            if sex1 == "Three or more":
                sex1 = self._sex_three_or_more()
            roll = self._sex_roll()
            sex2 = tables.sexes[roll]
            if sex2 == "Three or more":
                sex2 = self._sex_three_or_more()
            if sex1 == sex2:
                sexes = sex1
            else:
                sexes = "Alternating/Conditional: {} / {}".format(sex1, sex2)

        self.sexes = sexes

    def _sex_roll(self):
        sroll = dice.rolldie_zero(2, 6)
        if "Immobile" in self.locomotion:
            sroll = sroll - 1
        if self.symmetry == "Asymmetric":
            sroll = sroll - 1
        if self._is_autotroph:
            sroll = sroll - 1
        if sroll < 0:
            sroll = 0
        return sroll

    @staticmethod
    def _sex_three_or_more():
        roll = dice.rolldie(1, 6)
        if roll <= 3:
            sexes = "Three"
        elif roll <= 5:
            sexes = "Four"
        else:
            sexes = tables.numbers[dice.rolldie(2, 6)]
        sexes += " Sexes"
        return sexes

    # Alien Creation VII: GURPS Space pg. 161
    def _gen_gestation(self):
        gest = ""

        roll = dice.rolldie(2, 6)
        if (self.habitat_type == "Water"
                or "Swimming" in self.locomotion):
            roll -= 1
        if "Immobile" in self.locomotion:
            roll -= 2
        if "Warm-blooded" in self.temperature_regulation:
            roll += 1

        if roll <= 6:
            gest = "Spawning/Pollinating"
        elif roll <= 8:
            gest = "Egg-Laying"
        elif roll <= 10:
            gest = "Live-Bearing"
        else:
            gest = "Live-Bearing with Pouch"

        self.gestation = gest

    # Alien Creation VII: GURPS Space pg. 161
    def _gen_gestation_special(self):
        gest_special = ""

        roll = dice.rolldie(2, 6)
        if roll == 12:
            roll = dice.rolldie(1, 6)
            if roll == 1:
                gest_special = "Brood Parasite (raised by another species)"
            elif roll <= 3:
                gest_special = "Parasitic Young (implanted in a host)"
            elif roll <= 5:
                gest_special = "Cannibalistic Young (fatal to parent)"
            else:
                gest_special = "Cannibalistic Young (consume each other)"
        else:
            gest_special = "None"

        self.gestation_special = gest_special

    # Alien Creation VII: GURPS Space pg. 161
    def _gen_reproductive_strat(self):
        strat = ""

        roll = dice.rolldie(2, 6)
        if self.size_class in ("Large", "Huge"):
            roll -= 2
        elif self.size_class == "Small":
            roll += 1
        if self.gestation == "Spawning/Pollinating":
            roll += 2

        if roll <= 4:
            strat = "Strong K-Strategy"
        elif roll <= 6:
            strat = "Moderate K-Strategy"
        elif roll == 7:
            strat = "Median Strategy"
        elif roll <= 9:
            strat = "Moderate r-Strategy"
        else:
            strat = "Strong r-Strategy"

        self.reproductive_strat = strat

    def _gen_reproductive_detail(self):
        detail = ""
        extra = ""

        if "Strong K-Strategy" in self.reproductive_strat:
            litter_l = 1
            litter_h = 1
            care = "extensive"
        elif "Moderate K-Strategy" in self.reproductive_strat:
            litter_l = 1
            litter_h = 2
            care = "extensive"
        elif "Median Strategy" in self.reproductive_strat:
            litter_l = 1
            litter_h = 6
            care = "moderate"
        elif "Moderate r-Strategy" in self.reproductive_strat:
            litter_l = 2
            litter_h = 7
            care = "some"
        elif "Strong r-Strategy" in self.reproductive_strat:
            litter_l = 2
            litter_h = 12
            care = "no"
            extra = ", +1 Short Lifespan"

        if self.gestation == "Spawning/Pollinating":
            mult = 10 * dice.rolldie(2, 6)
            litter_l = litter_l * mult
            litter_h = litter_h * mult

        if litter_h == 1:
            off_num = "1"
        elif litter_h == litter_l:
            off_num = "20 - 120"
        else:
            off_num = "{} - {}".format(litter_l, litter_h)

        off_str = "{} offspring per litter".format(off_num)
        care_str = ", {} care after birth".format(care)
        detail = "".join([off_str, care_str, extra])

        self.reproductive_detail = detail

    # Alien Creation VIII: GURPS Space pg. 164
    # TODO:
    #   - Handle user input - reverse lookup sense rolls, etc
    #   - Bundle senses into their own datastructure / class
    def _gen_senses(self):

        if self.sense_primary is None:
            self._gen_senses_primary()
        self._gen_senses_vision()
        self._gen_senses_hearing()
        self._gen_senses_touch()
        self._gen_senses_tastesmell()
        if self.sense_specials is None:
            self._gen_senses_special()
        self._gen_communication_rolls()
        self._gen_communication_a()
        self._gen_communication_b()

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_senses_primary(self):
        roll = dice.rolldie(3, 6)

        if self.habitat_type == "Water":
            roll -= 2
        if self._is_autotroph:
            roll += 2

        if roll <= 7:
            primary = "Hearing"
        elif roll <= 12:
            primary = "Vision"
        else:
            primary = "Touch and Taste"

        self.sense_primary = primary

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_senses_vision(self):
        if "Vision" in self.sense_roll:
            roll = self.sense_roll["Vision"]
        else:
            roll = dice.rolldie(3, 6)

            if self.sense_primary == "Vision":
                roll += 4
            if self.locomotion[0] == "Digging":
                roll -= 4
            if "Climbing" in self.locomotion:
                roll += 2
            if self._is_flying:
                roll += 3
            if "Immobile" in self.locomotion:
                roll -= 4
            if self.habitat == "Deep-Ocean Vents":
                roll -= 4
            if "Filter-Feeder" in self.trophic_level:
                roll -= 2
            if (self._is_carnivore
                    or "Gathering Herbivore" in self.trophic_level):
                roll += 2
            if self.habitat_type == "Space-Dwelling":
                if roll < 10:
                    roll = 3

        if roll <= 6:
            vision = "Blindness"
        elif roll <= 7:
            vision = "Blindness (Can sense light and dark, -10%)"
        elif roll <= 9:
            vision = "Bad Sight and Colorblindness"
        elif roll <= 11:
            vision = "Bad Sight or Colorblindness"
        elif roll <= 14:
            vision = "Normal Vision"
        else:
            vision = "Telescopic Vision 4"

        self.sense_roll["Vision"] = roll
        self.sense_vision = vision

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_senses_hearing(self):
        if "Hearing" in self.sense_roll:
            roll = self.sense_roll["Hearing"]
        else:
            roll = dice.rolldie(3, 6)
            roll_v = self.sense_roll["Vision"]
            if roll_v <= 7:
                roll += 2
            elif roll_v <= 11:
                roll += 1
            if self.habitat_type == "Water":
                roll += 1
            if "Immobile" in self.locomotion:
                roll += 4
            if self.habitat_type == "Space-Dwelling":
                roll = 0

        if roll <= 6:
            hearing = "Deafness"
        elif roll <= 8:
            hearing = "Hard of Hearing"
        elif roll <= 10:
            hearing = "Normal Hearing"
        elif roll <= 11:
            if self.size_class in ["Large", "Huge"]:
                hearing = "Normal Hearing with extended range"
                hearing += " (Subsonic Hearing)"
            else:
                hearing = "Normal Hearing with extended range (Ultrahearing)"
        elif roll <= 12:
            hearing = "Acute Hearing 4"
        elif roll <= 13:
            hearing = "Acute Hearing 4 and either"
            hearing += " Subsonic Hearing or Ultrahearing"
        else:
            hearing = "Acute Hearing 4 with Ultrasonic Hearing and Sonar"

        self.sense_roll["Hearing"] = roll
        self.sense_hearing = hearing

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_senses_touch(self):
        if "Touch" in self.sense_roll:
            roll = self.sense_roll["Touch"]
        else:
            roll = dice.rolldie(2, 6)
            roll_v = self.sense_roll["Vision"]

            if "External" in self.skeleton:
                roll -= 2
            if self.habitat_type == "Water":
                roll += 2
            if "Digging" in self.locomotion:
                roll += 2
            if self._is_flying:
                roll -= 2
            if roll_v <= 7:
                roll += 2
            if "Trapping Carnivore" in self.trophic_level:
                roll += 1
            if self.size_class == "Small":
                roll += 1

        if roll <= 2:
            touch = "Numb"
        elif roll <= 4:
            touch = "-2 DX from poor sense of touch"
        elif roll <= 6:
            touch = "-1 DX from poor sense of touch"
        elif roll <= 8:
            touch = "Human-level touch"
        elif roll <= 10:
            touch = "Acute Touch 4"
        else:
            touch = "Acute Touch 4 and either"
            touch += " Senstive Touch or Vibration Sense"

        self.sense_roll["Touch"] = roll
        self.sense_touch = touch

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_senses_tastesmell(self):
        if "Taste/Smell" in self.sense_roll:
            roll = self.sense_roll["Taste/Smell"]
        else:
            roll = dice.rolldie(2, 6)

            if "Chasing Carnivore" in self.trophic_level:
                roll += 2
            if "Gathering Herbivore" in self.trophic_level:
                roll += 2
            if("Filter-Feeder" in self.trophic_level
               or "Trapping Carnivore" in self.trophic_level
               or self._is_autotroph):
                roll -= 2
            if self.sexes != "Asexual Reproduction or Parthenogenesis":
                roll += 2
            if "Immobile" in self.locomotion:
                roll -= 4

        if roll <= 3:
            tastesmell = "No Sense of Smell/Taste"
        elif roll <= 5:
            tastesmell = "No Sense of Smell (can taste, -50%)"
        elif roll <= 8:
            tastesmell = "Normal taste/smell"
        elif roll <= 10:
            if self.habitat_type == "Water":
                tastesmell = "Acute Taste 4"
            else:
                tastesmell = "Acute Taste/Smell 4"
        else:
            if self.habitat_type == "Water":
                tastesmell = "Acute Taste 4 and Discriminatory Taste"
            else:
                tastesmell = "Acute Taste/Smell 4 and Discriminatory Smell"

        self.sense_roll["Taste/Smell"] = roll
        self.sense_tastesmell = tastesmell

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_senses_special(self):
        special = []
        roll_v = self.sense_roll["Vision"]
        roll_h = self.sense_roll["Hearing"]

        #  360 Vision
        if roll_v >= 7:
            roll = dice.rolldie(2, 6)
            if self.habitat in ["Desert", "Plains"]:
                roll += 1
            if self._is_herbivore:
                roll += 1
            if self.symmetry in ["Radial", "Spherical"]:
                roll += 1
            if roll >= 11:
                special.append("360 Vision")

        #  Absolute Direction
        roll = dice.rolldie(2, 6)
        if self.habitat == "Open Ocean":
            roll += 1
        if self._is_flying:
            roll += 1
        if "Digging" in self.locomotion:
            roll += 1
        if roll >= 11:
            special.append("Absolute Direction")

        #  Discriminatory Hearing
        if roll_h >= 9:
            roll = dice.rolldie(2, 6)
            if roll_h >= 14:
                roll += 2
            if roll >= 11:
                special.append("Discriminatory Hearing")

        #  Peripheral Vision
        if roll_v >= 7:
            roll = dice.rolldie(2, 6)
            if self.habitat in ["Plains", "Desert"]:
                roll += 1
            if self._is_herbivore:
                roll += 2
            if roll >= 10:
                special.append("Peripheral Vision")

        #  Night Vision 1d+3
        if roll_v >= 7:
            roll = dice.rolldie(2, 6)
            if self.habitat_type == "Water":
                roll += 2
            if self._is_carnivore:
                roll += 2
            if roll >= 11:
                nvroll = dice.rolldie(1, 6) + 3
                special.append("Night Vision {}".format(nvroll))

        #  Ultravision
        if (self.habitat_type != "Water"
                and self.chemical_basis != "Ammonia-Based"):
            roll = dice.rolldie(2, 6)
            if roll >= 11:
                special.append("Ultravision")
                self.sense_roll["Ultravision"] = roll

        #  Detect (Heat)
        if self.habitat_type != "Water":
            roll = dice.rolldie(2, 6)
            if self._is_carnivore:
                roll += 1
            if self.habitat == "Arctic":
                roll += 1
            if roll >= 11:
                special.append("Detect (Heat)")
                self.sense_roll["Detect (Heat)"] = roll

        #  Detect (Electric Fields)
        if self.habitat_type == "Water":
            roll = dice.rolldie(2, 6)
            if self._is_carnivore:
                roll += 1
            if roll >= 11:
                special.append("Detect (Electric Fields)")
                self.sense_roll["Detect (Electric Fields)"] = roll

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
            if roll >= 11:
                special.append("Perfect Balance")

        #  Scanning Sense (Radar)
        if (self.size_class != "Small"
                and self.habitat_type != "Water"):
            roll = dice.rolldie(2, 6)
            if self.habitat_type == "Space-Dwelling":
                roll += 2
            if roll >= 11:
                special.append("Scanning Sense (Radar)")
                self.sense_roll["Scanning Sense (Radar)"] = roll

        self.sense_specials = special

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_communication_rolls(self):
        if self.sense_roll["Vision"] >= 10:
            self.sense_comm["Vision"] = dice.rolldie(1, 6)
        if self.sense_roll["Hearing"] >= 9:
            self.sense_comm["Hearing"] = dice.rolldie(1, 6)
            if self.sense_roll["Hearing"] >= 12:
                self.sense_comm["Hearing"] += 1
        if self.sense_roll["Touch"] >= 9:
            self.sense_comm["Touch"] = dice.rolldie(1, 6)
        if self.sense_roll["Taste/Smell"] >= 9:
            self.sense_comm["Taste/Smell"] = dice.rolldie(1, 6)
        if "Ultravision" in self.sense_specials:
            self.sense_comm["Ultravision"] = dice.rolldie(1, 6)
        if "Detect (Heat)" in self.sense_specials:
            self.sense_comm["Detect (Heat)"] = dice.rolldie(1, 6)
        if "Detect (Electric Fields)" in self.sense_specials:
            self.sense_comm["Detect (Electric Fields)"] = dice.rolldie(1, 6)
        if "Scanning Sense (Radar)" in self.sense_specials:
            self.sense_comm["Scanning Sense (Radar)"] = dice.rolldie(1, 6)

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_communication_a(self):
        comms_a = ""
        sense_comm = self.sense_comm
        sense_roll = self.sense_roll

        if not sense_comm:
            comms_a = "None"
        else:
            maxvalue = max(sense_comm.values())
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

        self.comms_a = comms_a

    # Alien Creation VIII: GURPS Space pg. 164
    def _gen_communication_b(self):
        comms_b = ""
        sense_comm = self.sense_comm
        sense_roll = self.sense_roll

        if not sense_comm:
            comms_b = "None"
        else:
            maxvalue = max(sense_comm.values())
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

        self.comms_b = comms_b

    # TODO: separate descriptors + advantages/disadvantages
    # Alien Creation IX: GURPS Space pg. 168
    def _gen_intelligence(self):
        intell = ""

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
        if roll <= 3:
            intell = "Mindless"
        elif roll <= 5:
            intell = "Preprogrammed (Cannot Learn)"
        elif roll <= 8:
            intell = "Low Intelligence (Bestial)"
        elif roll <= 10:
            intell = "High Intelligence (Bestial)"
        else:
            intell = "Presapient"

        if self.possible_sapient is True:
            if roll >= 13:
                intell = "Sapient"

        if self.sapient is True:
            intell = "Sapient"

        self.intelligence = intell

    def _gen_stat_iq(self):
        stat_iq = 0

        if "Mindless" in self.intelligence:
            stat_iq = 0
        elif "Preprogrammed" in self.intelligence:
            stat_iq = 1
        elif "Low" in self.intelligence:
            stat_iq = dice.rolldie(1, 3)
        elif "High" in self.intelligence:
            stat_iq = dice.rolldie(1, 3) + 2
        elif "Presapient" in self.intelligence:
            stat_iq = 5
        elif "Sapient" in self.intelligence:
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

        self.stat_iq = stat_iq

    # Alien Creation IX: GURPS Space pg. 168
    def _gen_mating(self):
        mating = ""

        roll = dice.rolldie(2, 6)
        if "Hermaphrodite" in self.sexes:
            roll -= 2
        if self.gestation == "Spawning/Pollinating":
            roll -= 1
        if self.gestation == "Live-Bearing":
            roll += 1
        if "Strong K-Strategy" in self.reproductive_strat:
            roll += 1
        elif "Strong r-Strategy" in self.reproductive_strat:
            roll -= 1

        # exception for user input, otherwise it's impossible to have
        #   already determined the social organization before mating behavior
        if (self.social_organization is not None
                and self.social_organization != "Hive"
                and roll > 10):
            roll = 10

        if roll <= 5:
            mating = "Mating only, no pair bond"
        elif roll <= 7:
            mating = "Temporary pair bond"
        elif roll == 8:
            mating = "Permanent pair bond"
        elif roll <= 10:
            mating = "Harem"
        else:
            mating = "Hive"

        self.mating = mating

    # Alien Creation IX: GURPS Space pg. 168
    def _gen_social(self):
        social = ""

        if self.mating == "Hive":
            social = "Hive"
        else:
            roll = dice.rolldie(2, 6)
            if self._is_carnivore:
                roll -= 1
            if "Grazing/Browsing Herbivore" in self.trophic_level:
                roll += 1
            if self.size_class in ("Large", "Huge"):
                roll -= 1
            if self.mating == "Harem":
                roll += 1
            if self.mating == "Mating only, no pair bond":
                roll -= 1

            if roll <= 6:
                social = "Solitary"
            elif roll <= 8:
                social = "Pair-bonded"
            elif roll <= 10:
                social = "Troop of 4 - 10 members"
            elif roll == 11:
                social = "Pack of 6 - 20 members"
            else:
                social = "Herd of 10+ members"

        self.social_organization = social

    # Alien Creation X: GURPS Space pg. 169
    def _gen_personality(self):
        if self.p_chauvinism is None:
            self._gen_p_chauvinism()
        if self.p_concentration is None:
            self._gen_p_concentration()
        if self.p_curiosity is None:
            self._gen_p_curiosity()
        if self.p_egoism is None:
            self._gen_p_egoism()
        if self.p_empathy is None:
            self._gen_p_empathy()
        if self.p_gregariousness is None:
            self._gen_p_gregariousness()
        if self.p_imagination is None:
            self._gen_p_imagination()
        if self.p_suspicion is None:
            self._gen_p_suspicion()
        if self.p_playfulness is None:
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
            if self.p_empathy > 0 > self.p_suspicion:
                t_cha = "Xenophilia (15)"
            else:
                t_cha = "Broad-minded (quirk)"
        elif self.p_chauvinism < -2:
            if self.p_empathy > 0 > self.p_suspicion:
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
            if self.p_gregariousness > 0 > self.p_suspicion:
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
    PLANET.generate()
    ALIEN = Species(PLANET)
    ALIEN.generate()
    print(ALIEN.output_text_basic())
