from items.item import Item
class WoodSpikes(Item):
    def __init__(self):
        Item.__init__(self, "Wooden Spikes", 1, "ally")

    def use(self, team, index, extra=None):
        if team.field[index].lastAttacked == None:
            return
        damage = team.field[index].lastAttacked.takeDamage(4, False)
        msg = team.field[index].lastAttacked.name + " took " + damage + " damage from the wood spikes!"
        return msg