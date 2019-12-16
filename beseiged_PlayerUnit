from random import choice

# This defines the PlayerUnit class. It represents each player controlled unit used in the game.

class PlayerUnit:
    def __init__(self, faction='Garden Laborers', race='Worm', unit_class='Minion', unit_name='Toiler'):
        self.faction = faction                  #one of the large groupings
        self.race = race                        #one of six in a faction
        self.unit_class = unit_class            #the unit class
        self.unit_name = unit_name              #a name of the unit
        self.HP = 5                             #current hit points
        self.MaxHP = 5                          #maximum hit points
        self.EP = 3                             #current energy points
        self.MaxEP = 3                          #maximum energy points
        self.is_dead = False                    #flag for unit death
        self.is_female = choice([True, False])  #generate sex randomly
                
    def __repr__(self):
        
        is_dead_string = '(Deceased)' if self.is_dead else ''
        is_female_string = 'Female' if self.is_female else 'Male'

        return f'\n\nName: {self.unit_name} {is_dead_string}\n{is_female_string} {self.race} {self.unit_class} ({self.faction})\n\nHP: {self.HP}/{self.MaxHP}\nEP: {self.EP}/{self.MaxEP}'
        
    def take_damage (self, dmg):
        self.HP -= dmg
        if self.HP < 1:
            PlayerUnit.kill_unit(self)
            self.HP = 0
        
    def heal (self, heal):
        self.HP += heal
        if heal + self.HP > self.MaxHP:
            self.HP = self.MaxHP
        
    def kill_unit(self):
        self.is_dead = True
        
    def revive_unit(self):
        self.is_dead = False
        
    def define_unit_type_availability(self):
        unit_type_range = ''
        unit_type_range_f = ''
        
        '''
    Default Setting
        '''
        if self.race == 'Worm':
            unit_type_range = ['Minion']
            unit_type_range_f = ['Special']
            '''
    Emperian Units
            '''
        elif self.race == 'Amazon':
            unit_type_range = ['Aegis','Deceiver','Destroyer','Minion','Ranger']
            PlayerUnit(self).is_female = True #Amazon is an all female race
        elif self.race == 'Dwarf':
            unit_type_range = ['Aegis', 'Destroyer', 'Mender', 'Minion', 'Shaper']
        elif self.race == 'Elf':
            unit_type_range = ['Caster', 'Deceiver', 'Mender', 'Minion', 'Ranger']
        elif self.race == 'Human':
            unit_type_range = ['Aegis', 'Caster', 'Destroyer', 'Minion', 'Shaper']
        elif self.race == 'Satyr':
            unit_type_range = ['Caster', 'Deceiver', 'Mender', 'Minion', 'Shaper']
        elif self.race == 'Symian':
            unit_type_range = ['Caster', 'Mender', 'Minion', 'Ranger', 'Shaper']
            '''
    Outlander Units
            '''
        elif self.race == 'Gypsy':
            unit_type_range = ['Caster', 'Deceiver', 'Mender', 'Minion', 'Shaper']
        elif self.race == 'Lamian':
            unit_type_range = ['Caster', 'Deceiver', 'Destroyer', 'Minion', 'Ranger']
        elif self.race == 'Lycan':
            unit_type_range = ['Aegis', 'Deceiver', 'Minion', 'Ranger', 'Shaper']
        elif self.race == 'Minotaur':
            unit_type_range = ['Aegis', 'Destroyer', 'Minion', 'Ranger', 'Shaper']
        elif self.race == 'Orc':
            unit_type_range = ['Aegis', 'Destroyer', 'Mender', 'Minion', 'Ranger']
        elif self.race == 'Troll':
            unit_type_range = ['Aegis', 'Caster', 'Mender', 'Minion', 'Shaper']
            '''
    Safety Pass
            '''
        else:
            pass
            
        for i in range(len(unit_type_range)):
            unit_types[unit_type_range[i]] = True
        for i in range(len(unit_type_range_f)):
            unit_types[unit_type_range_f[i]] = False
            
        return unit_type_range

factions = ['Emperians', 'Outlanders', 'Netherrealmers']
races_emp = ['Amazon', 'Dwarf', 'Elf', 'Human', 'Satyr', 'Symian']
races_out = ['Gypsy', 'Lamian', 'Lycan', 'Minotaur', 'Orc', 'Troll']
races_net = ['Demon', 'Djinn', 'Necron', 'Porphyrian', 'Specter', 'Wendigo']
races_lists = [races_emp, races_out, races_net]
unit_types = {
            'Aegis': False,
            'Caster': False,
            'Deceiver': False,
            'Destroyer': False,
            'Mender': False,
            'Minion': False,
            'Ranger': False,
            'Shaper': False,
            'Special': True
        }

# class PlayerUnitRace(PlayerUnit):
#     '''
#     Defines the Race object for use in units. A race determines certain passive bonuses and which unit_types are available from the beginning. 
#     '''
    
#     def __init__(self, faction, race, unit_type, unit_name):
#         super().__init__(faction, unit_type, unit_name)
#         self.race = race
#         self.unit_types = {
#             'Aegis': False,
#             'Caster': False,
#             'Deceiver': False,
#             'Destroyer': False,
#             'Mender': False,
#             'Minion': False,
#             'Ranger': False,
#             'Shaper': False,
#             'Special': True
#         }
#         self.abil_racial_a = ''
#         self.abil_racial_b = ''
#         self.abil_racial_c = ''
    
#     def __repr__(self):
#         return self.race
        
#     def define_unit_type_availability(self):
#         unit_type_range = ''
#         unit_type_range_f = ''
        
#         '''
#     Default Setting
#         '''
#         if self.race == 'Worm':
#             unit_type_range = ['Minion']
#             unit_type_range_f = ['Special']
#             '''
#     Emperian Units
#             '''
#         elif self.race == 'Amazon':
#             unit_type_range = ['Aegis','Deceiver','Destroyer','Minion','Ranger']
#             PlayerUnit(self).is_female = True #Amazon is an all female race
#         elif self.race == 'Dwarf':
#             unit_type_range = ['Aegis', 'Destroyer', 'Mender', 'Minion', 'Shaper']
#         elif self.race == 'Elf':
#             unit_type_range = ['Caster', 'Deceiver', 'Mender', 'Minion', 'Ranger']
#         elif self.race == 'Human':
#             unit_type_range = ['Aegis', 'Caster', 'Destroyer', 'Minion', 'Shaper']
#         elif self.race == 'Satyr':
#             unit_type_range = ['Caster', 'Deceiver', 'Mender', 'Minion', 'Shaper']
#         elif self.race == 'Symian':
#             unit_type_range = ['Caster', 'Mender', 'Minion', 'Ranger', 'Shaper']
#             '''
#     Outlander Units
#             '''
#         elif self.race == 'Gypsy':
#             unit_type_range = ['Caster', 'Deceiver', 'Mender', 'Minion', 'Shaper']
#         elif self.race == 'Lamian':
#             unit_type_range = ['Caster', 'Deceiver', 'Destroyer', 'Minion', 'Ranger']
#         elif self.race == 'Lycan':
#             unit_type_range = ['Aegis', 'Deceiver', 'Minion', 'Ranger', 'Shaper']
#         elif self.race == 'Minotaur':
#             unit_type_range = ['Aegis', 'Destroyer', 'Minion', 'Ranger', 'Shaper']
#         elif self.race == 'Orc':
#             unit_type_range = ['Aegis', 'Destroyer', 'Mender', 'Minion', 'Ranger']
#         elif self.race == 'Troll':
#             unit_type_range = ['Aegis', 'Caster', 'Mender', 'Minion', 'Shaper']
#             '''
#     Safety Pass
#             '''
#         else:
#             pass
            
#         for i in range(len(unit_type_range)):
#             self.unit_types[unit_type_range[i]] = True
#         for i in range(len(unit_type_range_f)):
#             self.unit_types[unit_type_range_f[i]] = False
            
#     def define_racial_abilities(self):
#         pass
                
# class PlayerUnitFaction:
    
#     def __init__(self, name, races):
#         self.name = name
#         self.races = races
        
#     def __repr__(self):
#         return(f'{self.name} ({self.races})')
        
#     def get_races(self):
#         pass
