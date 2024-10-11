import time

class Player:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
        self.inventory = {}
        self.active_item = None

class Item:
    def __init__(self, name, category, power):
        self.name = name
        self.category = category
        self.power = power

class Enemy:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

class Main:
    def __init__(self, player):
        self.player = player
        self.current_location = "forest"
        self.locations = {
            "forest": {
                "north": "cave",
                "south": "cliff"
            },
            "cave": {
                "south": "forest"
            },
            "cliff": {
                "north": "forest"
            }
        }
    
    def spawn_item(self, item_name, item_type, item_power):
        
        return Item(item_name, item_type, item_power)
    
    def spawn_enemy(self, enemy_name, enemy_hp, enemy_power):

        return Enemy(enemy_name, enemy_hp, enemy_power)

    def combat(self, enemy, turns):

        for _ in range(turns):
            self.player.hp -= enemy.power
            enemy.hp -= self.player.power

            print(f"--> Your health point: {self.player.hp}")
            print(f"Enemy health point: {enemy.hp}")

            time.sleep(2)

    def take_item(self, item):

        self.player.inventory[item.name] = item

    def use_item(self, item):

        inventory = self.player.inventory
        target_item = None

        if target_item is None and item in inventory:
            target_item = inventory[item]

        print(f"DEBUG > target_item: {target_item} - type: {type(target_item)}")
        print(f"target_item access-value: {target_item.category}")

        if target_item is not None: 
            if target_item.category == "weapon":
                self.player.active_item = target_item.name
                self.player.power += target_item.power
            elif inventory[target_item.category] == "potion":
                self.player.hp += target_item.power
            else:
                print("This item can't be use")
        else:
            print("There is no item named that in your inventory")

    def move(self):

        destination = []

        print(f"You're in {self.current_location}")
        print("Where do you wanna go?")

        temp_current_location = self.locations[self.current_location]

        for direction in temp_current_location:
            destination.append(direction)
            print(f"Head {direction} to the {temp_current_location[direction]}.")

        user_direction = str(input(": "))

        for i in range(len(destination)):
            # print(f"1: {destination}")
            # print(f"2: {destination[i]}")
            # print(f"3: {user_direction}")
            # print(f"4: {self.current_location}")
            if destination[i] in user_direction:
                self.current_location = temp_current_location[user_direction]

player1 = Player(500, 5)
game = Main(player1)

def winter_season():
    print("The snow is so thick and you get cold, you must find a warm place")

    game.move()

    if game.current_location == "cliff":
        print("You arrived at the cliff, such beautiful view, but you died cause hypothermia")
        print("What a shame Traveller")
        return False
    elif game.current_location == "cave":
        print("You found a cave, and make a camp fire, you slowly get warm up")
        print("You feel hungry, but your supplies is running out")
        print("So you look something to eat, luckly you found a snow rabbit,")
        print("There is other option, rather to turn the rabbit into your dinner")
        
        knife = game.spawn_item("knife", "weapon", 10)
        game.take_item(knife)

        print("Take your knife from your inventory and use it")

        respond_2_decision1 = str(input("Am I gonna use my knife to kill the rabbit? [Yes/Nah] "))

        print("Did take your knife?")

        respond_2_decision2 = str(input("[Yes/Nah] "))

        if respond_2_decision1 == "Nah" and respond_2_decision2 == "Nah":
            print("Use your knife brother!")
        elif respond_2_decision1 == "Nah" and respond_2_decision2 == "Yes":
            print("Bruh... don't be kidding")
        elif respond_2_decision1 == "Yes" and respond_2_decision2 == "Yes":
            print("Great! now chase after him (snow rabbit)!")
        elif respond_2_decision1 == "Yes" and respond_2_decision2 == "Nah":
            print("Alright, whatever now go!")

        game.use_item("knife")
        print(game.player.power)

        snow_rabbit = game.spawn_enemy("snow rabbit", 100, 0)

        game.combat(snow_rabbit, 10)

        if player1.hp == 0 and snow_rabbit.hp != 0 or snow_rabbit.hp < 0:
            print(f"What!? you lose against {snow_rabbit.name}?")
            return False
        
        print("Great fight bro!")


while True:
    winter_season()

    break
