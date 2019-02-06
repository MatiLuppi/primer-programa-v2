pikachu_hp = 100
rival_hp = 0
pokemon_elegido = input("what pokemon you want to fight against?(BULBASAUR/SQUIRTLE/CHARMANDER): ").upper()
rival_name = 7
rival_damage = 0
rival_attack = 3


if pokemon_elegido == "SQUIRTLE":
    rival_hp = 90
    rival_name = "Squirtle"
    rival_damage = 10
    rival_attack = "Bubble Beam"
# ses
elif pokemon_elegido == "CHARMANDER":
    rival_hp = 80
    rival_name = "Charmander"
    rival_damage = 11
    rival_attack = "Ember"

elif pokemon_elegido == "BULBASAUR":
    rival_hp = 100
    rival_name = "bulbasaur"
    rival_damage = 12
    rival_attack = "Razor Leafe"

if (pokemon_elegido == "BULBASAUR" or pokemon_elegido == "SQUIRTLE" or pokemon_elegido == "CHARMANDER"):
    print("your rival has sent out {}".format(rival_name))
else:
    print("that's not a pokemon")
print("You has sent out Pikachu")

while pikachu_hp > 0 and rival_hp > 0:

    chose_atack = input("what atack you want to use (TACKLE/THUNDERBOLT): ").upper()




    if chose_atack == "TACKLE":
        rival_hp -=10

    elif chose_atack == "THUNDERBOLT":
        rival_hp -=13

    else: rival_hp -=0

    print("{} has actually {}HP".format(pokemon_elegido, rival_hp))

    print("{} used {}".format(rival_name, rival_attack ))

    pikachu_hp -= rival_damage

    print("Your Pikachu has actually {}HP".format(pikachu_hp))
if rival_hp <= 0:
    print("You won, rival paid you 35")
elif pikachu_hp <= 0:
    print("You lose")