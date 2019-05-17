'''
Created on Dec 15, 2018

@author: willh
'''

world_sizes = ["Tiny", "Small", "Standard", "Large"]

world_types = ["Asteroid Belt",
               "Ice",
               "Sulfur",
               "Rock",
               "Hadean",
               "Ammonia",
               "Ocean",
               "Garden",
               "Greenhouse",
               "Cthonian"]

world_climates = ["Frozen",
                  "Very Cold",
                  "Cold",
                  "Chilly",
                  "Cool",
                  "Normal",
                  "Warm",
                  "Tropical",
                  "Hot",
                  "Very Hot",
                  "Infernal"]

chemical_basis = ["Hydrogen-Based",
                  "Hydrogen-Based",
                  "Hydrogen-Based",
                  "Ammonia-Based",
                  "Ammonia-Based",
                  "Hydrocarbon-Based",
                  "Water-Based",
                  "Water-Based",
                  "Water-Based",
                  "Chlorine-Based",
                  "Silicon/Sulfuric Acid",
                  "Silicon/Liquid Sulfur",
                  "Silicon/Liquid Rock",
                  "Plasma",
                  "Exotica",
                  "Exotica"]

# not used in any code, defined as a reference
hab_type = ["Space-Dwelling",
            "Gas Giant",
            "Planetary Interior",
            "Water",
            "Land"]

hab_land = ["Plains",
            "Plains",
            "Plains",
            "Plains",
            "Plains",
            "Desert",
            "Island/Beach",
            "Woodlands",
            "Swampland",
            "Mountain",
            "Arctic",
            "Jungle",
            "Jungle",
            "Jungle",
            "Jungle",
            "Jungle"]

hab_water = ["Banks",
             "Banks",
             "Banks",
             "Banks",
             "Banks",
             "Open Ocean",
             "Fresh-Water Lakes",
             "River/Stream",
             "Tropical Lagoon",
             "Deep-Ocean Vents",
             "Salt-Water Sea",
             "Reef",
             "Reef",
             "Reef",
             "Reef",
             "Reef"]

troph_ordinary = ["Combined",
                  "Autotroph",
                  "Decomposer",
                  "Scavenger",
                  "Omnivore",
                  "Gathering Herbivore",
                  "Gathering Herbivore",
                  "Grazing/Browsing Herbivore",
                  "Grazing/Browsing Herbivore",
                  "Pouncing Carnivore",
                  "Chasing Carnivore",
                  "Trapping Carnivore",
                  "Hijacking Carnivore",
                  "Filter-Feeder",
                  "Parasite/Symbiont",
                  "Parasite/Symbiont"]

troph_sapient = ["Combined",
                 "Parasite/Symbiont",
                 "Filter-Feeder",
                 "Pouncing Carnivore",
                 "Scavenger",
                 "Gathering Herbivore",
                 "Gathering Herbivore",
                 "Omnivore",
                 "Chasing Carnivore",
                 "Chasing Carnivore",
                 "Grazing/Browsing Herbivore",
                 "Hijacking Carnivore",
                 "Trapping Carnivore",
                 "Trapping Carnivore",
                 "Decomposer",
                 "Autotroph"]

troph_auto = ["Photosynthetic Autotroph",
              "Photosynthetic Autotroph",
              "Photosynthetic Autotroph",
              "Chemosynthetic Autotroph",
              "Chemosynthetic Autotroph",
              "Exotic Autotroph"]

loco_primary = {
        "Arctic": ["Immobile",
                   "Slithering",
                   "Slithering",
                   "Swimming",
                   "Swimming",
                   "Digging",
                   "Walking",
                   "Walking",
                   "Winged Flight",
                   "Winged Flight",
                   "Special",
                   "Special"],

        "Banks": ["Immobile",
                  "Immobile",
                  "Floating",
                  "Sailing",
                  "Swimming",
                  "Swimming",
                  "Swimming",
                  "Winged Flight",
                  "Winged Flight",
                  "Winged Flight",
                  "Special",
                  "Special"],

        "Open Ocean": ["Immobile",
                       "Immobile",
                       "Floating",
                       "Sailing",
                       "Swimming",
                       "Swimming",
                       "Swimming",
                       "Winged Flight",
                       "Winged Flight",
                       "Winged Flight",
                       "Special",
                       "Special"],

        "Deep-Ocean Vents": ["Immobile",
                             "Immobile",
                             "Immobile",
                             "Immobile",
                             "Floating",
                             "Digging",
                             "Walking",
                             "Walking",
                             "Swimming",
                             "Swimming",
                             "Swimming",
                             "Swimming"],

        "Reef": ["Immobile",
                 "Immobile",
                 "Immobile",
                 "Immobile",
                 "Floating",
                 "Digging",
                 "Walking",
                 "Walking",
                 "Swimming",
                 "Swimming",
                 "Swimming",
                 "Swimming"],

        "Desert": ["Immobile",
                   "Slithering",
                   "Slithering",
                   "Digging",
                   "Walking",
                   "Walking",
                   "Walking",
                   "Winged Flight",
                   "Winged Flight",
                   "Winged Flight",
                   "Special",
                   "Special"],

        "Gas Giant": ["Swimming",
                      "Swimming",
                      "Swimming",
                      "Swimming",
                      "Winged Flight",
                      "Winged Flight",
                      "Winged Flight",
                      "Bouyant Flight",
                      "Bouyant Flight",
                      "Bouyant Flight",
                      "Bouyant Flight",
                      "Bouyant Flight"],

        "Island/Beach": ["Immobile",
                         "Slithering",
                         "Slithering",
                         "Digging",
                         "Walking",
                         "Walking",
                         "Climbing",
                         "Swimming",
                         "Winged Flight",
                         "Winged Flight",
                         "Special",
                         "Special"],

        "Tropical Lagoon": ["Immobile",
                            "Immobile",
                            "Immobile",
                            "Floating",
                            "Slithering",
                            "Walking",
                            "Digging",
                            "Swimming",
                            "Winged Flight",
                            "Winged Flight",
                            "Special",
                            "Special"],

        "Fresh-Water Lakes": ["Immobile",
                              "Immobile",
                              "Floating",
                              "Walking",
                              "Slithering",
                              "Swimming",
                              "Swimming",
                              "Swimming",
                              "Winged Flight",
                              "Winged Flight",
                              "Special",
                              "Special"],

        "Salt-Water Sea": ["Immobile",
                           "Immobile",
                           "Floating",
                           "Walking",
                           "Slithering",
                           "Swimming",
                           "Swimming",
                           "Swimming",
                           "Winged Flight",
                           "Winged Flight",
                           "Special",
                           "Special"],

        "Mountain": ["Immobile",
                     "Slithering",
                     "Slithering",
                     "Digging",
                     "Walking",
                     "Walking",
                     "Climbing",
                     "Winged Flight",
                     "Winged Flight",
                     "Winged Flight",
                     "Special",
                     "Special"],

        "Plains": ["Immobile",
                   "Slithering",
                   "Slithering",
                   "Digging",
                   "Walking",
                   "Walking",
                   "Walking",
                   "Winged Flight",
                   "Winged Flight",
                   "Winged Flight",
                   "Special",
                   "Special"],

        "Planetary Interior": ["Immobile",
                               "Immobile",
                               "Immobile",
                               "Immobile",
                               "Immobile",
                               "Digging",
                               "Digging",
                               "Digging",
                               "Digging",
                               "Digging",
                               "Digging",
                               "Digging"],

        "River/Stream": ["Immobile",
                         "Immobile",
                         "Floating",
                         "Slithering",
                         "Digging",
                         "Walking",
                         "Swimming",
                         "Swimming",
                         "Winged Flight",
                         "Winged Flight",
                         "Special",
                         "Special"],

        "Space-Dwelling": ["Immobile",
                           "Immobile",
                           "Immobile",
                           "Immobile",
                           "Immobile",
                           "Solar Sail",
                           "Solar Sail",
                           "Solar Sail",
                           "Solar Sail",
                           "Solar Sail",
                           "Rocket",
                           "Rocket"],

        "Swampland": ["Immobile",
                      "Swimming",
                      "Swimming",
                      "Swimming",
                      "Slithering",
                      "Digging",
                      "Walking",
                      "Climbing",
                      "Winged Flight",
                      "Winged Flight",
                      "Special",
                      "Special"],

        "Woodlands": ["Immobile",
                      "Slithering",
                      "Slithering",
                      "Digging",
                      "Walking",
                      "Walking",
                      "Climbing",
                      "Climbing",
                      "Winged Flight",
                      "Winged Flight",
                      "Special",
                      "Special"],

        "Jungle": ["Immobile",
                   "Slithering",
                   "Slithering",
                   "Digging",
                   "Walking",
                   "Walking",
                   "Climbing",
                   "Climbing",
                   "Winged Flight",
                   "Winged Flight",
                   "Special",
                   "Special"]

        }

loco_second_water = {
        "Climbing": ["Slithering",
                     "Slithering",
                     "Slithering",
                     "Slithering",
                     "Slithering",
                     "Walking",
                     "Walking",
                     "Walking",
                     "Walking",
                     "Walking",
                     ""],

        "Digging": ["Slithering",
                    "Slithering",
                    "Slithering",
                    "Slithering",
                    "Walking",
                    "Walking",
                    "Swimming",
                    "Swimming",
                    "Swimming",
                    "Swimming",
                    ""],

        "Slithering": ["Swimming",
                       "Swimming",
                       "Swimming",
                       "Swimming",
                       "Swimming",
                       "Swimming",
                       "Swimming",
                       "Swimming",
                       "Swimming",
                       "",
                       ""],

        "Swimming": ["Slithering",
                     "Slithering",
                     "Slithering",
                     "Slithering",
                     "Slithering",
                     "Walking",
                     "Walking",
                     "Walking",
                     "",
                     "",
                     ""],

        "Walking": ["Swimming",
                    "Swimming",
                    "Swimming",
                    "Swimming",
                    "Swimming",
                    "Swimming",
                    "Swimming",
                    "",
                    "",
                    "",
                    ""],

        "Winged Flight": ["Climbing",
                          "Climbing",
                          "Climbing",
                          "Climbing",
                          "Swimming",
                          "Swimming",
                          "Walking",
                          "Walking",
                          "Walking",
                          "Slithering",
                          ""]

        }

loco_second_land = {
        "Climbing": ["Slithering",
                     "Slithering",
                     "Slithering",
                     "Slithering",
                     "Slithering",
                     "Walking",
                     "Walking",
                     "Walking",
                     "Walking",
                     "Walking",
                     ""],

        "Digging": ["Slithering",
                    "Slithering",
                    "Slithering",
                    "Slithering",
                    "Slithering",
                    "Walking",
                    "Walking",
                    "Walking",
                    "Walking",
                    "Walking",
                    ""],

        "Swimming": ["Slithering",
                     "Slithering",
                     "Slithering",
                     "Slithering",
                     "Slithering",
                     "Walking",
                     "Walking",
                     "Walking",
                     "",
                     "",
                     ""],

        "Walking": ["Slithering",
                    "Slithering",
                    "Digging",
                    "Walking",
                    "Walking",
                    "Climbing",
                    "Winged Flight",
                    "Winged Flight",
                    "Winged Flight",
                    "Special",
                    "Special"],

        "Winged Flight": ["Climbing",
                          "Climbing",
                          "Climbing",
                          "Climbing",
                          "Swimming",
                          "Swimming",
                          "Walking",
                          "Walking",
                          "Walking",
                          "Slithering",
                          ""]

        }

loco_primary_extra = {

        "Arctic": ["Swimming", "Digging"],
        "Banks": ["Winged Flight"],
        "Open Ocean": ["Winged Flight"],
        "Deep-Ocean Vents": ["Digging", "Walking"],
        "Reef": ["Digging", "Walking"],
        "Desert": ["Digging", "Winged Flight"],
        "Gas Giant": [],
        "Island/Beach": ["Digging", "Climbing", "Swimming", "Winged Flight"],
        "Tropical Lagoon": ["Slithering", "Walking", "Digging"],
        "Fresh-Water Lakes": ["Walking", "Slithering"],
        "Salt-Water Sea": ["Walking", "Slithering"],
        "Mountain": ["Digging", "Walking", "Climbing", "Winged Flight"],
        "Plains": ["Digging", "Winged Flight"],
        "Planetary Interior": [],
        "River/Stream": ["Slithering", "Digging", "Walking"],
        "Space-Dwelling": [],
        "Swampland": ["Swimming", "Digging", "Climbing"],
        "Woodlands": ["Digging", "Climbing", "Winged Flight"],
        "Jungle": ["Digging", "Climbing", "Winged Flight"]

        }

loco_second_extra = {

        "Climbing": [],
        "Digging": ["Slithering", "Walking"],
        "Slithering": [],
        "Swimming": [],
        "Walking": [],
        "Winged Flight": ["Climbing", "Swimming", "Slithering"]

        }

size_volume_small = [0.05, 0.07, 0.1, 0.15, 0.2, 0.3]
size_volume_human = [0.5, 0.7, 1, 1.5, 2, 3]
size_volume_large = [5, 7, 10, 15, 20, 99999]

size_mass_small = [0.003, 0.01, 0.025, 0.08, 0.2, 1]
size_mass_human = [4, 9, 25, 80, 200, 600]
size_mass_large = [3000, 8000, 24000, 80000, 200000, 99999]

body_symmetry = ["Bilateral",
                 "Bilateral",
                 "Bilateral",
                 "Bilateral",
                 "Bilateral",
                 "Bilateral",
                 "Trilateral",
                 "Radial",
                 "Spherical",
                 "Asymmetric",
                 "Asymmetric",
                 "Asymmetric",
                 "Asymmetric"]

body_tail_features = ["",
                      "",
                      "",
                      "",
                      "Striker",
                      "Long",
                      "Constricting",
                      "Barbed Striker",
                      "Gripping",
                      "Branching",
                      "Combination"]

body_skeleton = ["No skeleton",
                 "No skeleton",
                 "Hydrostatic skeleton",
                 "Hydrostatic skeleton",
                 "External skeleton",
                 "External skeleton",
                 "Internal skeleton",
                 "Internal skeleton",
                 "Internal skeleton",
                 "Combination",
                 "Combination",
                 "Combination",
                 "Combination",
                 "Combination",
                 "Combination"]

skin_covertype = ["Skin",
                  "Skin",
                  "Scales",
                  "Fur",
                  "Feathers",
                  "Exoskeleton"]

skin_skin = ["Soft Skin",
             "Soft Skin",
             "Soft Skin",
             "Normal Skin",
             "Hide (DR 1)",
             "Hide (DR 1)",
             "Thick Hide (DR 4)",
             "Armor Shell (DR 5)",
             "Blubber",
             "Blubber",
             "Blubber",
             "Blubber",
             "Blubber",
             "Blubber"]

skin_scales = ["Normal Skin",
               "Normal Skin",
               "Scales (DR 1)",
               "Scales (DR 1)",
               "Scales (DR 1)",
               "Scales (DR 1)",
               "Scales (DR 1)",
               "Heavy Scales (DR 3)",
               "Heavy Scales (DR 3)",
               "Armor Shell (DR 5)",
               "Armor Shell (DR 5)",
               "Armor Shell (DR 5)",
               "Armor Shell (DR 5)"]

skin_fur = ["Normal Skin",
            "Normal Skin",
            "Normal Skin",
            "Normal Skin",
            "Fur",
            "Fur",
            "Thick Fur (+1 Temperature Tolerance)",
            "Thick Fur (+1 Temperature Tolerance)",
            "Thick Fur over Hide (DR 1, +1 Temperature Tolerance)",
            "Thick Fur over Hide (DR 1, +1 Temperature Tolerance)",
            "Spines",
            "Spines",
            "Spines"]

skin_feathers = ["Normal Skin",
                 "Normal Skin",
                 "Normal Skin",
                 "Normal Skin",
                 "Feathers (+1 Temperature Tolerance)",
                 "Feathers (+1 Temperature Tolerance)",
                 "Feathers (+1 Temperature Tolerance)",
                 "Thick Feathers (+2 Temperature Tolerance)",
                 "Thick Feathers (+2 Temperature Tolerance)",
                 "Feathers over Hide (DR 1, +1 Temperature Tolerance)",
                 "Spines",
                 "Spines",
                 "Spines"]

skin_exoskeleton = ["Light Exoskeleton (DR 0)",
                    "Light Exoskeleton (DR 0)",
                    "Tough Exoskeleton (DR 1)",
                    "Tough Exoskeleton (DR 1)",
                    "Heavy Exoskeleton (DR 2)",
                    "Armor Shell (DR 5)",
                    "Armor Shell (DR 5)",
                    "Armor Shell (DR 5)"]

