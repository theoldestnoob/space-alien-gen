'''
Created on Dec 15, 2018

@author: willh

'''

if __name__ == '__main__':

    from aliengen import planetinfo as planetinfo
    from aliengen import species as species
    import time

    print("space-aliens.py run! Have some dice rolls:")
    planet = planetinfo.PlanetInfo()
    planet.generate()
    spec = species.Species(planet)
    spec.generate()
    print("First planet:")
    print("")
    planet.planet_output()
    print("")
    print("First species:")
    print("")
    spec.output_text_basic()
    print("")
    print("now rolling 10,000 planets and species to check runtime errors")
    start = time.process_time()
    for i in range(1, 10000):
        planet.reroll()
        spec = species.Species(planet)
        spec.generate()

    end = time.process_time()
    elapsed = end - start
    print("That took ", end="")
    print(elapsed, end=" ")
    print("seconds!")
    print("")
    spec.output_text_basic()
'''
    print("Specific Input Tests:")
    print("")
    print("Chemical Basis!")
    for _ in range(100):
        spec.reroll()
        print("{}".format(spec.chemical_basis))
    print("")
    print("it's over!")'''
