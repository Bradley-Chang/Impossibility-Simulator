
# status IDs:
# Tier 1 Debuffs
#  chill: Chill - 25% reduced speed, default lasts 2 turns, ice immune
#  confuse: Confusion - Afflicted attacks a random creature
#  poison: Poison - 1 damage per turn, default lasts 5 turns
#  blind: Blindness - Afflicted attacks random enemy
#  sick: Sickness - -1 DEF, ATK, and SPD, default lasts 3 turns, machine immune
#  burn: Burning - 3 damage per turn, default lasts 2 turns, fire immune
#  smolder: Smoldering - 2 damage per turn, default lasts 2 turns, fire immune
#  frostbite: Frostbite - 25% reduced speed, 2 damage per turn, default lasts 2 turns, ice immune
# Tier 2 Debuffs
#  frozen: Frozen - Cannot attack, or switch, default lasts 1 turn
#  blaze: Blazing - 4 damage, default lasts 2 turns, fire immune
#  paralyze: Paralyzed - Halved speed, default lasts 2 turns, electric immune
#  venom: Venom - 2 damage per turn, default lasts 5 turns, machine immune
#  plague: Plague - -2 DEF -1 ATK, -2 SPD, default lasts 3 turns, machine and undead immune
# Tier 3 Debuffs
#  curse: Curse - -3 stars in item usage
#  timeFreeze: Frozen in Time - affected can't do anything
#  override: Overridden - N/A
#  cursedInferno: Cursed Inferno - 3 damage per turn, forever.
#  condemned: Condemned - Afflicted dies upon expiration
#  corruption: Corruption - Afflicted takes damage for using ability.
#  imprison: Imprison
# Buffs
#  wellFed: Well-Fed +1 HP, default lasts 3 turns, machine immune
#  regen: Regen +2 HP, default lasts 3 turns
#  rapidRegen: Rapid Regen +3 HP, default lasts 3 turns
#  hyper: Hyper +25% SPD
# Character Specific
#  cvPuppet: Puppet does 6 piercing damage to itself and the target if it has this.
#  wbRock: Wham Bam Rock +1 DEF
#  wbJewel: Wham Bam Jewel +2 DEF
#  mmFire: Fire Mode (Miracle Matter) +2 ATK, +2 SPD
#  mmRock: Rock Mode (Miracle Matter) +3 DEF, Heal 2 HP
#  mmWater: Water Mode (Miracle Matter) +1 ATK, +1 DEF, +1 SPD, heal 1 HP
#  mmIce: Ice Mode (Miracle Matter) +1 ATK, +1 DEF, +1 SPD, heal 1 HP
#  lcBarricade: Barricade (Lord Crump) +1 ATK, +2 DEF, teammates gain +2 DEF
#  lcAcrobat: Acrobat (Lord Crump) 2 attacks per turn, attacks ignore minions
#  lcXball: X-Ball (Lord Crump) +3 ATK, immune to slower opponents.
#  mdSpinning: Spinning Doom (Masked Dedede) -2 ATK, can hit 2 targets.
#  mdBarrage: Barrage (Masked Dedede) -4 ATK, can hit 4 times per turn
#  mdFlamethrower: Flamethrower (Masked Dedede) Attacks inflict Blaze
# Items
#  candyCorn: +1 SPD
#  copperSword: +0.5 ATK
#  corruptedRing: Attack inflicts corruption.
#  dumplingBuff: +1 DEF, +1 SPD
#  dumplingDebuff: -1 SPD
#  feast: -1 SPD
#  gasFire: +2 ATK
#  gasMachine: +2 SPD
#  gasOther: Being attacked by a fire creature inflicts Burning.
#  hydrantBuff: +1 ATK +1 SPD
#  hydrantDebuff: -50% ATK -33% SPD
#  ironSword: +1 ATK
#  mechanicalShield: +4 DEF -1 SPD
#  mirrorCopy: Amazing Mirror creatures always have this: -1 DEF, -1 ATK, -1 SPD, 50% max HP.
#  pizza: Gained by eating Pizza. -1 SPD
#  planAhead: Afflicted is immune to damage when duration is at 1.
#  rageBeacon: Gives rage effect to everyone on the team.
#  rage: +2 ATK, +25% SPD
#  shortcake: +25% SPD
#  shrunken: Gained from the Shrink Ring. ATK and DEF -33%, SPD +33%
#  swordsOfRage: +1 ATK per 25% hp missing. When the holder is killed, the killer loses 25% HP.
#  titaniumSword: +2 ATK, -1 SPD
# Other
#  defend: Defending - Defense doubled for 1 turn


# Immunities
machineImmunities = ["poison", "sickness", "venom", "plague", "wellFed"]
fireImmunities = ["burn", "smoulder", "blaze"]
iceImmunities = ["frostbite", "frozen", "chill"]
undeadImmunities = ["plague", "sickness"]

# Additive stat changes when affected by status effects
statusAddAtk = {
                "sick": -1,
                "plague": -1,
                "mmFire": 2,
                "mmWater": 1,
                "mmIce": 1,
                "lcBarricade": 1,
                "lcXball": 3,
                "mdSpinning": -2,
                "mdBarrage": -4,
                "copperSword": 0.5,
                "gasFire": 2,
                "ironSword": 1,
                "mirrorCopy": -1,
                "rage": 2,
                "titaniumSword": 2,
                }
statusAddDef = {
                "sick": -1,
                "plague": -2,
                "mmRock": 3,
                "mmWater": 1,
                "mmIce": 1,
                "lcBarricade": 2,
                "dumplingBuff": 1,
                "mechanicalShield": 4,
                "mirrorCopy": -1,
                }
statusAddSpd = {"sick": -1,
                "plague": -2,
                "mmFire": 2,
                "mmWater": 1,
                "mmIce": 1,
                "lcBarricade": 2,
                "candyCorn": 1,
                "dumplingBuff": 1,
                "dumplingDebuff": -1,
                "feast": -1,
                "gasMachine": 2,
                "hydrantBuff": 1,
                "mechanicalShield": -1,
                "mirrorCopy": -1,
                "pizza": -1,
                "titaniumSword": -1,
                }
# Multiplicative stat changes when affected by status effects
statusMultAtk = {"hydrantDebuff": 0.5,
                 "shrunken": 0.66,
                }
statusMultDef = {
                 "shrunken": 0.66,
                 "defend": 2
                }
statusMultSpd = {"chill": 0.75,
                 "frostbite": 0.75,
                 "paralyze": 0.5,
                 "hyper": 1.25,
                 "hydrantDebuff": 0.5,
                 "rage": 1.25,
                 "shortcake": 1.25,
                 "shrunken": 1.33,
                }
# Damage per turn of status effects, negative values denote healing.
statusDoT = {"chill": 0,
             "confuse": 0,
             "poison": 1,
             "blind": 0,
             "sick": 0,
             "burn": 3,
             "smolder": 2,
             "frostbite": 2,
             "frozen": 0,
             "blaze": 4,
             "paralyze": 0,
             "venom": 2,
             "plague": 0,
             "curse": 0,
             "timeFreeze": 0,
             "cursedInferno": 3,
             "condemned": 0,
             "corruption:": 0,
             "imprison": 0,
             "wellFed": -1,
             "regen": -2,
             "rapidRegen": -3,
             "hyper": 0,
             "cvPuppet": 0,
             "wbRock": 0,
             "wbJewel": 0,
             "mmFire": 0,
             "mmRock": -2,
             "mmWater": -1,
             "mmIce": -1,
             "lcBarricade": 0,
             "lcAcrobat": 0,
             "lcXball": 0,
             "mdSpinning": 0,
             "mdBarrage": 0,
             "mdFlamethrower": 0,
             "candyCorn": 0,
             "copperSword": 0,
             "corruptedRing": 0,
             "dumplingBuff": 0,
             "dumplingDebuff": 0,
             "feast": 0,
             "gasFire": 0,
             "gasMachine": 0,
             "gasOther": 0,
             "hydrantBuff": 0,
             "hydrantDebuff": 0,
             "ironSword": 0,
             "mechanicalShield": 0,
             "mirrorCopy": 0,
             "pizza": 0,
             "planAhead": 0,
             "rageBeacon": 0,
             "rage": 0,
             "shrunken": 0,
             "swordsOfRage": 0,
             "titaniumSword": 0,
             "defend": 0
                }

statusNames = {
             "chill": "Chilled",
             "confuse": "Confused",
             "poison": "Poisoned",
             "blind": "Blinded",
             "sick": "Sick",
             "burn": "Burned",
             "smolder": "Smouldering",
             "frostbite": "Frostbite",
             "frozen": "Frozen",
             "blaze": "Blazing",
             "paralyze": "Paralyzed",
             "venom": "Venom",
             "plague": "Plague",
             "curse": "Cursed",
             "timeFreeze": "Frozen In Time",
             "cursedInferno": "Cursed Inferno",
             "condemned": "Condemned",
             "corruption:": "Corrupted",
             "imprison": "Imprisoned",
             "wellFed": "Well Fed",
             "regen": "Regen",
             "rapidRegen": "Rapid Regen",
             "hyper": "Hyper",
             "cvPuppet": "Dancing Doll Piercing",
             "wbRock": "Wham Bam Rock",
             "wbJewel": "Wham Bam Jewel",
             "mmFire": "Fire Mode",
             "mmRock": "Rock Mode",
             "mmWater": "Water Mode",
             "mmIce": "Ice Mode",
             "lcBarricade": "Barricade Formation",
             "lcAcrobat": "Acrobat Formation",
             "lcXball": "X Ball Formation",
             "mdSpinning": "Spinning Doom",
             "mdBarrage": "Barrage",
             "mdFlamethrower": "Flamethrower",
             "candyCorn": "Candy Corn Speed",
             "copperSword": "Copper Sword Equipped",
             "corruptedRing": "Corrupted Ring",
             "dumplingBuff": "Dumpling (Panda)",
             "dumplingDebuff": "Dumpling (Non Panda)",
             "feast": "Feast",
             "gasFire": "Gas Powered (Fire)",
             "gasMachine": "Gas Powered (Machine)",
             "gasOther": "Gas Covered",
             "hydrantBuff": "Wet",
             "hydrantDebuff": "Extinguished",
             "ironSword": "Iron Sword",
             "mechanicalShield": "Mechanical Shield",
             "mirrorCopy": "Mirror Copy",
             "pizza": "Pizza Slowness",
             "planAhead": "Plan Ahead",
             "rageBeacon": "Beacon Of Rage",
             "rage": "Enraged",
             "shortcake": "Shortcake Speed",
             "shrunken": "Shrunken",
             "swordsOfRage": "Swords Of Rage",
             "titaniumSword": "Titanium Sword",
             "defend": "Defending"
                }


def onTurnEnd(team1, team2):
    pass


def affectStatus(affected):
    return