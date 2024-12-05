import random
from parser import CharacterParser

class GameCharacter:
    def __init__(self, name, health, damage, armor, resist):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.resist = resist

    def attack(self, target):
        clean_damage = max(self.damage - target.armor, 0)
        final_damage = clean_damage * (1 - target.resist)
        target.health -= final_damage
        return final_damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: Health={self.health}, Damage={self.damage}, Armor={self.armor}, Resist={self.resist}"

class Game:
    def __init__(self):
        self.characters = []
        self.history = []

    def load_characters(self):
        parser = CharacterParser()
        data = parser.load_characters()
        self.characters = [
            GameCharacter(
                name=c["name"],
                health=random.randint(50, 100),
                damage=random.randint(10, 20),
                armor=random.randint(5, 10),
                resist=random.uniform(0.1, 0.3)
            )
            for c in data
        ]

    def start(self):
        self.load_characters()
        if not self.characters:
            print("No characters available to play.")
            return

        print("Choose your character:")
        for index, character in enumerate(self.characters, start=1):
            print(f"{index}. {character}")

        choice = int(input("Enter character number: ")) - 1
        player = self.characters[choice]
        enemy = random.choice([c for c in self.characters if c != player])

        print(f"You chose {player.name}. Your enemy is {enemy.name}.")
        self.play_turns(player, enemy)

    def play_turns(self, player, enemy):
        turn = 1
        player_defending = False
        while player.is_alive() and enemy.is_alive():
            print(f"Turn {turn}:")
            print(f"Your character: {player}")
            print(f"Enemy character: {enemy}")

            action = input("Choose action (attack/defend): ").strip().lower()

            if action == "attack":
                damage = player.attack(enemy)
                self.history.append(f"{player.name} attacked {enemy.name} for {damage:.2f} damage.")
                print(f"You dealt {damage:.2f} damage to {enemy.name}.")

            elif action == "defend":
                if random.random() < 0.75:
                    print(f"{player.name} dodged the attack!")
                    self.history.append(f"{player.name} dodged {enemy.name}'s attack.")
                else:
                    reduced_damage = enemy.attack(player) * 0.5
                    player.health -= reduced_damage
                    print(f"{player.name} reduced the damage and took only {reduced_damage:.2f}!")
                    self.history.append(f"{player.name} reduced the damage from {enemy.name}'s attack.")

                heal = random.randint(10, 15)
                player.health += heal
                print(f"{player.name} recovered {heal} health!")
                self.history.append(f"{player.name} defended and recovered {heal} health.")

                counter_damage = player.damage * random.uniform(0.5, 1.0)
                enemy.health -= counter_damage
                print(f"{player.name} counter-attacked and dealt {counter_damage:.2f} damage!")
                self.history.append(f"{player.name} counter-attacked {enemy.name} for {counter_damage:.2f} damage.")

            if enemy.is_alive():
                enemy_damage = enemy.attack(player)
                if player_defending and random.random() < 0.5:
                    print(f"{player.name} dodged the attack!")
                    self.history.append(f"{player.name} dodged {enemy.name}'s attack.")
                else:
                    player.health -= enemy_damage
                    self.history.append(f"{enemy.name} attacked {player.name} for {enemy_damage:.2f} damage.")
                    print(f"{enemy.name} dealt {enemy_damage:.2f} damage to you.")

            turn += 1

        if player.is_alive():
            print("You won!")
        else:
            print("You lost!")

        print("Game history:")
        for event in self.history:
            print(event)
