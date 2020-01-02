import random

def roll_dice(amount, score, range):
    rolls = []
    i = 0
    while i < amount:
        rolls.append(score + random.randrange(1, range+1))
        i += 1
    return rolls

def roll_explorer_dice(amount):
    return roll_dice(amount, 10, 4)

def roll_attacker_dice(amount):
    return roll_dice(amount, 20, 6)

def roll_tank_dice(amount):
    return roll_dice(amount, 30, 8)

def get_rolls(att_rolls_counter, def_rolls_counter):
    attack_rolls = []
    defending_rolls = []
    
    attack_rolls = roll_explorer_dice(att_rolls_counter[0]) + roll_attacker_dice(att_rolls_counter[1]) + roll_tank_dice(att_rolls_counter[2])
    defending_rolls = roll_explorer_dice(def_rolls_counter[0]) + roll_attacker_dice(def_rolls_counter[1]) + roll_tank_dice(def_rolls_counter[2])

    return attack_rolls, defending_rolls

def  fill_rolls(rolls):
    i = len(rolls)
    if i < 5:
       while i < 5:
           rolls.append(0)
           i += 1
    return rolls

def combat(att_rolls_counter, def_rolls_counter):
    # Get rolls
    rolls = get_rolls(att_rolls_counter, def_rolls_counter)
    att_rolls = sorted(rolls[0], key=lambda n: n%10, reverse=True)
    def_rolls = sorted(rolls[1], key=lambda n: n%10, reverse=True)

    #Combat system
    while len(att_rolls) > 0 and len(def_rolls) > 0:
        att_rolls = fill_rolls(att_rolls)
        def_rolls = fill_rolls(def_rolls)
        i = 0
        for roll in def_rolls:
            # print(att_rolls[i],' vs ', roll)
            if (roll % 10) > (att_rolls[i] % 10):
                #Deff loses
                att_rolls[i] = 0
            elif (roll % 10) < (att_rolls[i] % 10):
                #Att wins
                def_rolls[i] = 0
            elif (roll % 10) == (att_rolls[i] % 10):
                #Both loses
                def_rolls[i] = 0
                att_rolls[i] = 0
            i += 1

        while 0 in def_rolls:
            def_rolls.remove(0)

        while 0 in att_rolls:
            att_rolls.remove(0)
    
    if len(att_rolls) == 0 and len(def_rolls) == 0:
        return 0
    elif len(att_rolls) == 0:
        return ['defending',def_rolls]
    else:
        return ['attacking',att_rolls]
