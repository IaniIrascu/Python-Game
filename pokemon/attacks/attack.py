import pygame as pg
import os

FRAMEWIDTH = FRAMEHEIGHT = 192
FRAMESPERWIDTH = 4

# Clasa care salveaza frame-urile pentru un obiect
class AttackFrames:
    def __init__(self):
        self.attackFrames = []
        self.size = (FRAMEWIDTH, FRAMEHEIGHT)

    def get_attack_frame(self, n):
        if 1 <= n <= len(self.attackFrames) + 1:
            return self.attackFrames[n - 1]
        else:
            print("NO FRAME")
            return None

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def extract_ability_attack_frames(self, image):
        image = pg.image.load(image)
        # ABILITY ATTACK FRAMES
        for i in range(0, FRAMESPERWIDTH):
            self.attackFrames.append(pg.Surface((FRAMEWIDTH, FRAMEHEIGHT), pg.SRCALPHA))
            self.attackFrames[i].blit(image, (0, 0), (i * FRAMEWIDTH, 0, FRAMEWIDTH, FRAMEHEIGHT))
            self.attackFrames[i] = pg.transform.scale(self.attackFrames[i], (self.size[0], self.size[1]))

class AttacksFrames:
    def __init__(self):
        self.attacksFrames = {}

    def get_attack_frames(self, image_name):
        if image_name in self.attacksFrames:
            return self.attacksFrames[image_name]

    def load_all_attacks_frames(self, folder):
        for i, image_name in enumerate(os.listdir(folder)):
            if image_name not in self.attacksFrames:
                attackFrames = AttackFrames()
                # Se updateaza frame-urile pentru atacul curent
                attackFrames.extract_ability_attack_frames(folder + "/" + image_name)
                # Se adauga la dictionarul de atack frames inca un element
                self.attacksFrames[image_name] = attackFrames

    def add_attack_frames(self, image_name):
        if image_name not in self.attacksFrames:
            attackFrames = AttackFrames()
            # Se updateaza frame-urile pentru atacul curent
            attackFrames.extract_ability_attack_frames(image_name)
            # Se adauga la dictionarul de atack frames inca un element
            self.attacksFrames[image_name] = attackFrames

    def delete_attack_frames(self, image_name):
        if image_name in self.attacksFrames:
            self.attacksFrames.pop(image_name)

class SpecialAttack:
    def __init__(self):
        self.attackFrames = None  # Aceasta variabila retine un obiect in cadrul ei
        self.effects = None
        self.name = None
        self.energy_cost = None

    def set_effects(self, effects):
        self.effects = effects

    def set_name(self, name):
        self.name = name

    def set_energy_cost(self, cost):
        self.energy_cost = cost

    def get_effects(self):
        return self.effects

    def get_name(self):
        return self.name

    def get_energy_cost(self):
        return self.energy_cost

    def set_attack_frames(self, attackFramesClass):
        self.attackFrames = attackFramesClass

    def get_attack_frames(self):
        return self.attackFrames

class Attack:
    def __init__(self):
        self.attackFrames = None
        self.name = None

    def set_name(self, name):
        self.name = name

    def set_attack_frames(self, attackFrames):
        self.attackFrames = attackFrames

    def get_name(self):
        return self.name

    def get_attack_frames(self):
        return self.attackFrames