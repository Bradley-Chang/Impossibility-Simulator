from creatures.creature import Creature

class TheMaster(Creature):
    def __init__(self):
        Creature.__init__(self, "The Master", 5, 16, 4, 10, 7, "None", ["earth","light"], "No Ability.", "Sensei/Powerhouse", (150, 59, 48, 255), (205, 203, 51, 255))
