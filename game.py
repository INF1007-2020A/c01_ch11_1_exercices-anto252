import random
import utils

class Weapon:
	def __init__(self, nom: str, power: int, niveau: int):
		self.nom = nom
		self.power = power
		self.niv_min = niveau
		print(f"L'arme choisie est {nom}, avec un dégat de {power} et il faut être au niveau {niveau} pour l'utiliser")

	def make_unarmed(self):
		self.nom = "Unarmed"
		self.power = 20
		print("le personnage unarmed a été créé")

class Character:
	def __init__(self, level, weapon: "weapon"):
		self.level = level
		self.weapon = weapon
	def compute_damage(self, defendant: "Character") -> float:
		return 


	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage



'''
def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués
'''


Weapon("shotgun", 50, 2)
