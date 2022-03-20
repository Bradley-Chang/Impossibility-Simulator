from items.item import Item
class Grapes(Item):
    def __init__(self):
        Item.__init__(self, "Grapes", 2, "ally")

    def use(self, team, index, extra=None):
        team.field[index].heal(4)
        msg = team.field[index].name + " ate the grapes and healed 4 HP."
        return msg