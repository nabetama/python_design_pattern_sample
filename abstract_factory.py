# coding: utf-8

class Duck():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print "アヒル: %sは食事中です" % self.name

class Frog():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print 'カエル: %sは食事中です' % self.name

class Algae():
    def __init__(self, name):
        self.name = name

    def grow(self):
        print "藻: %sは成長中です" % self.name

class WaterLily():
    def __init__(self, name):
        self.name = name

    def grow(self):
        print "睡蓮: %sは成長中です" % self.name

class FrogAndAlgaeFactory():
    """カエルと藻の育成のみを行う"""
    def new_animal(self, name):
        return Frog(name)

    def new_plant(self, name):
        return Algae(name)

class DuckAndWaterLilyFactory():
    """アヒルと植物の育成のみを行う"""
    def new_animal(self, name):
        return Duck(name)

    def new_plant(self, name):
        return WaterLily(name)

class Pond():
    def __init__(self, number_animals, number_plants, organism_factory):
        self.animals = []
        for i in range(1, number_animals+1):
            param = "動物 " + str(i)
            self.animal = organism_factory.new_animal(param)
            self.animals.append(self.animal)

        self.plants = []
        for i in range(1, number_plants+1):
            param = "植物 " + str(i)
            self.plant = organism_factory.new_plant(param)
            self.plants.append(self.plant)
        pass

    def simulate_now(self):
        [animal.eat() for animal in self.animals]
        [plant.grow() for plant in self.plants]

pond = Pond(1, 4, FrogAndAlgaeFactory())
pond.simulate_now()

pond = Pond(2, 3, DuckAndWaterLilyFactory())
pond.simulate_now()
