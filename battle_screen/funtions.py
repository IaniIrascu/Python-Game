from pokemoni.ability_screen.ability_screen import *
import random

FONT = pg.font.Font("./main_menu/assets/minecraft.ttf", 24)

def check_button_pressed(mouse_pos, ability_screen, ability_screen_position):
    buttons = ability_screen.get_buttons()
    for button_name in buttons:
        button_rect = pg.Rect(ability_screen_position[0] + buttons[button_name].get_position()[0],
                              ability_screen_position[1] + buttons[button_name].get_position()[1],
                              buttons[button_name].get_size()[0],
                              buttons[button_name].get_size()[1])
        if button_rect.collidepoint(mouse_pos):
            return button_name

# NU SCHIMBATI NUMERE PRIN PROGRAM
def change_health_bar(health_bar, bars_surface, percentage, text_surface):
    removeFromBar = (health_bar.get_width() - 115) * percentage
    width = health_bar.get_width()
    height = health_bar.get_height()
    health_bar.fill((0, 0, 0, 0))
    health_bar.fill(RED, (90, 37, width - 115 - removeFromBar, height / 3))
    health_bar.blit(text_surface, (145, 45))
    health_bar.blit(bars_surface, (0, 0), (0, 0, width, height))

def change_energy_bar(energy_bar, bars_surface, percentage, text_surface):
    removeFromBar = (energy_bar.get_width() - 115) * percentage
    width = energy_bar.get_width()
    height = energy_bar.get_height()
    energy_bar.fill((0, 0, 0, 0))
    energy_bar.fill(BLUE, (90, 37, width - 115 - removeFromBar, height / 3))
    energy_bar.blit(text_surface, (145, 45))
    energy_bar.blit(bars_surface, (0, 0), (0, height, width, height))

def remove_effects_turns(effects, effects_names):
    for effect in effects:
        if effect.get_name() in effects_names:
            effect.set_number_of_turns_left(effect.get_number_of_turns_left() - 1)
            effect.change_effectIcon(color=effect.get_color(), number=effect.get_number_of_turns_left())

def calculate_damage(attacking_pokemon, attacked_pokemon):
    damage = attacking_pokemon.get_damage()
    for effect in attacked_pokemon.get_effects():
        effect_name = effect.get_name()
        if effect_name == "Bleeding":
            damage += attacking_pokemon.get_damage() * 0.1 * effect.get_number_of_turns_left()
        if effect_name == "Weakness":
            damage -= attacking_pokemon.get_damage() * 0.1 * effect.get_number_of_turns_left()
        if effect_name == "Stunned":
            chance = 5 * effect.get_number_of_turns_left()
            if chance > 100:
                chance = 100
            randomnumber = random.randint(1, 100)
            if randomnumber > chance:
                return 0
    if damage < 0:
        damage = 0
    return damage

def calculate_passive_damage(pokemon):
    damage = 0
    for effect in pokemon.get_effects():
        effect_name = effect.get_name()
        if effect_name == "Restoration":
            damage -= pokemon.get_maxHealth() * 0.5 * effect.get_number_of_turns_left()
        if effect_name == "Poison":
            damage += 0.1 * pokemon.get_health() * effect.get_number_of_turns_left()
    return damage

def modify_health(pokemon, damage):
    health = pokemon.get_health()
    health -= damage
    if health <= 0:
        return "DEAD"
    elif health > pokemon.get_maxHealth():
        pokemon.set_health(pokemon.get_maxHealth())
    else:
        pokemon.set_health(health)

def reset_pokemons(player_pokemons, enemies):
    for pokemon in player_pokemons:
        pokemon.set_health(pokemon.get_maxHealth())
        pokemon.set_isDead(False)
        pokemon.set_energy(pokemon.get_maxEnergy())
        pokemon.get_effects().clear()

    for enemies in enemies:
        enemies.set_health(enemies.get_maxHealth())
        enemies.set_isDead(False)
        enemies.set_energy(enemies.get_maxEnergy())
        enemies.get_effects().clear()

def create_ability_screen():
    ability_screen = AbilityScreen()
    ability_screen.create_ability_screen()
    return ability_screen

def passive_update_pokemon(pokemon, last_pokemon, effects_end_of_turn):
    # PASSIVE DAMAGE AFTER ATTACKING
    damage = calculate_passive_damage(pokemon)
    if modify_health(pokemon, damage) == "DEAD":
        pokemon.set_isDead(True)  # Inamicul moare
        if last_pokemon.get_isDead():  # Daca a murit ultimul inamic se trece in meniu
            return "MainMenu"
        return "DEAD"
    # Check if lose energy
    for effect in pokemon.get_effects():
        if effect.get_name() == "Burned":
            energy = pokemon.get_energy()
            energy -= 0.05 * effect.get_number_of_turns_left() * energy
            if energy <= 0:
                energy = 0
            pokemon.set_energy(energy)
    # Check if effect applied to itself is over
    remove_effects_turns(pokemon.get_effects(), effects_end_of_turn)
    pokemon.check_what_effect_is_over()

def active_update_pokemon(pokemon_attacking, pokemon_attacked, last_pokemon, effect_when_attacked):
    # ACTIVE DAMAGE
    damage = calculate_damage(pokemon_attacking, pokemon_attacked)
    if modify_health(pokemon_attacked, damage) == "DEAD":
        pokemon_attacked.set_isDead(True)  # Inamicul moare
        if last_pokemon.get_isDead():  # Daca a murit ultimul inamic se trece in meniu
            return "MainMenu"
        return "DEAD"
    # Check if effect on the other pokemon is over after attack
    remove_effects_turns(pokemon_attacked.get_effects(), effect_when_attacked)
    pokemon_attacked.check_what_effect_is_over()