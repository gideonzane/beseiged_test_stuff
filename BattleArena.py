import besieged_PlayerUnit as unit
from ndxpm import capitalize as cap
from random import randint, choice as rnd, choice

class Player(unit.PlayerUnit):
    def __init__(self, faction, race, unit_class, unit_name, index, health):
        super().__init__(faction, race, unit_class, unit_name)
        self.index = index
        self.health = health
        
    def __repr__(self):
        
        is_dead_string = '(Deceased)' if self.is_dead else ''
        is_female_string = 'Female' if self.is_female else 'Male'

        return f'\n\nName: {self.unit_name} {is_dead_string}\n' \
            f'{is_female_string} {self.race} {self.unit_class}' \
            f' ({self.faction})\n\nHP: {self.HP}/{self.MaxHP}\nEP: ' \
            f'{self.EP}/{self.MaxEP}'

class VirtualPlayer(Player):
    def __init__ (self, faction, race, unit_class, unit_name, index, health, \
        difficulty):
        super().__init__(index, health)
        self.difficulty = difficulty
        
    def check_self(self, HP):
        if HP/100 < self.health:
            pass
            
class PlayerCharacter(Player):
    pass
        
class PlayGame:
    def __init__(self):
        self.is_over = False
        self.player_one_turn = True
        self.two_players = False
        self.p1 = ''
        self.p2 = ''
        
    def create_player_one(self):
        self.p1 = PlayGame.create_player(self, self.p1, 1, False)
        
    def create_player_two(self):
        if self.two_players:
            self.p2 = PlayGame.create_player(self, self.p2, 2, False)
        else:
            self.p2 = PlayGame.create_player(self, self.p2, 2, True)
            
    def create_player(self, player, index, is_virtual):
        '''
        This goes through the options to create a player. It requests input
        and fits it in to the PlayerUnit class from the besieged_PlayerUnit
        file.
        '''
        
        if is_virtual:
            player = VirtualPlayer('', '', '', 'Player 2', index, 1, 1)
        player = PlayerCharacter('', '', '', '', index, 1)
        
        player.faction = game.character_creation_subloop('faction', \
            'Choose a faction: ', unit.factions, player.index, is_virtual)
        
        for i in range(len(unit.factions)):
            if i == unit.factions.index(player.faction):
                race_list = unit.races_lists[i]
        
        player.race = game.character_creation_subloop('race', \
            'Choose a race: ', race_list, player.index, is_virtual)
        
        class_list = unit.PlayerUnit.define_unit_type_availability(player)
        
        player.unit_class = game.character_creation_subloop('unit_class', \
            'Choose a class: ', class_list, player.index, is_virtual)
        
        player.unit_name = cap(input('What name would you choose? \n'))
        
        if is_virtual:
            player.is_female = choice([True, False])
        else:
            sex = input('Are you male or female (M/F)? \n')
            player.is_female = True if sex[0:1].lower() == 'f' else False
        if player.race == 'Amazon': player.is_female = True
        
        return player
        
        
    def character_creation_subloop(self, param, input_str, param_list, index, \
        is_virtual):
        err_msg = ''
        if is_virtual:
            return choice(param_list)
        while 1:
            param = cap(input(f'{err_msg}{input_str} {param_list}\n'))
            if param in param_list:
                return param
            err_msg = 'I\'m sorry, that\'s not a valid option. '
            
            
        
'''
GAME CODE START
'''
        
print('BESIEGED: BATTLE ARENA\n\n\n\n')

num_of_players = ''
break_check = 0
game = PlayGame()

while num_of_players != '1' and num_of_players != '2': 
    num_of_players = input('Enter the number of players (1 or 2): ')
    print(num_of_players)
    break_check += 1
    if num_of_players == '2':
        game.two_players = True
    if break_check > 5:
        print(':break: too many failed attempts. 1 player game')
        num_of_players = 1
        break

'''
MAIN LOOP
'''
while 1:
    game.create_player_one()
    game.create_player_two()
    
    print(f'{game.p1.unit_name} VS {game.p2.unit_name}')
    break
