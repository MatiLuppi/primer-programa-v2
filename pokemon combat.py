pikachu_hp = 100
rival_hp = 0
pokemon_elegido = input("what pokemon you want to fight against?(BULBASAUR/SQUIRTLE/CHARMANDER): ")

if pokemon_elegido == "SQUIRTLE":
    rival_hp = 90

if pokemon_elegido == "CHARMANDER":
    rival_hp = 80

if pokemon_elegido == "BULBASAUR":
    rival_hp = 100

print("your rival has sent out {}".format(pokemon_elegido))

while pikachu_hp > 0 and rival_hp > 0:

    chose_atack = input("what atack you want to use (TACKLE/THUNDERBOLT)")

    if chose_atack == "TACKLE":
        rival_hp -=10

    if chose_atack == "THUNDERBOLT":
        rival_hp -=13

    if pokemon_elegido == "SQUIRTLE":
        print("Squirtle used tackle (-10HP)")
        pikachu_hp -=10

    if pokemon_elegido == "CHARMANDER":
        print("Charmander used Ember (-13HP)")
        pikachu_hp -=13

    if pokemon_elegido == "BULBASAUR":
        print("Bulbasaur used aor leafe (-12HP)")
        pikachu_hp -=12
