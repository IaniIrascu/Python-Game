import utils.colors as colors

default_size = (350, 350)
default_health = 100
default_energy = 100
default_attack = 5
default_attacksprite = "scratch.png"

pokemons_info = {
    "Atrox.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Charmadillo.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Cindrill.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Cleaf.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Draem.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Finiette.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Finsta.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Friolera.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Gulfin.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Ivieron.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Jacana.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Larvea.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Pluma.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Plumette.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Pouch.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
    "Sparchu.png": {"health": default_health, "energy": default_energy, "size":  default_size, "attack": default_attack, "attacksprites": default_attacksprite},
}

effects_information = {
    "Poison": {"color": colors.PURPLE, "no_of_turns": 2},
    "Restoration": {"color": colors.PINK, "no_of_turns": 2},
    "Stunned": {"color": colors.DARK_GRAY, "no_of_turns": 1},
    "Bleeding": {"color": colors.RED, "no_of_turns": 3},
    "Weakness": {"color": colors.YELLOW, "no_of_turns": 2},
    "Burned": {"color": colors.BLACK, "no_of_turns": 3},
    "Wet": {"color": colors.BLUE, "no_of_turns": 3},
}

# DESCRIERI EFECTE
effects_descriptions = [
    "For every poison effect on the pokemon, that pokemon takes (5 * number_of_poison)% damage of the total remaining health"
    "For every healing effect applied, recover (3 * number_of_healing) % health of the total hp)"
    "(15 * nr_stunned) % skip tura"
    "more damage"
    "less damage"
    "burn lose (5 * nr burned)% energie"
    "cleans last applyed negative effect"
]
