from creatures.creature import Creature
# A basic creature. Starts with 50% HP.
class WoundedTester(Creature):
    def __init__(self):
        Creature.__init__(self, "Wounded Fasty McTenSpeed", 3, 10, 5, 5, 10, "None", "Light", 1)
        self.currentHp = 5
