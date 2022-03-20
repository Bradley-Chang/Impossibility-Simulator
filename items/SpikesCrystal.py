from items.item import Item
class CrystalSpikes(Item):
    def __init__(self):
        Item.__init__(self, "Crystal Spikes", 3, "ally")

    def use(self, team, index, extra=None):
        if team.field[index].lastAttacked == None:
            return
        damage = team.field[index].lastAttacked.takeDamage(4, True)
        msg = team.field[index].lastAttacked.name + " took " + damage + " damage from the crystal spikes!"
        return msg