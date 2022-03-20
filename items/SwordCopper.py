from items.item import Item
class SwordCopper(Item):
    def __init__(self):
        Item.__init__(self, "Copper Sword", 3, "ally", "equipped")

    def use(self, team, index, extra=None):
        team.field[index].takeStatus("copperSword", 999)
        msg = team.field[index].name + " equipped the copper sword!"
        return msg