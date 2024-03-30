import pygame
import sys
from Character import Character
import Abilities.BoneDruid.AbilityList as abilityList

class BoneDruid(Character):

    def __init__(self, 
                character_name = "Bone Druid", 
                base_health = 900,
                base_physical = 10,
                base_magic = 90,
                base_phys_resist = 10,
                base_mag_resist = 90,
                abilities = abilityList.abilities,
                ):
        super().__init__(character_name, base_health, base_physical, base_magic, base_phys_resist, base_mag_resist, abilities, companion="Calf of Calamity")
        

