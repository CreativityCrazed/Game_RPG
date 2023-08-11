from Player import *
from Monsters.Monster import *
from Monsters.Skeleton import *
from Monsters.Spirit import *

def create_monster():
    Monsters = ["Skeleton", "Spirit"]
    monster_name = random.choice(Monsters)
    return eval(f"{monster_name}()")

def run_game(name):
    player = Player(name)
    monster = create_monster()
    player.add_rand_item()
    player.add_rand_item()

    while True:
        if player.hp > 0:
            say = input("Вы можете ввести команды: city, dunge и status\n")
        if "city" == say or player.hp == 0:
            while True:
                player.heal()
                print("\nВаше здоровье восстановилось\n")
                player.print_stats()
                print("Вы находитесь в городе. Вы можете выйти из города введя: exit")
                say = input()
                if "exit" == say:
                    print("Вы вышли из города.")
                    break

        if "dunge" == say:
            print("Вы вошли в подземелье")
            while True:
                print("Вы можете поискать мобов: mob или выйти: exit, Посмотреть статус: status")
                say = input()

                if "mob" == say:

                    if monster.is_death:
                        monster = create_monster()

                    while not player.is_death and not monster.is_death:
                        player.print_stats()
                        monster.print_stats()
                        say = input("Введите команды: attack или run\n")
                        if say == "attack":
                            player.fight(monster)
                        if say == "run":
                            if random.random() * 100 < 30:
                                player.fight(monster, False, True)
                            break
                        if player.is_death:
                            #player.heal()
                            print("\nЧувак, ты только что помер, но мы тебя восскресили. \nСходил бы ты в город, подлечился)")
                            #player.print_stats()
                            break
                if player.hp == 0:
                    break

                if "status" == say:
                    player.print_stats()

                if "inv" == say:
                    player.print_items()

                if "exit" == say:
                    print("Вы вышли из подземелья")
                    break

        if "status" == say:
            player.print_stats()
        if "inv" == say:
            player.print_items()



player_name = input("Введите имя игрока: ")
run_game(player_name)
