from items.item import Item
class StoneSpikes(Item):
    def __init__(self):
        Item.__init__(self, "Stone Spikes", 2, "ally")

    def use(self, team, index, extra=None):
        if team.field[index].lastAttacked == None:
            return
        damage = team.field[index].lastAttacked.takeDamage(5, False)
        msg = team.field[index].lastAttacked.name + " took " + damage + " damage from the stone spikes!"
        return msg