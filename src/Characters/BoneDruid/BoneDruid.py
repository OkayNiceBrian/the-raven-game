import pygame
import sys
from Character import Character
import Abilities.BoneDruid.AbilityList as abilityList

class BoneDruid(Character):

    def __init__(self, 
                character_name = "Bone Druid", 
                description = "Long ago, the Bone Druid was a simple village mage, treating the sick and expecting nothing but peace in return. When the imperial nations started their war for resources and supremacy, the village was burned to the ground. Only ash and bone remained. Driven half mad, the Bone Druid has since dedicated their life to destroying the imperial order. No art is too dark to serve this cause...",
                base_health = 900,
                base_physical = 10,
                base_magic = 90,
                base_phys_resist = 10,
                base_mag_resist = 90,
                abilities = abilityList.abilities,
                ):
        super().__init__(character_name, description, base_health, base_physical, base_magic, base_phys_resist, base_mag_resist, abilities, companion="Calf of Calamity")
        

