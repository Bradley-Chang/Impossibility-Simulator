from items.item import Item
class Shortcake(Item):
    def __init__(self):
        Item.__init__(self, "Shortcake", 2, "ally")

    def use(self, team, index, extra=None):
        team.field[index].heal(2.5)
        msg = team.field[index].name + " ate the shortcake, healed 4 HP, and gained 25% SPD."
        return msg