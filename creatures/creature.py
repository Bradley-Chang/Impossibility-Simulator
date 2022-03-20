import math
from status import statusAddAtk, statusAddDef, statusAddSpd, statusMultAtk, statusMultDef, statusMultSpd, statusDoT, iceImmunities, fireImmunities, machineImmunities, undeadImmunities
from items import item
from team import Team

class Creature(object):
    # name: name
    # baseHp: health
    # baseAtk: damage per attack
    # baseDef: reduces damage from attack by (def / 2)
    # baseSpd: order of turns are based on pairs of creatures, the pair with highest speed goes first. If 2 with
    #          have identical speed, then the one with higher health percentage remaining goes first. If they have
    #          the same health, the creature of the opposite team that took its turn previously goes first
    # ability: The type of ability:
    #   "None": No ability
    #   "OnAtk": A passive ability that triggers on attack.
    #   "OnAtkAny": Prompts for a target after attacking. Anyone can be targeted.
    #   "Pay": Prompts for the user to pay a price in points to alter the creature.
    # element: a List which can contain earth, air, fire, water, light, dark, undead, machine
    # title:
    # turns: number of times the creature can attack.
    # remainingTurns: remaining times the creature can attack in a turn.
    # status: a dictionary, key is ID of status effects, value is the turns remaining
    # team: the team the creature is on.
    # enemyTeam: the enemy team
    # lastAttacked: The last one who attacked this creature.
    # description: The description of the ability.
    # flavor: the flavor text at the bottom.
    # primary: Color of the creature's stat bars
    # secondary: Color of the creature's star bar's negative space.
    # team: team the creature is in

    def __init__(self, name, stars, hp, defs, atk, spd, ability, element, description, flavor, primary, secondary):
        self.name = name
        self.stars = stars
        self.baseHp = hp
        self.baseAtk = atk
        self.baseDef = defs
        self.baseSpd = spd
        self.currentHp = hp
        self.currentAtk = atk
        self.currentDef = defs
        self.currentSpd = spd
        self.ability = ability
        self.element = element
        self.turns = 1
        self.remainingTurns = 1
        self.status = {}
        self.team = None
        self.enemyTeam = None
        self.lastAttacked = None
        self.abilityPrompt = ""
        self.description = description
        self.flavor = flavor
        self.primary = (255, 255, 255, 255)
        self.secondary = (0, 0, 0, 0)
        self.abilityCost = 0
        self.equipped = []

    # atk is the attack of the creature who attacks or the damage of the item.
    # isPiercing determines if the attack pierces.
    def takeDamage(self, attacker, isPiercing):
        if isinstance(attacker, int):
            if isPiercing:
                damage = attacker
            else:
                damage = ((attacker) - (self.currentDef / 2))
            if damage < 0:
                damage = 0
            self.currentHp -= damage
            if self.currentHp < 0:
                self.currentHp = 0
            return str(damage)
        elif isinstance(attacker, Creature):
            if isPiercing:
                damage = attacker.currentAtk
            else:
                damage = ((attacker.currentAtk) - (self.currentDef / 2))
            if damage < 0:
                damage = 0
            self.currentHp -= damage
            if self.currentHp < 0:
                self.currentHp = 0
            msg = attacker.name + " attacks " + self.name + "!\n" + self.name + " took " + str(
                damage) + " damage!\n"
            if self.currentHp == 0:
                msg += self.name + " has been defeated!\n"
            return msg
    # amount is the amount of damage, this is typically used with items

    # team is a Team object.
    # lane is the lane that the creature attacks on. Lane 0 is the far left, lane 1 is right of that, etc.
    # extra dictates extra info about attacks. For example, some creatures can choose what status they inflict.
    # isPiercing dictates if the attack is piercing or not.
    # The first creature in a lane is attacked. Protective minions are placed in the front of a lane.
    def attack(self, team, lane, extra, isPiercing):
        team.lanes[lane][0].lastAttacked = self
        numAttacks = (self.currentSpd / math.floor(team.field[lane][0].currentSpd))
        if numAttacks < 1:
            numAttacks = 1
        msg = ""
        # creatures can attack other creatures multiple times based on how much speed they have over the defender.
        for i in range(int(numAttacks)):
            msg = team.lanes[lane][0].takeDamage(self, isPiercing)
            if i > 0:
                self.currentAtk /= 2
                msg += team.lanes[lane][0].takeDamage(self, isPiercing)
                self.currentAtk *= 2
        return msg


    # handles healing, which is not affected by defense.
    def heal(self, heal):
        self.currentHp += heal
        if self.currentHp > self.baseHp:
            self.currentHp = self.baseHp

    # Some creatures do stuff on being swapped in.
    def onSwitchIn(self):
        pass

    # Some creatures do stuff when their teammates are hurt.
    def onTeamHurt(self, teammate):
        pass

    # Some creatures can only do stuff once per turn, etc.
    # Some effects affect all creatures, like Beacon Of Rage item which buffs everyone.
    def onTurnStart(self):
        self.remainingTurns = self.turns
        if "rageBeacon" in self.status:
            for i in self.team.field:
                i.takeStatus("rage", 1)

    # Some creatures do stuff on death.
    def onDeath(self):
        if "rageBeacon" in self.status:
            for i in self.team.field:
                i.status.pop("rageBeacon")
        self.enemyTeam.extraPoints += self.stars

    def toString(self):
        msg = ("**__" + self.name +  "__**" + "\n**Stars:** " + str(self.stars) +
        "\n**Attack:** " + str(self.baseAtk) + "\n**Defense:** " + self.baseDef + "\n**Speed:** " + str(self.baseSpd))
        return msg
    # calculate stat changes and get a status effect
    # effect: name of status
    # duration: length of status (in turns)
    def takeStatus(self, effect, duration):
        status = {effect: duration}
        if "machine" in self.element and effect in machineImmunities:
            return
        if "fire" in self.element and effect in fireImmunities:
            return
        if "ice" in self.element and effect in iceImmunities:
            return
        if "undead" in self.element and effect in undeadImmunities:
            return
        self.status.update(status)
        atkMult = 1
        atkAdd = 0
        defMult = 1
        defAdd = 0
        spdMult = 1
        spdAdd = 0
        for i in self.status:
            try:
                atkMult *= statusMultAtk[i]
            except KeyError:
                pass
            try:
                defMult *= statusMultDef[i]
            except KeyError:
                pass
            try:
                spdMult *= statusMultSpd[i]
            except KeyError:
                pass
            try:
                atkAdd += statusAddAtk[i]
            except KeyError:
                pass
            try:
                defAdd += statusAddDef[i]
            except KeyError:
                pass
            try:
                spdAdd += statusAddSpd[i]
            except KeyError:
                pass
        self.currentAtk = (self.baseAtk * atkMult) + atkAdd
        self.currentDef = (self.baseDef * defMult) + defAdd
        self.currentSpd = (self.baseSpd * spdMult) + spdAdd

    # calculate stat changes without a status effect.
    def calculateStatusChanges(self):
        atkMult = 1
        atkAdd = 0
        defMult = 1
        defAdd = 0
        spdMult = 1
        spdAdd = 0
        for i in self.status:
            atkMult *= statusMultAtk[i]
            defMult *= statusMultDef[i]
            spdMult *= statusMultSpd[i]
            atkAdd += statusAddAtk[i]
            defAdd += statusAddDef[i]
            spdAdd += statusAddSpd[i]
        self.currentAtk = (self.baseAtk * atkMult) + atkAdd
        self.currentDef = (self.baseDef * defMult) + defAdd
        self.currentSpd = (self.baseSpd * spdMult) + spdAdd



    def pluralise(s):
        if str.isupper(s[-1]):
            return s + "s"
        elif re.search("((c|s)h|s|x|z)$", s):
            return s + "es"
        elif re.search("[^aeiou]y$", s):
            return s[:-1] + "ies"
        elif re.search("^(.*)[^f]fe?$", s):
            if s[-1] == "e":
                return s[:-2] + "ves"
            else:
                return s[:-1] + "ves"
        else:
            return s + "s"
