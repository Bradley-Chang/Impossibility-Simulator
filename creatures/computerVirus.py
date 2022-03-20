from creatures.creature import Creature
import random

# stats are formatted in Slime/Puppet/Witch form
# CURRENT STATE: UNFINISHED
# HP: 4/6/6
# Def: 2/2/4
# Atk: 4/5/6
# Spd: 5/5/5
# Stars: 3
# Ability (Slime): Attacks inflict poison and deal 2 self damage.
# Poison - 1 damage per turn, default lasts 5 turns
# Ability (Puppet): You have the option to pay 3 points, or have a 1/3 chance to do 6 piercing damage.
# Ability (Witch): You have the option to heal 4 hp, or inflict burn or frostbite on anyone.
# Frostbite - 25% reduced speed, 2 damage per turn, default lasts 2 turns, ice immune
# Burning - 3 damage per turn, default lasts 2 turns, fire immune

class ComputerVirus(Creature):
    def __init__(self):
        super().__init__("Slime", 3, 4, 2, 4, 5, "OnAtk", ["machine"], "Attacks give poison and inflict 2 self damage.","Error", (2, 34, 94, 255), (191, 191, 191, 255))

    def takeDamage(self, attacker, isPiercing):
        msg = super().takeDamage(attacker,isPiercing)
        if self.currentHp <= 0 and self.name == "Slime":
            self.name = "Puppet"
            self.baseHp = 6
            self.currentHp = 6
            self.baseDef = 2
            self.baseAtk = 5
            self.baseSpd = 5
            self.ability = "Pay"
            self.description = "Has a 1/3 chance or pay 3 stars to do 6 piercing damage to both the puppet and target."
            self.primary = (16, 114, 189, 255)
            self.abilityPrompt = (
                    "You can pay 3 points to guarantee that the puppet will do 6 piercing damage to itself and an enemy "
                    + "on the next attack. Type 1 to pay the cost or 2 to not pay it.")
            self.abilityCost = 3
            self.calculateStatusChanges()
            msg += "\nSlime was defeated! Puppet appears!"
        if self.currentHp <= 0 and self.name == "Puppet":
            self.name = "Witch"
            self.baseHp = 6
            self.currentHp = 6
            self.baseDef = 4
            self.baseAtk = 6
            self.baseSpd = 5
            self.calculateStatusChanges()
            self.primary = (30, 177, 237, 255)
            self.ability = "OnAtkAny"
            self.description = "Attacks can give either frostbite, burning, or healing to any creature."
            self.abilityPrompt = (
                        "You can choose inflict burn, frostbite, or heal a target. Type \"burn\", \"frostbite\","
                        + "or \"heal\" then a target. (e.g. burn 1)")
            self.abilityCost = 0
            msg += "\nPuppet was defeated! Witch appears!"
        return msg
    # extra for puppet is either True or False. If True, then attack is piercing.
    # extra for witch is either "burn" or "frost", which gives those to the target, or "heal", which heals target 4 HP.

    def attack(self, team, index, extra, isPiercing):
        # The Slime does 2 self damage when hitting someone and inflicts them with poison.
        if self.name == "Slime":
            msg = super().attack(team, index, extra, False)
            team.field[index].takeStatus("poison", 5)
            msg += "Slime took " + str(self.takeDamage(2, True)) + " self damage!\n" + team.field[index].name + " was poisoned!\n"
        # The Puppet has a 1/3 chance of doing 6 piercing damage but also hitting itself.
        elif self.name == "Puppet":
            pierce = random.randint(1, 3)
            if pierce > 2 or "cvPuppet" in self.status:
                temp = self.currentAtk
                self.currentAtk = 6
                msg = super().attack(team, index, extra, True)
                self.currentAtk = temp
                msg += "Puppet took 6 self damage!"
                msg += self.takeDamage(6, True)
            else:
                msg = super().attack(team, index, extra, False)
        # The Witch can choose to burn, frostbite, or heal creatures.
        elif self.name == "Witch":
            if extra == "heal":
                heal = 4
                team.field[index].heal(heal)
                msg = team.field[index].name + " was healed " + str(heal) + " HP."
                return msg
            msg = super().attack(team, index, extra, False) + "\n"
            if extra == "burn":
                if team.field[index].element != "fire":
                    msg += "But " + team.field[index].name + "was immune to be burning!"
                else:
                    team.field[index].takeStatus("burn", 2)
            if extra == "frostbite":
                if team.field[index].element != "ice":
                    msg += "But " + team.field[index].name + "was immune to be frostbite!"
                else:
                    team.field[index].takeStatus("frostbite", 2)
        return msg
    # If creature is Puppet, check that the response is "1" or "2".
    # If creature is Witch, check that the response message contains "burn, frostbite, heal", then a number.
    # msg is the CONTENT of the msg (msg.content in the bot.py file).
    def abilityCheck(self, msg):
        if self.name == "Puppet":
            if msg == "1" or msg == "2":
                return True
            else:
                return False
        if self.name == "Witch":
            splitMsg = msg.split()
            # check if the first word is "burn", "frostbite", or "heal"
            if splitMsg[0].lower() in "burn" or splitMsg[0].lower() in "frostbite" or splitMsg[0].lower() in "heal" and \
                    splitMsg[1].isnumeric():
                # check if the second word is an int.
                    return True
            return False
    # after confirming the player entered in "burn", "frostbite", or "heal", this sets the extra segment of the attack.
    # example: burn 1

    def setExtra(self, extraMsg):
        extra = extraMsg.split()[0]
        return extra
    # Adds the piercing damage if accepted. Returns True if the user paid for the message.
    def payAbility(self, msg):
        if msg == "1":
            self.takeStatus("cvPuppet", 1)
            return True
        if msg == "2":
            return False

