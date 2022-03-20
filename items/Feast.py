from items.item import Item
class Feast(Item):
    def __init__(self):
        Item.__init__(self, "Feast", 3, "ally")

    def use(self, team, index, extra=None):
        team.field[index].heal(9)
        team.field[index].takeStatus("feast", 999)
        team.field[index].takeStatus("wellFed", 3)
        msg = team.field[index].name + " ate the feast, healed 9 HP, gained Well-Fed, and lost 1 SPD."
        return msg