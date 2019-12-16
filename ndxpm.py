# import pdb; pdb.set_trace()
from random import randint as rnd


"""
Section 1 - Die Rolls
__________________________


This section consists of virtual die rolls. The initial reason for writing this module was to achieve this function. In table-top role playing games (such as Dungeons and Dragons), many actions that can be taken are hinged on the roll of a die. In these games, it is not uncommon to use dice with a number of sides other than 6 - these dice are called dX, with X being the number of sides. So, if I were to roll a standard six-sided die, that would be considered rolling 1d6. In these games, it is also common to add a modifier to the die roll, representing some affinity or perhaps even hindering effect on whatever action is being attempted. The formula could then be represented as 1d6+2 if I had a bonus of 2, or 2d8-3 if I were to roll two eight-sided dice with a penalty of 3.

The name of this module, ndxpm, derives from this format - n number of x-sided dice, plus a modifier of m. Each method in this section utilizes the _roll_dice method, which generates a random number within a range, and attemps to add a modifier. I included all the standard gaming dice (d4, d6, d8, d10, d12, d20, d100) as well as d1000, a d2 (with customizable output - defaults "heads" or "tails"), a custom dX, and a function to allow for multiple combinations of dice (i.e.: 2d6+1 + 1d8-2). I also allowed for d20 rolls to recognize a natural 20 and a natural 1 (for those utilizing a d20 system).

"""

class DieRoll:
	
	def __init__(self, sides, number, mod):
		self.sides = sides
		self.number = number
		self.mod = mod
		self.min = self.number + self.mod
		self.max = (self.number * self.sides) + self.mod
		self.half = self.max // 2
		self.total = 0

	def __repr__(self):
		return f'{self.total} || {self.number}d{self.sides} + {self.mod}  ({self.min}-{self.max})'
		
	def _roll(self, sides, number, mod = 0):
		for i in range(number):
			self.total += rnd(1, sides)
		self.total += mod

def _roll_dice(num, x, modifier=0):

#	make sure all arguments are of the integer type
	
	params = locals()
	for i in params.values():
		if type(i) != int:
			arg_type = type(i)
			raise TypeError(f"Arguments must be of the \'int\' type. {arg_type} detected: \'{i}\'")

#	do the things!

	result = 0
	for i in range(num):
		result += rnd(1, x)
	return result + modifier

def roll_d4(modifier=0):
	return _roll_dice(1, 4) + modifier

def roll_d6(modifier=0):
	return _roll_dice(1, 6) + modifier

def roll_d8(modifier=0):
	return _roll_dice(1, 8) + modifier

def roll_d10(modifier=0):
	return _roll_dice(1, 10) + modifier

def roll_d20(modifier=0):
	d_result = _roll_dice(1, 20)

	if d_result == 20:
		return f"You rolled a natural 20! Critical hit! ({d_result + modifier})"
	elif d_result == 1:
		return f"You rolled a natural 1! Critical miss! ({d_result + modifier})"
	return d_result + modifier

def roll_prcnt(modifier=0):
	return _roll_dice(1, 100) + modifier

def roll_1000(modifier=0):
	return _roll_dice(1, 1000) + modifier

def roll_cust(x, modifier=0):
	return _roll_dice(1, x) + modifier

def roll_multi_dice(*args):
	"""
	Used for rolling multiple types of dice simultaneously.
	
	Creates multiple instances of the _roll_dice() function.

	Include arguments in a list (the modifier parameter will be optional).

	Valid:		ndxpm.roll_multi_dice([1, 10, 4], [3, 4], [2, 12, -1])
	Invalid:	ndxpm.roll_multi_dice([1, 10, 4], 3, 4, [2], [12, -1])
												  ^not a list
												  		 ^not enough params
	"""
	for arg in args:
		if len(arg) == 2:
			arg.append(0)
		elif len(arg) < 2 or len(arg) > 3:
			raise ValueError("Each list must have at least 2, but no more than 3, numbers.")

	return sum(_roll_dice(li[0], li[1], li[2]) for li in args)

def flip_coin(side_1="heads", side_2="tails"):
	"""Simulates the flip of a coin. Optional parameters for creating custom coins"""
	if _roll_dice(1,2) == 1:
		return side_1
	return side_2
	


# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

character_skills = {

	"arcana": "int",
	"athletics": "str",
	"acrobatics": "dex",
	"persuasion": "cha",
	"stealth": "dex",
	"intimidation": "cha",
	"perception": "wis",
	"sleight of hand": "dex",
	"deception": "cha",
	"animal handling": "wis",
	"history": "int",
	"investigation": "int",
	"nature": "int",
	"religion": "int",
	"insight": "wis",
	"medicine": "wis",
	"survival": "wis",
	"performance": "cha"

}

character_abilities = {
	
	"strength": "STR",
	"endurance": "END",
	"dexterity": "DEX",
	"intelligence": "INT",
	"wisdom": "WIS",
	"charisma": "CHA"

}

character_skills_list = list(sorted(character_skills.keys()))
character_abilities_list = list(character_abilities.values())


character_races_list = ["human", "orc", "elf", "dwarf", "goblin", "kobold", "halfling", "drow", "dragonborn", "half-orc", "half-elf", "gnoll", "ogre", "giant"]
character_classes_list = ["warrior", "mage", "paladin", "cleric", "rogue", "archer", "monk", "ranger", "warlock", "psion", "barbarian", "bard"]



def capitalize(s, style='start'):
	"""
	Capitalizes the first letter of every word in a string passed into it.
	
	Will add functionality to enable different styles of capitalization.
	
	Will shorten the method name for ease of use.
	
	start:	 	Sleight Of Hand
	title:	 	Sleight of Hand
	full_caps:	SLEIGHT OF HAND
	none:		sleight of hand
	wavy:		sLeIgHt Of HaNd
	wavy_rev:	SlEiGhT oF hAnD
	studly:		sLEigHt of hANd
	
	"""
	
	#declarations
	chars_ = [' ', '-']
	lowercase_words_ = ['of', 'the', 'to', 'a', 'an', 'for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'at', 'around', 'by', 'after', 'along', 'for', 'from', 'on', 'with', 'without'] #used by title case
	
	if style == 'start':
		s = s[:1].upper() + s[1:].lower()
	
		foo_ = 0
		for i in s:
			if i in chars_:
				temp_ = s.index(i, foo_) + 1
				s = s[:temp_] + s[temp_:temp_ + 1].upper() + s[temp_ + 1:]
				foo_ = temp_
		return s
		
	elif style == 'full_caps':
		return s.upper()
	
	elif style == 'none':
		return s.lower()
	
	else:
		temp_ = ''
		
		for i in range(len(s)):
			if style == 'wavy':
				bool_ = 0
			elif style == 'wavy_rev':
				bool_ = 1
			elif style == 'studly':
				bool_ = rnd(0, 1)
		
			if s[i] not in chars_:
				if i % 2 == bool_:
					temp_ += s[i].upper()
				else:
					temp_ += s[i].lower()
			else:
				temp_ += s[i]
				
		return temp_
		# s = s[i].upper() if i % 2 == bool_ else s[i].lower for i in range(len(s)) if s[i] not in chars_


my_chars = []	#all new characters' data will be stored here
	
#create a new character
def create_new_char():
	new_char = Character()
	my_chars.append(new_char)
	new_char._new_char()
	print(new_char)

class Character:
	def __init__(self, name="Unnamed", char_race="Undistinguishable", char_class="Adventurer", char_sex = "Unknown"):
		self.name = capitalize(name)
		self.char_race = capitalize(char_race)
		self.char_class = capitalize(char_class)
		self.char_sex = capitalize(char_sex)
		self.char_skills = list([i, 0, False] for i in character_skills_list)
		self.char_abilities = list([i, 10] for i in character_abilities_list)
		self.prof_count_max = 4
		self.hit_die = 0
		self.hit_points = 0
		self.max_hit_points = 0
		self.bloodied = False

	def __repr__(self):

		c_skill = ''
		c_abil = ''
		
		Character._char_skills_update(self)
		
		for i in self.char_skills:
			is_prof = " "
			if i[2]:
				is_prof = "*"
			c_skill += f'{is_prof} {capitalize(i[0])}: {i[1]}\n'
			
		for i in self.char_abilities:
			c_abil += f'  {i[0]}: {i[1]} ({"-" if i[1] < 0 else "+"}{Character._char_abil_score(self, i[0])})\n'

		return f"\n{self.name}: {self.char_sex} {self.char_race} {self.char_class}\n{self.hit_points}/{self.max_hit_points} HP\n\n{c_skill}\n{c_abil}"
		
	def _update_hit_points(self, amount):
		self.hit_points += amount
		if self.hit_points < self.max_hit_points / 2:
			self.bloodied = True
		else:
			self.bloodied = False

	def _new_char(self):
		Character._char_set_name(self)
		Character._char_set_race(self)
		Character._char_set_class(self)
		Character._char_set_sex(self)
		Character._char_set_prof(self)
		Character._char_set_abil(self)
		Character._char_set_hit_points(self)
		
	def _char_abil_score(self, abil):
		if abil.upper() in [i[0] for i in self.char_abilities]:
			_temp = [i[1] for i in self.char_abilities if abil.upper() == i[0]]
			return int(_temp[0]/2) - 5
		else:
			return "BAD ABILITY NAME"
			
	def _char_set_hit_points(self):
		pass

	def _char_set_name(self):
		self.name = None
		while type(self.name) != str:
			self.name = capitalize(input("What is your name? \n"))
		return f"Greetings, {self.name}"

	def _char_set_race(self):
		self.char_race = capitalize(input(f"Select race: {[capitalize(i) for i in sorted(character_races_list)]} \n"))

	def _char_set_class(self):
		
		prof_list_5 = ['paladin', 'cleric']
		
		self.char_class = capitalize(input(f"Select class: {[capitalize(i) for i in sorted(CharacterClass.char_class_list)]} \n"))
		if self.char_class.lower() in prof_list_5:
			self.prof_count_max = 5
			
	def _char_set_sex(self):
		# inititalizing
		answers_ = ['f', 'm']
		question_ = "Are you male or female?"
		err_msg = ''
		i = 0
		
		# funcitonal loop
		while self.char_sex[0] not in answers_:
			self.char_sex = input(f"{err_msg}{question_} \n").lower()
			err_msg = "I'm sorry, I didn't quite catch that. "
			i += 1
			if i >= 3:
				question_ = "Are you [M]ale or [F]emale?"
				
		# end of function
		if self.char_sex[0] == answers_[0]:
			self.char_sex = 'Female'
		if self.char_sex[0] ==  answers_[1]:
			self.char_sex = 'Male'

	def _char_set_prof(self):
		while [i[2] for i in self.char_skills].count(True) < self.prof_count_max:
			self._char_skills_set_proficiency()
		skill_count = 0
		for i in self.char_skills:
			score = Character._char_abil_score(self, character_skills[i[0]])
			Character._char_skills_bonus(self, skill_count, score)
			skill_count += 1
			
	def _char_set_abil(self):
		
		standard_deviation = [16, 14, 13, 12, 11, 10]
		toggle = [False for i in range(6)]
		
		for i in range(6):
			sd_ = standard_deviation[i]
			
			while True:
				
				c_abil = ''
		
				for j in self.char_abilities:
					c_abil += f'  {j[0]}: {j[1]}\n'
				
				sel_ = input(f'Please select a skill to set to {sd_}:\n\n{c_abil}').upper()
				options = [abil[0] for abil in self.char_abilities]
				
				if sel_ in options:
					index = options.index(sel_)
					if toggle[index]:
						print("You've already set that skill.")
					else:
						self.char_abilities[index][1] = sd_
						toggle[index] = True
						break
			
		

	def _char_skills_bonus(self, skill_index, amount=1):
		self.char_skills[skill_index][1] += amount

	def _char_skills_is_proficient(self, skill_index):
		Character._char_skills_bonus(self, skill_index, 5)

	def _char_skills_set_proficiency(self, skill=None):

		display_list = ""
		for i in sorted(self.char_skills):
			tickmark = "-"
			if i[2]:
				tickmark = "+"
			display_list += f" {tickmark} {capitalize(i[0])}\n"
		char_skill_menu_msg = f"Please choose a skill: \n\n{display_list} \n"

		while True:
			
			prof_count = [i[2] for i in self.char_skills].count(True)
			prof_count_r = self.prof_count_max - prof_count
			
			if prof_count >= self.prof_count_max:
				return 'You already have the maximum amount of proficiencies for your class.'
			
			elif skill in [i[0] for i in self.char_skills]:
				skill_index = [i[0] for i in self.char_skills].index(skill)
				if self.char_skills[skill_index][2]:
					err_msg = "You are already proficient in that skill. "
				else:
					self.char_skills[skill_index][2] = True
					Character._char_skills_is_proficient(self, skill_index)
					print(f'\nYou gain a +5 bonus to {capitalize(skill)}.\n\n')
					break
			
			elif skill == "quit":
				print("Function aborted\n")
				break
			
			elif skill == None:
				err_msg = ""

			else:
				err_msg = "That's not a recognized skill. "

			skill = input(f"{err_msg}You have {prof_count_r} proficiencies remaining. {char_skill_menu_msg}").lower()
			
	def _char_skills_update(self):
		for i in self.char_skills:
			amount = 0
			skill_index = -1
			for k, v in character_skills.items():
				if i[0] == k:
					amount = Character._char_abil_score(self, v.upper())
					skill_index = self.char_skills.index(i)
			Character._char_skills_bonus(self, skill_index, amount)
			
	def custom_skill(self):
		print('Please note: adding custom skills does not give you additional proficiency slots.')
		
		new_skill_name = input('What is the name of your skill?\n')
		new_skill_stat = input('Which attribute governs this skill?\n')
		
		print(f'New skill {new_skill_name} added.')
		
class CharacterClass:
	def __init__(self, name):
		self.name = name
		self.hit_die = 0
		self.primary = primary
		self.save_1 = save_1
		self.save_2 = save_2
		self.armor_prof = 'None'
		self.shield_prof = False
		
	armor_types: ['None', 'Light', 'Medium', 'Heavy']
	
	char_class_hit_dice = {
		
		"barbarian": 12,
		"bard": 8,
		"cleric": 8,
		"druid": 8,
		"fighter": 10,
		"monk": 8,
		"paladin": 10,
		"ranger": 10,
		"rogue": 8,
		"sorcerer": 6,
		"warlock": 8,
		"wizard": 6,
		"artificer": 8,
		"blood hunter": 10
		
	}
	
	char_class_list = char_class_hit_dice.keys()
	
class Assign_Class_Prof:
	
	def __init__(self, char_class):
		self.char_class = char_class
		self.profs = []

class Armor:
	
	def __init__(self, name, a_type, ac, dex_max, stealth, str_req):
		
		self.name = name			#proper name of the armor
		self.a_type = a_type		#none, light, medium, or heavy
		self.ac = ac				#ac bonus
		self.dex_max = dex_max		#maximum dex bonus allowed
		self.stealth = False		#true grants stealth disadvantage
		self.str_req = str_req		#required strength for use
		self.magic_bonus = 0		#bonus provided by '+' sign
		
	def __repr__(self):
		_dex = ''
		_stealth = ''
		_str = ''
		_magic = ''
	
		if self.dex_max != -1:
			_dex = self.dex_max
		if self.stealth:
			_stealth = '(Stealth Disadvantage)'
		if self.str_req > 0:
			_str = f'Strength requirement: {self.str_req}'
		if self.magic_bonus != 0:
			if self.magic_bonus > 0:
				_magic = f' +{self.magic_bonus}'
			else:
				_magic = f' {self.magic_bonus}'
		
		print(f'{self.name}{_magic}: {self.ac} {self.a_type} armor {_dex} {_stealth} {str}')
	
	def _max_dex_bonus(self):
		if self.dex_max == -1:
			self.dex_max = Character._char_abil_score(self, 'DEX')