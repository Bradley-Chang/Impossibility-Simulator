from items.item import Item


class CandyCorn(Item):

    def __init__(self):
        Item.__init__(self, "Candy Corn", 1, "ally")

    def use(self, team, index, extra=None):
        team.field[index].heal(1)
        team.field[index].takeStatus("candyCorn", 999)
        msg = team.field[index].name + " ate the candy corn, healed 1 HP, and gained 1 SPD."
        return msg