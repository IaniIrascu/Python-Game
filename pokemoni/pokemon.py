import pygame as pg
import sys
import os
from pokemoni.ability_screen.ability_screen import AbilityScreen

ANIMATION_FRAMES = 8
FRAMESPERWIDTH = 4
FRAMESPERHEIGHT = 2
FRAMEWIDTH = FRAMEHEIGHT = 192  # pixels

class PokemonFrames():
    def __init__(self):
        self.idleFrames = []
        self.attackFrames = []
        self.animations = {}
        self.size = (2 * FRAMEWIDTH, 2 * FRAMEHEIGHT)

    def get_idle_frame(self, frame_no):
        if 1 <= frame_no <= len(self.idleFrames) + 1:
            return self.idleFrames[frame_no - 1]
        print("Frame not in list")

    def clear_idle_frames(self):
        self.idleFrames.clear()

    def get_attack_frame(self, frame_no):
        if 1 <= frame_no <= len(self.attackFrames) + 1:
            return self.attackFrames[frame_no - 1]
        print("Frame not in list")

    def clear_attack_frames(self):
        self.attackFrames.clear()

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def extract_animation_frames(self, image):
        image = pg.image.load(image)
        # IDLE FRAMES
        for i in range(0, FRAMESPERWIDTH):
            self.idleFrames.append(pg.Surface((FRAMEWIDTH, FRAMEHEIGHT), pg.SRCALPHA))
            self.idleFrames[i].blit(image, (0, 0), (i * FRAMEWIDTH, 0, FRAMEWIDTH, FRAMEHEIGHT))
            self.idleFrames[i] = pg.transform.scale(self.idleFrames[i], self.size)

        # ATTACK FRAMES
        for i in range(0, FRAMESPERWIDTH):
            self.attackFrames.append(pg.Surface((FRAMEWIDTH, FRAMEHEIGHT), pg.SRCALPHA))
            self.attackFrames[i].blit(image, (0, 0), (i * FRAMEWIDTH, FRAMEHEIGHT, FRAMEWIDTH, FRAMEHEIGHT))
            self.attackFrames[i] = pg.transform.scale(self.attackFrames[i], self.size)

        # Update list of animation
        self.animations["Idle"] = self.idleFrames
        self.animations["Attack"] = self.attackFrames

class PokemonsFrames:
    def __init__(self):
        self.pokemonsFrames = {}

    def get_pokemon_frames(self, image_name):
        if image_name in self.pokemonsFrames:
            return self.pokemonsFrames[image_name]

    def load_all_pokemon_frames(self, folder):
        for i, image_name in enumerate(os.listdir(folder)):
            if image_name not in self.pokemonsFrames:
                pokemonFrames = PokemonFrames()
                pokemonFrames.extract_animation_frames(folder + "/" + image_name)
                self.pokemonsFrames[image_name] = pokemonFrames

    def add_pokemon_frames(self, image_name):
        if image_name not in self.pokemonsFrames:
            pokemonFrames = PokemonFrames()
            pokemonFrames.extract_animation_frames(image_name)
            self.pokemonsFrames[image_name] = pokemonFrames

    def delete_pokemon_frames(self, image_name):
        if image_name in self.pokemonsFrames:
            self.pokemonsFrames.pop(image_name)

# POKEMONUL
class Pokemon:
    def __init__(self, maxHealth = 0, maxEnergy = 0):
        self.pokemonFrames = None
        self.name = None
        self.attack = None
        self.specialAttack = None
        self.isDead = False
        self.isActive = False
        self.level = None
        self.health = None
        self.maxHealth = maxHealth
        self.damage = None
        self.maxEnergy = maxEnergy
        self.energy = None
        self.experience = None
        self.specialAbility = None
        self.effectsOnItself = []

    # Setters
    def set_special_attack(self, specialAttack):
        self.specialAttack = specialAttack

    def set_maxHealth(self, maxHealth):
        self.maxHealth = maxHealth

    def set_maxEnergy(self, maxEnergy):
        self.maxEnergy = maxEnergy

    def set_energy(self, energy):
        self.energy = energy

    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health

    def set_pokemon_frames(self, pokemonFramesClass):
        self.pokemonFrames = pokemonFramesClass

    def set_level(self, level):
        self.level = level

    def set_damage(self, damage):
        self.damage = damage

    def set_isDead(self, isDead):
        self.isDead = isDead

    def set_isActive(self, isActive):
        self.isActive = isActive

    def set_ability_screen(self, ability_screen):
        self.ability_screen = ability_screen

    def set_experience(self, experience):
        self.experience = experience

    def set_attack(self, attack):
        self.attack = attack

    def add_effect_on_itself(self, effect):
        self.effectsOnItself.append(effect)

    # Getters
    def get_experience(self):
        return self.experience

    def get_special_attack(self):
        return self.specialAttack

    def get_maxHealth(self):
        return self.maxHealth

    def get_maxEnergy(self):
        return self.maxEnergy

    def get_energy(self):
        return self.energy

    def get_name(self):
        return self.name

    def get_experience(self):
        return self.experience

    def get_damage(self):
        return self.damage

    def get_health(self):
        return self.health

    def get_level(self):
        return self.level

    def get_pokemon_frames(self):
        return self.pokemonFrames

    def get_isDead(self):
        return self.isDead

    def get_isActive(self):
        return self.isActive

    def get_ability_screen(self):
        return self.ability_screen

    def get_attack(self):
        return self.attack

    def get_effects(self):
        return self.effectsOnItself

    # Functia aceasta modifica experienta pe care o primeste un caracter dupa ce omoara un inamic
    def gain_experience(self, pokemon):
        self.experience += (pokemon.get_level() * 10)

    def check_what_effect_is_over(self):
        for i in range(len(self.effectsOnItself) - 1, -1, -1):
            if self.effectsOnItself[i].get_number_of_turns_left() == 0:
                self.effectsOnItself.pop(i)
