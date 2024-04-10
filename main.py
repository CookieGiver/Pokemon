import random
from time import sleep
import math
import os

MOVES_DICTIONARY = {
    'Scratch': 
    {
        'name': 'Scratch',
        'power': 40, 
        'type': 'Normal', 
        'super effective against': ['N/A'], 
        'not very effective against': ['Rock', 'Steel']
    },
    'Tackle': 
    {
        'name': 'Tackle',
        'power': 40, 
        'type': 'Normal', 
        'super effective against': ['N/A'], 
        'not very effective against': ['Rock', 'Steel']
    },
    'Pound': {'name': 'Pound', 'power': 40, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Rage': {'name': 'Rage', 'power': 20, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Fury Attack': {'name': 'Fury Attack', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Ember': {'name': 'Ember', 'power': 40, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']}, 
    'Fire Spin': {'name': 'Fire Spin', 'power': 35, 'type': 'Fire', 'super effective against': ['Grass', 'Ice', 'Bug', 'Steel'], 'not very effective against': ['Fire', 'Water', 'Rock', 'Dragon']}, 
    'Bubble': {'name': 'Bubble', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']}, 
    'Aqua Jet': {'name': 'Aqua Jet', 'power': 40, 'type': 'Water', 'super effective against': ['Fire', 'Ground', 'Rock'], 'not very effective against': ['Water', 'Grass', 'Dragon']}, 
    'Thunder Shock': {'name': 'Thunder Shock', 'power': 40, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']}, 
    'Thunderbolt': {'name': 'Thunderbolt', 'power': 90, 'type': 'Electric', 'super effective against': ['Water', 'Flying'], 'not very effective against': ['Electric', 'Grass', 'Dragon']}, 
    'Vine Whip': {'name': 'Vine Whip', 'power': 45, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Magical Leaf': {'name': 'Magical Leaf', 'power': 60, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Ice Shard': {'name': 'Ice Shard', 'power': 40, 'type': 'Ice', 'super effective against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'not very effective against': ['Fire', 'Water', 'Ice', 'Steel']}, 
    'Double Kick': {'name': 'Double Kick', 'power': 30, 'type': 'Fighting', 'super effective against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], 'not very effective against': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']}, 
    'Earthquake': {'name': 'Earthquake', 'power': 100, 'type': 'Ground', 'super effective against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'not very effective against': ['Grass', 'Bug']}, 
    'Wing Attack': {'name': 'Wing Attack', 'power': 60, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']}, 
    'Peck': {'name': 'Peck', 'power': 35, 'type': 'Flying', 'super effective against': ['Grass', 'Fighting', 'Bug'], 'not very effective against': ['Electric', 'Rock', 'Steel']}, 
    'Confusion': {'name': 'Confusion', 'power': 50, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']}, 
    'Twineedle': {'name': 'Twineedle', 'power': 25, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']}, 
    'Rock Throw': {'name': 'Rock Throw', 'power': 50, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']}, 
    'Rock Slide': {'name': 'Rock Slide', 'power': 75, 'type': 'Rock', 'super effective against': ['Fire', 'Ice', 'Flying', 'Bug'], 'not very effective against': ['Fighting', 'Ground', 'Steel']}, 
    'Lick': {'name': 'Lick', 'power': 30, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']}, 
    'Outrage': {'name': 'Outrage', 'power': 120, 'type': 'Dragon', 'super effective against': ['Dragon'], 'not very effective against': ['Steel']}, 
    'Crunch': {'name': 'Crunch', 'power': 80, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']}, 
    'Bite': {'name': 'Bite', 'power': 60, 'type': 'Dark', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Fighting', 'Dark', 'Fairy']}, 
    'Flash Cannon': {'name': 'Flash Cannon', 'power': 80, 'type': 'Steel', 'super effective against': ['Ice', 'Rock', 'Fairy'], 'not very effective against': ['Fire', 'Water', 'Electric', 'Steel']}, 
    'Smog': {'name': 'Smog', 'power': 30, 'type': 'Poison', 'super effective against': ['Grass', 'Fairy'], 'not very effective against': ['Poison', 'Ground', 'Rock', 'Ghost']}, 
    'Dream Eater': {'name': 'Dream Eater', 'power': 100, 'type': 'Psychic', 'super effective against': ['Fighting', 'Poison'], 'not very effective against': ['Psychic', 'Steel']}, 
    'Body Slam': {'name': 'Body Slam', 'power': 85, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Double Slap': {'name': 'Double Slap', 'power': 15, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Razor Leaf': {'name': 'Razor Leaf', 'power': 55, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Headbutt': {'name': 'Headbutt', 'power': 70, 'type': 'Normal', 'super effective against': ['N/A'], 'not very effective against': ['Rock', 'Steel']}, 
    'Absorb': {'name': 'Absorb', 'power': 20, 'type': 'Grass', 'super effective against': ['Water', 'Ground', 'Rock'], 'not very effective against': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']}, 
    'Fairy Wind': {'name': 'Fairy Wind', 'power': 40, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']}, 
    'Struggle Bug': {'name': 'Struggle Bug', 'power': 50, 'type': 'Bug', 'super effective against': ['Grass', 'Psychic', 'Dark'], 'not very effective against': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']}, 
    'Draining Kiss': {'name': 'Draining Kiss', 'power': 50, 'type': 'Fairy', 'super effective against': ['Fighting', 'Dragon', 'Dark'], 'not very effective against': ['Fire', 'Poison', 'Steel']}, 
    'Shadow Ball': {'name': 'Shadow Ball', 'power': 80, 'type': 'Ghost', 'super effective against': ['Psychic', 'Ghost'], 'not very effective against': ['Dark']}
}

POKEMONS = {
    'Pikachu': {'Type': ['Electric'], 'HP': 35, 'Moves': ['Thunder Shock',  'Double Kick', 'Thunderbolt'], 'Attack': 55, 'Defense': 40, 'Speed': 90, 'Experience': 112},
    'Charizard': {'Type': ['Fire', 'Flying'], 'HP': 78, 'Moves': [ 'Crunch', 'Ember', 'Scratch', 'Wing Attack'], 'Attack': 84, 'Defense': 78, 'Speed': 100, 'Experience': 240},
    'Squirtle': {'Type': ['Water'], 'HP': 44, 'Moves': ['Tackle',  'Bubble', 'Bite'], 'Attack': 48, 'Defense': 65, 'Speed': 43, 'Experience': 63},
    'Jigglypuff': {'Type': ['Normal', 'Fairy'], 'HP': 115, 'Moves': ['Pound', 'Body Slam', 'Double Slap'], 'Attack': 45, 'Defense': 20, 'Speed': 20, 'Experience': 95},
    'Gengar': {'Type': ['Ghost', 'Poison'], 'HP': 60, 'Moves': ['Lick', 'Smog', 'Dream Eater', 'Shadow Ball'], 'Attack': 65, 'Defense': 60, 'Speed': 110, 'Experience':225},
    'Magnemite': {'Type': ['Electric', 'Steel'], 'HP': 25, 'Moves': [ 'Tackle', 'Flash Cannon', 'Thunder Shock', 'Thunderbolt'],  'Attack': 35, 'Defense': 70, 'Speed': 45, 'Experience': 65},
    'Bulbasaur': {'Type': ['Grass', 'Poison'], 'HP': 45, 'Moves': ['Tackle', 'Vine Whip', 'Razor Leaf'], 'Attack': 49, 'Defense': 49, 'Speed': 45, 'Experience': 64},
    'Charmander': {'Type': ['Fire'], 'HP': 39, 'Moves': ['Scratch', 'Ember', 'Fire Spin'], 'Attack': 52, 'Defense': 43, 'Speed': 65, 'Experience': 62},
    'Beedrill': {'Type': ['Bug', 'Poison'], 'HP': 65, 'Moves': ['Peck', 'Twineedle', 'Rage', 'Fury Attack', 'Outrage'], 'Attack': 90, 'Defense': 40, 'Speed': 75, 'Experience': 178},
    'Golem': {'Type': ['Rock', 'Ground'], 'HP': 80, 'Moves': [ 'Tackle', 'Rock Throw', 'Rock Slide', 'Earthquake'], 'Attack': 120, 'Defense': 130, 'Speed': 45, 'Experience': 223},
    'Dewgong': {'Type': ['Water', 'Ice'], 'HP': 90, 'Moves': ['Aqua Jet',  'Ice Shard', 'Headbutt'], 'Attack': 70, 'Defense': 80, 'Speed': 70, 'Experience': 166},
    'Hypno': {'Type': ['Psychic'],'HP': 85, 'Moves': ['Pound', 'Confusion', 'Dream Eater'], 'Attack': 73, 'Defense': 70, 'Speed': 67, 'Experience': 169},
    'Cleffa': {'Type': ['Fairy'], 'HP': 50, 'Moves': [ 'Pound', 'Magical Leaf'], 'Attack': 25, 'Defense': 28, 'Speed': 15, 'Experience': 44},
    'Cutiefly': {'Type': ['Fairy', 'Bug'], 'HP': 40, 'Moves': ['Absorb', 'Fairy Wind', 'Struggle Bug', 'Draining Kiss'], 'Attack': 45, 'Defense': 40, 'Speed': 84, 'Experience': 61}
}

class Pokemon():
    '''Pokemon Class: ontains attributes and methods associated with the Pokemon character
        
    '''
    def __init__(self, name):
        self.name = name
        self.type = POKEMONS[name]['Type']
        self.hp = POKEMONS[name]['HP']
        self.max_hp = POKEMONS[name]['HP']
        self.moves = POKEMONS[name]['Moves']
        self.ATTACK = POKEMONS[name]['Attack']
        self.DEFENSE = POKEMONS[name]['Defense']
        self.speed = POKEMONS[name]['Speed']
        self.experience = POKEMONS[name]['Experience']
        self.buff_modifier = [1, 1]
        self.dead = False

    @property
    def level(self):
        '''
        Property returning level attribute = cube root of experience
        '''
        return math.floor(self.experience**(1/3))

    @property
    def attack(self):
        '''
        Property returning attack attribute with modifier
        '''
        return self.ATTACK * self.buff_modifier[0]

    @property
    def defense(self):
        '''
        Property returning defense attribute with modifier
        '''
        return self.DEFENSE * self.buff_modifier[1]

    @property
    def health_bar(self):
        '''Property which returns a formatted health bar using ASCII symbols
        '''
        percentage = int(round(self.hp / self.max_hp, 1)*10)
        return percentage*'▮ ' + (10-percentage)*'▯ '

    def calc_damage(self, move, pokemon):
        '''Calculates Pokemon damage based on a variety of factors
        
        Args:
            pokemon (Pokemon Class): represents the attacking pokemon
            move (string): represents the move used by the pokemon
        
        Returns:
            damage: rounded calculated damage based on pokemon and move
        '''
        modifier = 1
        for i in self.type:
            if i in MOVES_DICTIONARY[move]['super effective against']:
                modifier *= 2
            elif i in MOVES_DICTIONARY[move]['not very effective against']:
                modifier *= 0.5
        rand_speed = random.randrange(0,512)
        if rand_speed >= self.speed:
            modifier *= 2
        rand = random.randrange(85,101)
        rand = rand/100
        modifier *= rand

        power = MOVES_DICTIONARY[move]['power']
        attack = pokemon.attack
        defense = self.defense
        damage = ((2*self.level / 5 + 2) * power * (attack/defense))/50 * modifier
        return round(damage)

    def take_dmg(self, damage):
        '''Subtracts health from Pokemon and registers if their health is below or equal to 0
        
        Args:
            damage (int): represents amount of damage taken by Pokemon
        '''
        self.hp -= damage
        if self.hp <= 0:
            self.dead = True

    def __repr__(self):
        return self.name

LINE_LENGTH = 40

class Battle():
    '''Battle Class: runner class for pokemon battles
    
    Args:
        player_pokemon (Pokemon Class): represents player pokemon
        comp_pokemon (Pokemon Class): represents the radomized computer pokemon
    '''

    def __init__(self, player_pokemon, comp_pokemon):
        self.player_pokemon = player_pokemon
        self.comp_pokemon = comp_pokemon

    def fight(self, damage, pokemon):
        '''Does an amount of damage to target Pokemon
        
        Args:
            damage (int): represents the amount of damage
            pokemon (Pokemon Class): represents the target pokemon
        '''
        pokemon.take_dmg(damage)

    def optimized_attack(self):
        '''Returns the move that deals the optimal damage by the computer pokemon
        
        Returns:
            damage, move (int, string): returns a tuple representing the optimal move and the damage it does
        '''
        move_damages = [(self.player_pokemon.calc_damage(move, self.comp_pokemon), move) for move in self.comp_pokemon.moves]
        move_damages.sort(reverse=True)
        return move_damages[0]

    def item_action(self):
        '''Function representing the item_action turn by player: allows the user to use an item
        '''
        for index, item in enumerate(collection.items):
            print(f'{index+1}. {item}')
        chosen_item = collection.items[int(input('Type in the number of the item which you wish to use: '))-1]
        if isinstance(chosen_item, DamageItem):
            chosen_item.use_item(self.comp_pokemon)
        else:
            chosen_item.use_item(self.player_pokemon)
        del chosen_item

    def switch_action(self):
        '''Function representing the switch_action turn by player: allows player to switch pokemon
        '''
        print("")
        collection.print_pokemon(self.player_pokemon)

        chosen_pokemon = collection.pokemons[int(input("Choose your pokemon: "))-1]
        chosen_pokemon.hp = round(chosen_pokemon.max_hp * (self.player_pokemon.hp/self.player_pokemon.max_hp))
        print(f'{self.player_pokemon} was switched for {chosen_pokemon} with {chosen_pokemon.hp} HP!')
        self.player_pokemon = chosen_pokemon

    def death_check(self):
        '''Function that checks the death statuses of the two pokemon
        
        Returns:
            (bool): represents if the battle has ended
        '''
        if self.player_pokemon.dead:
            print(f'{self.player_pokemon.name} has fainted, {self.comp_pokemon.name} wins!')
            return True
        elif self.comp_pokemon.dead:
            print(f'{self.comp_pokemon.name} has fainted, {self.player_pokemon.name} wins!')

            if difficulty > 4:
                potions = [Potion(10), Potion(10), Potion(30), Potion(30), 20, 10, 10, 20]
            elif difficulty == 4:
                potions = [Potion(10), Potion(10), Potion(30), Potion(30), 20, 20, 20, 20]
            else:
                potions = [Potion(20), Potion(40), Potion(40), Potion(60), 30, 35, 35, 30]
            loot = random.choice(potions)
            if isinstance(loot, Potion):
                print(f'You have earned a {loot}!')
                collection.add_item(loot)
            else:
                print(f'You have earned ${loot}!')
                collection.money += loot

            self.comp_pokemon.hp = self.comp_pokemon.max_hp
            self.comp_pokemon.dead = False
            collection.add_pokemon(self.comp_pokemon)

            self.player_pokemon.experience += self.comp_pokemon.experience
            self.player_pokemon.hp += math.floor((self.player_pokemon.max_hp - self.player_pokemon.hp)/2)
            self.player_pokemon.buff_modifier = [1, 1]
            return True
        else:
            return False

    def main(self):
        '''Main runner class facilitating the battle
        contains alternating player turns based on variable "counter" and corresponding actions
        '''
        if self.player_pokemon.speed > self.comp_pokemon.speed:
            counter = 1
        else:
            counter = 0

        if difficulty == 5:
            self.comp_pokemon.experience = max(self.comp_pokemon.experience, collection.pokemons[0].experience)
        if difficulty == 4:
            self.comp_pokemon.experience = max(self.comp_pokemon.experience, self.player_pokemon.experience)
        #self.comp_pokemon.hp = 1
        print(f'A wild {self.comp_pokemon.name} appeared! (Level {self.comp_pokemon.level})')

        while True:
            clear_screen()
            print(f'{self.player_pokemon} {self.player_pokemon.health_bar} {self.player_pokemon.hp} HP vs {self.comp_pokemon} {self.comp_pokemon.health_bar} {self.comp_pokemon.hp} HP')
            if counter % 2 == 0:
                print('\nComputer Turn!')
                prob = random.randrange(0, 5)
                if prob < difficulty:
                    damage, move = self.optimized_attack()
                else:
                    move = random.choice(self.comp_pokemon.moves)
                    damage = self.player_pokemon.calc_damage(move, self.player_pokemon)

                self.fight(damage, self.player_pokemon)
                print(f'{self.comp_pokemon.name} used {move} for {damage} damage!')
                print(f'{self.player_pokemon.name} is now at {self.player_pokemon.hp} health')
                if self.death_check():
                    sleep(4)
                    clear_screen()
                    break

            else:
                print('\nPlayer Turn!')
                for index, move in enumerate(self.player_pokemon.moves):
                    print(f'{index+1}. {move}')
                if len(collection.items) > 0:
                    print(f'{len(self.player_pokemon.moves)+1}. Use Item')
                if len(collection.pokemons) > 1:
                    print(f'{len(self.player_pokemon.moves)+2}. Swap Pokemon')
                try:
                    action_index = int(input(

                        'Type in the number of the move which you wish to use: '))
                    chosen_move = self.player_pokemon.moves[action_index-1]
                    damage = self.comp_pokemon.calc_damage(chosen_move, self.player_pokemon)
                    self.fight(damage, self.comp_pokemon)

                    print(f'{self.player_pokemon.name} used {chosen_move} for {damage} damage!')
                    print(f'{self.comp_pokemon.name} is now at {self.comp_pokemon.hp} health')
                except IndexError:
                    if action_index == len(self.player_pokemon.moves)+1:
                        self.item_action()
                    elif action_index == len(self.player_pokemon.moves)+2:
                        self.switch_action()
                if self.death_check():
                    sleep(4)
                    clear_screen()
                    break

            sleep(2)
            counter += 1


class Shop():
    '''
    Shop class:
    '''
    def __init__(self):
        self.items = [random.choice([Potion(random.choice([20, 40, 60])), DamageItem(random.choice([10, 20, 30])), Buff(random.choice([1.5, 2, 3]), random.choice(['attack', 'defense']))]) for i in range(9)]

    def reload(self):
        self.items = [random.choice([Potion(random.choice([20, 40, 60])), DamageItem(random.choice([10, 20, 30])), Buff(random.choice([1.5, 2, 3]), random.choice(['attack', 'defense']))]) for i in range(9)]


class Buff():
    '''
    Buff class:
    '''
    def __init__(self, modifier, type_):
        self.type_ = type_
        self.modifier = modifier
        self.price = modifier*20

    def use_item(self, pokemon):
        ''' 
        Uses buff on target pokemon
        
        Args:
            target_pokemon (class: Pokemon): gives pokemon item will be used on
        '''
        if self.type_ == 'attack':
            pokemon.buff_modifier[0] *= self.modifier
        else:
            pokemon.buff_modifier[1] *= self.modifier
        print(f'{pokemon.name}\'s {self.type_} was buffed x{self.modifier}')


    def __repr__(self):
        return f'{self.type_.title()} Buff x{self.modifier}'
            
class DamageItem():
    '''
    Damage item class:
    '''
    def __init__(self, value):
        self.value = value
        self.price = round(value*(4/3))

    def use_item(self, target_pokemon):
        ''' 
        Uses damage item on target pokemon
        
        Args:
            target_pokemon (class: Pokemon): gives pokemon item will be used on
        '''
        target_pokemon.take_dmg(self.value)
        print(f'{target_pokemon.name} took {self.value} damage!')

    def __repr__(self):
        return f'{self.value} Damage Item'


class Potion():
    '''
    Potion class:
    
    '''
    
    def __init__(self, value):
        self.value = value
        self.price = round(value*1.5)

    def use_item(self, target_pokemon):
        ''' 
        Uses potion on target pokemon
        
        Args:
            target_pokemon (class: Pokemon): gives pokemon item will be used on
        '''
        delta_hp = min(target_pokemon.hp + self.value, POKEMONS[target_pokemon.name]['HP']) - target_pokemon.hp
        target_pokemon.hp += delta_hp
        print(f'{target_pokemon.name} was healed for {delta_hp}!')
        
    def __repr__(self):
        return f'{self.value} HP Potion'


class Player():
    '''
    Player Class:

    '''
    def __init__(self):
        self.pokemons = []
        self.items = [Potion(20), DamageItem(30), Buff(2, 'attack')]
        self.money = 100

    def formatted_pokemon_list(self, *omitted_pokemon):
        '''
        Returns array of Pokemon formatted in x by 3 grid
        can pass a pokemon into the function if you'd like to omit that pokemon from the array

        Args:
            (Optional) omitted_pokemon (class: Pokemon): will omit given pokemon from reformated list
        '''
        pokemon_list = [pokemon for pokemon in self.pokemons if not pokemon in omitted_pokemon]
        formatted_pokemon = []
        for i in range(math.floor(len(pokemon_list)/3)):
            formatted_pokemon.append([pokemon_list[i*3], pokemon_list[i*3+1], pokemon_list[i*3+2]])
        if not len(pokemon_list)%3 == 0:
            formatted_pokemon.append([])
            for i in range(len(pokemon_list)%3):
                formatted_pokemon[-1].insert(0, pokemon_list[-(i+1)])
        return formatted_pokemon

    def print_pokemon(self, omitted_pokemon=None):
        '''
        Prints Pokemon from collection (will omit inputed pokemon)
        
        Args:
            omitted_pokemon(class: Pokemon): will cause given pokemon to be omitted from print statement
        '''
        for i, row in enumerate(self.formatted_pokemon_list(omitted_pokemon)):
            data = ['', '', '', '', '', '', '', '']
            for j, pokemon in enumerate(row):
                data[0] += f'{i*3+j+1}. {pokemon.name}'
                data[1] += f'Level: {pokemon.level}'
                data[2] += f"Type: {', '.join(pokemon.type)}"
                data[3] += f"HP: {pokemon.max_hp}"
                data[4] += f"Moves: {', '.join(POKEMONS[pokemon.name]['Moves'])}"
                data[5] += f"Attack: {POKEMONS[pokemon.name]['Attack']}"
                data[6] += f"Defense: {POKEMONS[pokemon.name]['Defense']}"
                data[7] += f"Speed: {POKEMONS[pokemon.name]['Speed']}"

                for k in range(len(data)):
                    data[k] += ((j+1)*LINE_LENGTH-len(data[k]))*' '
            for attribute in data:
                print(attribute)
            print('')

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        temp = [(pokemon.level, pokemon) for pokemon in self.pokemons]
        temp.sort(key=lambda a: a[0], reverse=True)
        self.pokemons = [x[1] for x in temp]

    def add_item(self, item):
        self.items.append(item)


def clear_screen():
    '''
    Clears Terminal screen
    '''
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

ascii_ = random.choice(['ascii_poke.txt','ascii_poke_1.txt','ascii_poke_2.txt','ascii_poke_3.txt'])
file = open(ascii_)
image = file.read()
print(image + '\n')

difficulty = int(input("Input the level of difficulty you wish to set (0-5): "))
sleep(1)
clear_screen()

starters = ['Bulbasaur', 'Squirtle', 'Charmander']
data = ['', '', '', '', '', '', '']
for i, pokemon in enumerate(starters):
    data[0] += f'{i+1}. {pokemon}'
    data[1] += f"Type: {', '.join(POKEMONS[pokemon]['Type'])}"
    data[2] += f"HP: {POKEMONS[pokemon]['HP']}"
    data[3] += f"Moves: {', '.join(POKEMONS[pokemon]['Moves'])}"
    data[4] += f"Attack: {POKEMONS[pokemon]['Attack']}"
    data[5] += f"Defense: {POKEMONS[pokemon]['Defense']}"
    data[6] += f"Speed: {POKEMONS[pokemon]['Speed']}"

    for j in range(len(data)):
        data[j] += ((i+1)*LINE_LENGTH-len(data[j]))*' '
for attribute in data:
    print(attribute)
print('')
    
starter_pokemon = Pokemon(starters[int(input("Choose your starter pokemon (1-3): "))-1])

collection = Player()
collection.add_pokemon(starter_pokemon)

shop = Shop()

def home():
    '''
    Home screen for player:
    '''
    while True:
        for index, option in enumerate(options):
            print(f'{index+1}. {option}')
        choice = int(input("Choose what you want to do next: "))
        if choice == 1:
            return False
        elif choice == 2:
            clear_screen()
            print(f'\nYour Balance: ${collection.money}')
            for i in range(3):
                for item in shop.items[i*3:i*3+3]:
                    print(f'{shop.items.index(item)+1}. {item}: ${item.price}{(20-len(item.__repr__()+": $"+str(item.price)))*" "}', end='  ')
                print('')
            print('')
            try:
                chosen_item = shop.items[int(input('Press x to exit or a number to buy the corresponding item: '))-1]
                print(f"{chosen_item} was bought for ${chosen_item.price}")
                collection.add_item(chosen_item)
                collection.money -= chosen_item.price
                sleep(2)
                clear_screen()
            except:
                clear_screen()
        elif choice == 3:
            collection.print_pokemon()
            input('Press ENTER when you want to exit')
        elif choice == 4:
            clear_screen()
            for index, item in enumerate(collection.items):
                print(f'{index+1}. {item}')
            try:
                chosen_item = collection.items[int(input('Press x to exit or a number to use the corresponding item: '))-1]
                collection.print_pokemon()
                chosen_pokemon = collection.pokemons[int(input(f'Type number of pokemon which you wish to use the item on: '))-1]
                chosen_item.use_item(chosen_pokemon)
                collection.items.remove(chosen_item)
                sleep(2)
                clear_screen()
            except ValueError:
                clear_screen()
        else:
            return True

while True:
    clear_screen()
    
    pokemon_encounter = Pokemon(random.choice(list(POKEMONS.keys())))

    collection.print_pokemon()
        
    chosen_pokemon = collection.pokemons[int(input("Choose your pokemon: "))-1]

    clear_screen()
    battle = Battle(chosen_pokemon, pokemon_encounter)
    battle.main()
    
    options = ["Continue", "Access Shop", "Pokemon Collection", "Items", "Finish"]
    
    if home():
        break