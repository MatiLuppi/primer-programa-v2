p_one_hp = 0
p_two_hp = 0
p_one_damage = 0
p_two_damage = 0
p_one_name = 0
p_two_name = 0
p_one_attack = 0
p_two_attack = 0

player_one = input("player 1, what pokemon will you take? (Infernape/ Sharpedo/ Tyranitar): ").upper()

if player_one == "INFERNAPE":
    p_one_hp = 100
    p_one_name = "Infernape"
    print("player one sent out {}".format(player_one))

elif player_one == "TYRANITAR":
    p_one_hp = 100
    p_one_name = "Tyranitar"
    print("player one sent out {}".format(player_one))

elif player_one == "SHARPEDO":
    p_one_hp = 70
    p_one_name = "Sharpedo"
    print("player one sent out {}".format(player_one))

player_two = input("player 2, what pokemon will you take? (Venasaur/ Pachirisu/ Garchomp): ").upper()

if player_two == "VENASAUR":
    p_two_hp = 130
    p_two_name = "Venasaur"
    print("player two sent out {}".format(p_two_name))

elif player_two == "PACHIRISU":
    p_two_hp = 70
    p_two_name = "pachirisu"
    print("player two sent out {}".format(p_two_name))

elif player_two == "GARCHOMP":
    p_two_hp = 90
    p_two_name = "Garchomp"
    print("player two sent out {}".format(p_two_name))

while p_one_hp > 0 and p_two_hp > 0:
    if player_one == "INFERNAPE":
        p_one_attack = input("(Player 1)What attack you want to use? (Fire Blitz/ Meteor Punch): ")
        if p_one_attack == "meteor punch":
            p_two_hp -=40
            print("{} used {} ({} currently has {}HP)".format(p_one_name, p_one_attack, p_two_name, p_two_hp))
        elif p_one_attack == "fire blitz":
            p_two_hp -=80
            print("{} used {} ({} currently has {}HP)".format(p_one_name, p_one_attack, p_two_name, p_two_hp))
        else:
            print("{} falied".format(p_one_name))

    if player_one == "SHARPEDO":
        p_one_attack = input("(Player 1)What attack you want to use? (Dark Slash/ Tackle): ")
    if p_one_attack == "dark slash":
        p_two_hp -=60
        print("{} used {} ({} currently has {}HP)".format(p_one_name, p_one_attack, p_two_name, p_two_hp))
    elif p_one_attack == "tackle":
        p_two_hp -=40
        print("{} used {} ({} currently has {}HP)".format(p_one_name, p_one_attack, p_two_name, p_two_hp))
    else:
        print("{} falied".format(p_one_name))

    if player_one == "TYRANITAR":
        p_one_attack = input("(Player 1)What attack you want to use? (Tail Slap/ Gigacrush): ")
        if p_one_attack == "tail slap":
            p_two_hp -=40
            print("{} used {} ({} currently has {}HP)".format(p_one_name, p_one_attack, p_two_name, p_two_hp))
        elif p_one_attack == "gigacrush":
            p_two_hp -=70
            print("{} used {} ({} currently has {}HP)".format(p_one_name, p_one_attack, p_two_name, p_two_hp))
        else:
            None

    if player_two == "VENASAUR":
        p_two_attack = input("(Player 2)What attack you want to use? (Razor Leafe/ Solar Beam): ")
        if p_two_attack == "razor leafe":
            p_one_hp -=35
        elif p_two_attack == "solar beam":
            p_one_hp -=60
        else:
            print("{} failed".format(p_two_name))

    if player_two == "PACHIRISU":
        p_two_attack = input("(Player 2)What attack you want to use? (Thunder Bolt/ Poison Berry): ")
        if p_two_attack == "thunder bolt":
            p_one_hp -=50
        elif p_two_attack == "poison berry":
            p_one_hp -=25
        else:
            print("{} failed".format(p_two_name))

    if player_two == "GARCHOMP":
        p_two_attack = input("(player 2)What attack you want to use? (Dragon Pulse/ Dragon Fang): ")
        if p_two_attack == "dragon pulse":
            p_one_hp -=60
        elif p_two_attack == "fragon fang":
            p_one_hp -=80
        else:
            None

