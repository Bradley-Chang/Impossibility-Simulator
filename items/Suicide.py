from items.item import Item


class Suicide(Item):
    def __init__(self):
        Item.__init__(self, "Suicide", 2, "ally")

    def use(self, team, index, extra=None):
        if team.field[index].currentHp / team.field[index].baseHp > 0.25:
            return
        else:
            team.field[index].currentHp = 0
            return team.field[index].name + " was slain..."