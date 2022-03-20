from items.item import Item
class IronSpikes(Item):
    def __init__(self):
        Item.__init__(self, "Iron Spikes", 3, "ally")

    def use(self, team, index, extra=None):
        if team.field[index].lastAttacked == None:
            return
        damage = team.field[index].lastAttacked.takeDamage(7, False)
        msg = team.field[index].lastAttacked.name + " took " + damage + " damage from the iron spikes!"
        return msg